import base64
import os
import shutil
import time
import uuid

import requests

from config import (
    COMFY_URL,
    OUTPUT_DIR,
    POLL_INTERVAL,
    TIMEOUT,
)


def queue_prompt(workflow):
    response = requests.post(
        f"{COMFY_URL}/prompt",
        json={"prompt": workflow},
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()
    if "prompt_id" not in data:
        raise RuntimeError(f"Unexpected ComfyUI response: {data}")
    return data["prompt_id"]


def wait_until_finished(prompt_id):
    start = time.time()

    while True:
        if time.time() - start > TIMEOUT:
            raise TimeoutError("ComfyUI generation timeout.")

        response = requests.get(
            f"{COMFY_URL}/history/{prompt_id}",
            timeout=30,
        )
        response.raise_for_status()

        history = response.json()

        if prompt_id in history:
            outputs = history[prompt_id].get("outputs", {})
            if outputs:
                return outputs

        time.sleep(POLL_INTERVAL)


def find_video(outputs):
    for node in outputs.values():
        for key in ("videos", "gifs", "files", "images"):
            if key not in node:
                continue

            for item in node[key]:
                filename = item.get("filename")
                if filename and filename.lower().endswith(".mp4"):
                    return item

    raise RuntimeError("No MP4 returned by ComfyUI.")


def locate_video(video):
    filename = video["filename"]
    subfolder = video.get("subfolder", "")

    candidates = [
        os.path.join("/ComfyUI/output", subfolder, filename),
        os.path.join("/workspace/ComfyUI/output", subfolder, filename),
        os.path.join("/app/output", subfolder, filename),
        os.path.join("/app/output", filename),
    ]

    for path in candidates:
        if os.path.exists(path):
            return path

    raise FileNotFoundError(f"Unable to locate generated video: {filename}")


def copy_video(source_path):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    destination = os.path.join(
        OUTPUT_DIR,
        f"{uuid.uuid4().hex}.mp4",
    )

    shutil.copy2(source_path, destination)

    return destination


def encode_video(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def generate_one(workflow):
    prompt_id = queue_prompt(workflow)
    outputs = wait_until_finished(prompt_id)
    video = find_video(outputs)
    source = locate_video(video)
    destination = copy_video(source)
    return destination


def generate(workflows):
    videos = []
    failed = []

    for item in workflows:
        try:
            output_path = generate_one(item["workflow"])

            videos.append({
                "name": item["name"],
                "filename": os.path.basename(output_path),
                "base64": encode_video(output_path),
            })

        except Exception as exc:
            failed.append({
                "name": item.get("name", "unknown"),
                "error": str(exc),
            })

    if not videos:
        raise RuntimeError("All video generations failed.")

    return {
        "count": len(videos),
        "videos": videos,
        "failed": failed,
    }
