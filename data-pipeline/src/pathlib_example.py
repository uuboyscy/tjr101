from pathlib import Path

PARENT_FOLDER = "../res_gossiping/"

for path in Path(PARENT_FOLDER).glob("*.txt"):
    with path.open("r") as f:
        print(f.read())
