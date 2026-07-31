from pathlib import Path
import os


# -----------------------------------------------------------------------------
# ComfyUI
# -----------------------------------------------------------------------------

COMFY_URL = os.getenv(
    "COMFY_URL",
    "http://127.0.0.1:8188"
)

TIMEOUT = int(
    os.getenv(
        "TIMEOUT",
        "1800"
    )
)

POLL_INTERVAL = float(
    os.getenv(
        "POLL_INTERVAL",
        "2"
    )
)


# -----------------------------------------------------------------------------
# Directories
# -----------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

INPUT_DIR = BASE_DIR / "input"

OUTPUT_DIR = BASE_DIR / "output"

TMP_DIR = BASE_DIR / "tmp"

WORKFLOW_DIR = BASE_DIR / "workflows"

GENERATED_WORKFLOW_DIR = WORKFLOW_DIR / "generated"


# -----------------------------------------------------------------------------
# Default workflow
# -----------------------------------------------------------------------------

DEFAULT_WORKFLOW = os.getenv(
    "DEFAULT_WORKFLOW",
    "vectraos_wan2.2"
)


# -----------------------------------------------------------------------------
# Default generation settings
# -----------------------------------------------------------------------------

DEFAULT_WIDTH = 832

DEFAULT_HEIGHT = 480

DEFAULT_DURATION = 5

DEFAULT_FPS = 16

DEFAULT_CFG = 6.0

DEFAULT_STEPS = 30

DEFAULT_SEED = -1


# -----------------------------------------------------------------------------
# Create directories automatically
# -----------------------------------------------------------------------------

for directory in (

    INPUT_DIR,

    OUTPUT_DIR,

    TMP_DIR,

    GENERATED_WORKFLOW_DIR,

):

    directory.mkdir(

        parents=True,

        exist_ok=True,

    )
