import runpod

from utils.cleanup import (
    cleanup_generated_workflows,
    cleanup_inputs,
)
from utils.comfy import generate
from utils.download import download_image
from utils.health import wait_for_comfy
from utils.logger import log
from utils.prompt_builder import build_prompts
from utils.response import success, error
from utils.validator import validate_job
from utils.workflow import process_jobs


wait_for_comfy()


def handler(job):
    cleanup_inputs()
    cleanup_generated_workflows()

    try:
        log("========== NEW JOB ==========")

        job_input = job.get("input", {})

        settings = validate_job(job_input)

        image_path = download_image(job_input)

        prompts = build_prompts(
            product_type=settings["product_type"],
            language=settings["language"],
        )

        workflows = process_jobs(
            image_path=image_path,
            angles=prompts,
            workflow_name=settings["workflow"],
            width=settings["width"],
            height=settings["height"],
            duration=settings["duration"],
            fps=settings["fps"],
            cfg=settings["cfg"],
            steps=settings["steps"],
            seed=settings["seed"],
        )

        result = generate(workflows)

        response = success(
            videos=result["videos"],
            product_type=settings["product_type"],
            language=settings["language"],
            quality=settings["quality"],
        )

        response["failed"] = result.get("failed", [])

        cleanup_inputs()
        cleanup_generated_workflows()

        return response

    except Exception as exc:
        log(f"ERROR: {exc}")

        cleanup_inputs()
        cleanup_generated_workflows()

        return error(str(exc))


runpod.serverless.start({"handler": handler})
