import copy
from pathlib import Path

from config import DEFAULT_WORKFLOW, WORKFLOW_DIR

from utils.constants import (
    IMAGE_NODE,
    PROMPT_NODE,
    NEGATIVE_PROMPT_NODE,
    WAN_NODE,
    DURATION_NODE,
    FPS_NODE,
    CFG_NODE,
    STEPS_NODE,
    SAMPLER_LOW,
    SAMPLER_HIGH,
)

from utils.json_utils import load_json, save_json
from utils.seeds import generate_seeds


GENERATED_DIR = Path(WORKFLOW_DIR) / "generated"
GENERATED_DIR.mkdir(parents=True, exist_ok=True)


def load_workflow(workflow_name=None):
    if not workflow_name:
        workflow_name = DEFAULT_WORKFLOW

    return load_json(
        Path(WORKFLOW_DIR) / f"{workflow_name}.json"
    )


def apply_settings(
    workflow,
    image_path,
    positive,
    negative,
    width,
    height,
    duration,
    fps,
    cfg,
    steps,
    seed,
):

    wf = copy.deepcopy(workflow)

    wf[IMAGE_NODE]["inputs"]["image"] = image_path

    wf[PROMPT_NODE]["inputs"]["text"] = positive
    wf[NEGATIVE_PROMPT_NODE]["inputs"]["text"] = negative

    wf[WAN_NODE]["inputs"]["width"] = width
    wf[WAN_NODE]["inputs"]["height"] = height

    wf[DURATION_NODE]["inputs"]["value"] = duration
    wf[FPS_NODE]["inputs"]["value"] = fps
    wf[CFG_NODE]["inputs"]["value"] = cfg
    wf[STEPS_NODE]["inputs"]["value"] = steps

    if seed in (-1, None):
        wf[SAMPLER_LOW]["inputs"]["noise_seed"] = -1
        wf[SAMPLER_HIGH]["inputs"]["noise_seed"] = -1
    else:
        wf[SAMPLER_LOW]["inputs"]["noise_seed"] = seed
        wf[SAMPLER_HIGH]["inputs"]["noise_seed"] = seed + 1

    return wf


def process_jobs(
    image_path,
    angles,
    workflow_name=None,
    width=832,
    height=480,
    duration=5,
    fps=16,
    cfg=3.5,
    steps=20,
    seed=None,
):

    template = load_workflow(workflow_name)

    seeds = generate_seeds(
        len(angles),
        seed,
    )

    jobs = []

    for index, angle in enumerate(angles):

        workflow = apply_settings(
            template,
            image_path=image_path,
            positive=angle["positive"],
            negative=angle["negative"],
            width=width,
            height=height,
            duration=duration,
            fps=fps,
            cfg=cfg,
            steps=steps,
            seed=seeds[index],
        )

        output_file = GENERATED_DIR / f'{angle["name"]}.json'

        save_json(
            workflow,
            output_file,
        )

        jobs.append(
            {
                "name": angle["name"],
                "workflow": workflow,
                "workflow_path": str(output_file),
                "seed": seeds[index],
            }
        )

    return jobs
