import requests

from config import COMFY_URL


def comfy_is_ready():

    try:

        response = requests.get(

            f"{COMFY_URL}/system_stats",

            timeout=5

        )

        return response.status_code == 200

    except Exception:

        return False


def wait_for_comfy(interval=2):

    import time

    while not comfy_is_ready():

        time.sleep(interval)

    return True


def get_queue():

    try:

        response = requests.get(

            f"{COMFY_URL}/queue",

            timeout=5

        )

        response.raise_for_status()

        return response.json()

    except Exception:

        return None


def get_history(prompt_id):

    try:

        response = requests.get(

            f"{COMFY_URL}/history/{prompt_id}",

            timeout=5

        )

        response.raise_for_status()

        return response.json()

    except Exception:

        return None


def ping():

    return {

        "status": "ok" if comfy_is_ready() else "starting"

    }
