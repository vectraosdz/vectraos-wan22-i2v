from copy import deepcopy


QUALITY_PRESETS = {

    "fast": {

        "steps": 12,
        "cfg": 3.0,
        "guidance_scale": 3.0,
        "scheduler": "normal",
        "fps": 16,
        "duration": 5,
        "width": 832,
        "height": 480

    },

    "balanced": {

        "steps": 20,
        "cfg": 3.5,
        "guidance_scale": 3.5,
        "scheduler": "normal",
        "fps": 16,
        "duration": 5,
        "width": 832,
        "height": 480

    },

    "premium": {

        "steps": 30,
        "cfg": 4.0,
        "guidance_scale": 4.0,
        "scheduler": "normal",
        "fps": 16,
        "duration": 5,
        "width": 832,
        "height": 480

    }

}


DEFAULT_NEGATIVE_PROMPT = (
    "low quality, blurry, watermark, text, logo, "
    "deformed, duplicate, bad anatomy, distorted"
)


CAMERA_PROFILES = {

    "orbit": {

        "name": "orbit",

        "suffix": (
            "cinematic orbit camera, slow rotation around the product, "
            "premium lighting, shallow depth of field, highly realistic"
        )

    },

    "macro": {

        "name": "macro",

        "suffix": (
            "macro lens, close-up details, soft cinematic lighting, "
            "premium commercial quality, ultra realistic"
        )

    },

    "lifestyle": {

        "name": "lifestyle",

        "suffix": (
            "real person naturally using the product, commercial advertising, "
            "beautiful environment, cinematic movement, realistic"
        )

    },

    "hero": {

        "name": "hero",

        "suffix": (
            "hero shot, dramatic lighting, luxury advertising, "
            "slow cinematic camera"
        )

    },

    "reveal": {

        "name": "reveal",

        "suffix": (
            "product reveal, smooth cinematic movement, "
            "high-end commercial advertisement"
        )

    },

    "closeup": {

        "name": "closeup",

        "suffix": (
            "extreme close-up, premium product details, "
            "beautiful reflections, cinematic"
        )

    }

}


def get_quality(name="balanced"):

    if name not in QUALITY_PRESETS:
        name = "balanced"

    return deepcopy(QUALITY_PRESETS[name])


def get_camera(name):

    if name not in CAMERA_PROFILES:
        raise ValueError(f"Unknown camera profile: {name}")

    return deepcopy(CAMERA_PROFILES[name])


def build_video_settings(quality="balanced"):

    settings = get_quality(quality)

    settings["negative_prompt"] = DEFAULT_NEGATIVE_PROMPT

    return settings


def available_qualities():

    return list(QUALITY_PRESETS.keys())


def available_cameras():

    return list(CAMERA_PROFILES.keys())


def default_cameras():

    return [

        get_camera("orbit"),

        get_camera("macro"),

        get_camera("lifestyle"),

    ]
