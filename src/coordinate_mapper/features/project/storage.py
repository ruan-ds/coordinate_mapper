import json


def save_project(project: dict, filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(project, f, indent=4, ensure_ascii=False)


def load_project(filename: str) -> dict:
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
