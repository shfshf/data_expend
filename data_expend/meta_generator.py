from pathlib import Path
import collections
import json
from typing import List


def generate_all_part(parts: List[str]):
    prefix = []
    for part in parts:
        yield "_".join(prefix + [part])
        prefix.append(part)


def main(src_dir: str, output_file: str):
    src_dir = Path(src_dir)
    files = src_dir.glob("*.json")

    meta = collections.defaultdict(list)
    for f in files:
        f_name = str(f.relative_to(src_dir))
        parts = f.stem.split("_")

        for k in generate_all_part(parts):
            meta[k].append(f_name)

    with open(output_file, "w") as fd:
        json.dump(dict(meta), fd, ensure_ascii=False)


if __name__ == "__main__":
    assert ["x"] == list(generate_all_part(["x"]))
    assert ["x", "x_y", "x_y_z"] == list(generate_all_part(["x", "y", "z"]))

    src_dir = "./data/dict"
    output_file = "./data/dict/meta.json"
    main(src_dir, output_file)
