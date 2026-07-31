import base64
import mimetypes
import uuid
from pathlib import Path

import requests

from config import INPUT_DIR


def _extension_from_content_type(content_type):

    if not content_type:
        return ".jpg"

    ext = mimetypes.guess_extension(
        content_type.split(";")[0].strip()
    )

    return ext or ".jpg"


def _save_bytes(data, extension):

    filename = f"{uuid.uuid4().hex}{extension}"

    filepath = INPUT_DIR / filename

    filepath.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(filepath, "wb") as f:
        f.write(data)

    return str(filepath)


def _download_from_url(url):

    response = requests.get(
        url,
        timeout=60
    )

    response.raise_for_status()

    extension = _extension_from_content_type(
        response.headers.get("Content-Type")
    )

    return _save_bytes(
        response.content,
        extension
    )


def _decode_base64(image_data):

    if image_data.startswith("data:"):

        header, image_data = image_data.split(",", 1)

        content_type = header.split(";")[0].replace(
            "data:",
            ""
        )

        extension = _extension_from_content_type(
            content_type
        )

    else:

        extension = ".jpg"

    binary = base64.b64decode(image_data)

    return _save_bytes(
        binary,
        extension
    )


def download_image(job_input):

    image_path = job_input.get("image_path")

    if image_path:

        image_path = Path(image_path)

        if not image_path.exists():

            raise FileNotFoundError(
                f"Image not found: {image_path}"
            )

        return str(image_path)

    image_url = job_input.get("image_url")

    if image_url:

        return _download_from_url(
            image_url
        )

    image_base64 = job_input.get("image_base64")

    if image_base64:

        return _decode_base64(
            image_base64
        )

    raise ValueError(
        "One of image_path, image_url or image_base64 is required."
    )
