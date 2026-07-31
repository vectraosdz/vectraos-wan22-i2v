import random
import time


def random_seed():

    return random.randint(
        1,
        2**63 - 1
    )


def generate_seeds(count, base_seed=None):

    if base_seed is None:

        random.seed(time.time_ns())

        return [
            random_seed()
            for _ in range(count)
        ]

    return [
        int(base_seed) + i
        for i in range(count)
    ]


def unique_seed(existing):

    while True:

        seed = random_seed()

        if seed not in existing:

            return seed
