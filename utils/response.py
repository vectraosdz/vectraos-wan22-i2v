import time


def video(name, base64_data, filename=None):
    return {
        "name": name,
        "filename": filename,
        "base64": base64_data,
    }


def merge(video_names, encoded_videos, filenames=None):
    if filenames is None:
        filenames = [None] * len(video_names)

    videos = []

    for name, data, filename in zip(
        video_names,
        encoded_videos,
        filenames,
    ):
        videos.append(
            video(
                name=name,
                base64_data=data,
                filename=filename,
            )
        )

    return videos


def success(
    videos,
    product_type=None,
    language=None,
    quality=None,
    failed=None,
):
    if failed is None:
        failed = []

    return {
        "success": True,
        "timestamp": int(time.time()),
        "video_count": len(videos),
        "failed_count": len(failed),
        "product_type": product_type,
        "language": language,
        "quality": quality,
        "videos": videos,
        "failed": failed,
    }


def error(message, details=None):
    payload = {
        "success": False,
        "timestamp": int(time.time()),
        "error": str(message),
    }

    if details is not None:
        payload["details"] = details

    return payload
