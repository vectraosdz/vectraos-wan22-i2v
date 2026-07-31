from utils.video_profiles import (
    get_camera,
    DEFAULT_NEGATIVE_PROMPT,
)


DEFAULT_STYLE = (
    "ultra realistic, cinematic commercial advertisement, "
    "professional product videography, premium lighting, "
    "8k, HDR, shallow depth of field, highly detailed"
)


PRODUCT_PROMPTS = {

    "generic":
        "A premium product displayed in a luxury environment.",

    "shoes":
        "A pair of premium shoes displayed in a luxury environment.",

    "watch":
        "A luxury wristwatch with premium metallic reflections.",

    "perfume":
        "A luxury perfume bottle with elegant cinematic lighting.",

    "phone":
        "A modern premium smartphone with realistic reflections.",

    "clothing":
        "Premium clothing displayed naturally with realistic fabric movement.",

    "bag":
        "A luxury handbag displayed in a premium fashion environment.",

    "food":
        "Delicious gourmet food prepared for a premium commercial.",

    "drink":
        "A refreshing premium beverage with realistic liquid motion.",

    "car":
        "A luxury vehicle in a cinematic advertising scene.",

    "jewelry":
        "Luxury jewelry with sparkling reflections and premium lighting."

}


LANGUAGE_PREFIX = {

    "English": "",

    "French": (
        "The final scene must look like a French commercial advertisement. "
    ),

    "Arabic": (
        "The final scene must look like an Arabic commercial advertisement. "
    )

}


def build_prompt(
    product_type,
    camera,
    language="English",
):

    if product_type not in PRODUCT_PROMPTS:
        product_type = "generic"

    camera_profile = get_camera(camera)

    prefix = LANGUAGE_PREFIX.get(
        language,
        ""
    )

    prompt = (

        prefix

        + PRODUCT_PROMPTS[product_type]

        + " "

        + camera_profile["suffix"]

        + ". "

        + DEFAULT_STYLE

        + "."

    )

    return {

        "positive": prompt,

        "negative": DEFAULT_NEGATIVE_PROMPT,

    }


def build_prompts(
    product_type,
    language="English",
):

    cameras = [

        "orbit",

        "macro",

        "lifestyle",

    ]

    prompts = []

    for camera in cameras:

        p = build_prompt(

            product_type=product_type,

            camera=camera,

            language=language,

        )

        prompts.append({

            "name": camera,

            "positive": p["positive"],

            "negative": p["negative"],

        })

    return prompts
