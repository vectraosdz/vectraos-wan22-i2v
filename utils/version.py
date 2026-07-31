VERSION = "1.0.0"

WORKER_NAME = "WAN 2.2 RunPod Worker"

ENGINE = "WAN-2.2"

AUTHOR = "VectraOS"

BUILD = "2026.07"

SUPPORTED_FORMATS = [

    "jpg",

    "jpeg",

    "png",

    "webp"

]

SUPPORTED_OUTPUT = [

    "mp4"

]

DEFAULT_LANGUAGE = "English"

DEFAULT_QUALITY = "balanced"

DEFAULT_CAMERA_MODES = [

    "orbit",

    "macro",

    "lifestyle"

]


def info():

    return {

        "worker": WORKER_NAME,

        "engine": ENGINE,

        "version": VERSION,

        "build": BUILD,

        "author": AUTHOR,

        "quality": DEFAULT_QUALITY,

        "languages": [

            "English",

            "French",

            "Arabic"

        ],

        "camera_modes": DEFAULT_CAMERA_MODES,

        "input_formats": SUPPORTED_FORMATS,

        "output_formats": SUPPORTED_OUTPUT

    }
