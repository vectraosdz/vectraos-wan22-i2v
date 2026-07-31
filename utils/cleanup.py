import shutil

from config import INPUT_DIR
from config import OUTPUT_DIR
from config import TMP_DIR
from config import WORKFLOW_DIR


GENERATED_DIR = WORKFLOW_DIR / "generated"


def _clear_directory(directory):

    if not directory.exists():
        return

    for item in directory.iterdir():

        try:

            if item.is_file() or item.is_symlink():

                item.unlink()

            elif item.is_dir():

                shutil.rmtree(item)

        except Exception:

            pass


def cleanup_inputs():

    _clear_directory(INPUT_DIR)

    _clear_directory(TMP_DIR)


def cleanup_outputs():

    _clear_directory(OUTPUT_DIR)


def cleanup_generated_workflows():

    GENERATED_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    _clear_directory(GENERATED_DIR)


def cleanup():

    cleanup_inputs()

    cleanup_outputs()

    cleanup_generated_workflows()
