import json
from pathlib import Path


def load_json(path):

    path = Path(path)

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data, path):

    path = Path(path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

    return str(path)


def clone_json(data):

    return json.loads(
        json.dumps(data)
    )


def update_node(workflow, node_id, field, value):

    if node_id not in workflow:
        return workflow

    inputs = workflow[node_id].setdefault(
        "inputs",
        {}
    )

    inputs[field] = value

    return workflow


def update_nodes(workflow, updates):

    for node_id, field, value in updates:
        update_node(
            workflow,
            node_id,
            field,
            value
        )

    return workflow


def pretty(data):

    return json.dumps(
        data,
        indent=4,
        ensure_ascii=False
    )
