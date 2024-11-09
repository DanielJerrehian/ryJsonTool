import os
from uuid import uuid4
from json import dump

from analyze import Analyze
from recursive import walk


def main(directory: os.PathLike, google_folder_name: str, json_file_name: str) -> None:
    files = walk(location=directory)
    dictionaries = []
    scan = Analyze()

    for path in files:
        name = os.path.basename(path)
        mp3 = name.replace(".wav", ".mp3")
        mp3 = name.replace("#", "%23")
        info = {
            "id": uuid4().hex,
            "name": name.split(".")[0],
            "filename": name,
            "source": path,
            "link": f"https://storage.googleapis.com/{google_folder_name}/{mp3}",
            "tags": scan.tags(path=path),
            "type": scan.category(name=name, path=path),
            "artwork": scan.art(name=name),
        }
        if info.get("type") == "loop":
            info["bpm"] = scan.tempo(name=name)
        dictionaries.append(info)

    with open(f"{json_file_name}.json", "w") as file:
        dump(dictionaries, file)


main(
    directory=os.path.join("/", "Volumes", "SSD", "Raveyard - Control Samples"),
    google_folder_name="controlhousesamples",
    json_file_name="operatorLibrary",
)
