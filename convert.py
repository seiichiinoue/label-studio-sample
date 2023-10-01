import os
import json
from collections import defaultdict

INDEX_KEY = "index"
INPUT_KEY = "input"
OUTPUT_KEY = "output"
ANNOTATION_KEY = "annotation"

def set_annotation_as_output(data: list) -> list:
    """
    qloraで使われるoutput keyにannotation結果を格納
    """
    for instance in data:
        instance[OUTPUT_KEY] = instance[ANNOTATION_KEY]
        instance.pop(ANNOTATION_KEY)
    return data

def remove_duplicated_instance(data: list) -> list:
    """
    複数人がアノテーションする場合、データの重複が起こる
    同じデータに対して複数人がannotationした場合、最新のものを採用する
    """
    index2annotation_ids = defaultdict(list)
    for instance in data:
        index2annotation_ids[instance["index"]].append(instance["annotation_id"])
    for k, v in index2annotation_ids.items():
        v.sort(reverse=True)
    data_new = []
    for instance in data:
        head_id = index2annotation_ids[instance["index"]][0]
        if instance["annotation_id"] != head_id:
            continue
        data_new.append(instance)
    return data_new
        
def load_data(path: str) -> list:
    if not os.path.exists(path):
        raise ValueError(f"Error loading dataset: {path}")
    else:
        return json.load(open(path))

def convert(path: str) -> None:
    data = load_data()


if __name__ == "__main__":
    path = "data/project-2-at-2023-10-01-12-40-3fd2fd59.json"
    data = load_data(path=path)
    ret = set_annotation_as_output(data=data)
    ret = remove_duplicated_instance(data=data)
    with open(path.replace(".json", "") + "-proc.json", "w") as f:
        json.dump(ret, f, indent=2, ensure_ascii=False)
    