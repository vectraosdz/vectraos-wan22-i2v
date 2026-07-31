from config import DEFAULT_WORKFLOW
from utils.product_detector import get_category
from utils.video_profiles import build_video_settings


def validate_job(job_input):

    if not any([
        job_input.get("image_url"),
        job_input.get("image_base64"),
        job_input.get("image_path")
    ]):
        raise ValueError(
            "One of image_url, image_base64 or image_path is required."
        )

    quality = str(
        job_input.get(
            "quality",
            "balanced"
        )
    ).lower()

    settings = build_video_settings(
        quality
    )

    settings["duration"] = float(
        job_input.get(
            "duration",
            settings.get(
                "duration",
                5
            )
        )
    )

    if settings["duration"] <= 0:
        raise ValueError(
            "duration must be greater than 0."
        )

    settings["fps"] = float(
        job_input.get(
            "fps",
            settings.get(
                "fps",
                16
            )
        )
    )

    if settings["fps"] <= 0:
        raise ValueError(
            "fps must be greater than 0."
        )

    settings["width"] = int(
        job_input.get(
            "width",
            settings.get(
                "width",
                832
            )
        )
    )

    settings["height"] = int(
        job_input.get(
            "height",
            settings.get(
                "height",
                480
            )
        )
    )

    if settings["width"] <= 0 or settings["height"] <= 0:
        raise ValueError(
            "width and height must be greater than 0."
        )

    settings["seed"] = job_input.get(
        "seed",
        -1
    )

    settings["workflow"] = job_input.get(
        "workflow",
        DEFAULT_WORKFLOW
    )

    settings["language"] = str(
        job_input.get(
            "language",
            "English"
        )
    )

    settings["quality"] = quality

    settings["product_type"] = get_category(
        job_input
    )

    return settings
