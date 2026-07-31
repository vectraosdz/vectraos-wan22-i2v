import base64
import mimetypes
import uuid
from pathlib import Path

from config import INPUT_DIR
from config import OUTPUT_DIR
from config import TMP_DIR


def ensure_directories():

    for directory in (
        INPUT_DIR,
        OUTPUT_DIR,
        TMP_DIR
    ):
        directory.mkdir(
            parents=True,
            exist_ok=True
        )


def unique_filename(extension):

    if not extension.startswith("."):
        extension = "." + extension

    return f"{uuid.uuid4().hex}{extension}"


def file_extension(path):

    return Path(path).suffix.lower()


def mime_type(path):

    mime, _ = mimetypes.guess_type(path)

    return mime or "application/octet-stream"


def read_bytes(path):

    with open(path, "rb") as f:
        return f.read()


def write_bytes(path, data):

    path = Path(path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(path, "wb") as f:
        f.write(data)

    return str(path)


def file_to_base64(path):

    with open(path, "rb") as f:
        return base64.b64encode(
            f.read()
        ).decode("utf-8")


def base64_to_file(data, extension=".bin"):

    filename = unique_filename(extension)

    path = INPUT_DIR / filename

    with open(path, "wb") as f:
        f.write(base64.b64decode(data))

    return str(path)


def list_videos():

    return sorted(

        OUTPUT_DIR.glob("*.mp4"),

        key=lambda x: x.stat().st_mtime

    )


def latest_video():

    videos = list_videos()

    if not videos:
        return None

    return str(videos[-1])


def delete_file(path):

    try:
        Path(path).unlink(
            missing_ok=True
        )
    except Exception:
        pass
