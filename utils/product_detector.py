import re


PRODUCT_KEYWORDS = {

    "shoes": [
        "shoe",
        "shoes",
        "sneaker",
        "sneakers",
        "boot",
        "boots",
        "running shoe",
        "basket",
        "nike",
        "adidas",
        "puma"
    ],

    "watch": [
        "watch",
        "smartwatch",
        "rolex",
        "omega",
        "casio",
        "apple watch"
    ],

    "perfume": [
        "perfume",
        "fragrance",
        "parfum",
        "cologne",
        "eau de parfum"
    ],

    "phone": [
        "phone",
        "iphone",
        "smartphone",
        "mobile",
        "android",
        "samsung",
        "xiaomi",
        "huawei"
    ],

    "clothing": [
        "shirt",
        "tshirt",
        "t-shirt",
        "hoodie",
        "jacket",
        "coat",
        "dress",
        "pants",
        "jeans",
        "clothes"
    ],

    "bag": [
        "bag",
        "backpack",
        "handbag",
        "wallet",
        "purse"
    ],

    "food": [
        "pizza",
        "burger",
        "cake",
        "bread",
        "cookie",
        "food",
        "meal",
        "sandwich",
        "dessert"
    ],

    "drink": [
        "coffee",
        "tea",
        "juice",
        "drink",
        "cola",
        "water",
        "soda"
    ],

    "car": [
        "car",
        "vehicle",
        "automobile",
        "bmw",
        "mercedes",
        "audi",
        "tesla"
    ],

    "jewelry": [
        "ring",
        "necklace",
        "bracelet",
        "gold",
        "silver",
        "diamond",
        "jewelry"
    ]

}


def normalize(text):

    if text is None:
        return ""

    text = str(text).lower()

    text = re.sub(r"[^a-z0-9 ]+", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def detect_product(text):

    text = normalize(text)

    for category, keywords in PRODUCT_KEYWORDS.items():

        for keyword in keywords:

            if keyword in text:

                return category

    return "generic"


def detect_from_metadata(job_input):

    fields = [

        job_input.get("product"),

        job_input.get("product_type"),

        job_input.get("title"),

        job_input.get("name"),

        job_input.get("description"),

        job_input.get("prompt")

    ]

    for value in fields:

        category = detect_product(value)

        if category != "generic":

            return category

    return "generic"


def get_category(job_input):

    if "product_type" in job_input:

        value = normalize(job_input["product_type"])

        if value in PRODUCT_KEYWORDS:

            return value

    return detect_from_metadata(job_input)
