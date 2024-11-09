import pathlib

from tags import tags


class Analyze:
    mapper = {
        "art": {"control": "control.jpg"},
        "tags": [tags],
        "type": {
            "shot": "one-shot",
            "loop": "loop",
        },
    }

    def __init__(self) -> None:
        pass

    def _process_name(self, name: str) -> list:
        return name.lower().split("_")

    def category(self, name: str, path: str) -> str:
        if "loop" in path.lower():
            return Analyze.mapper["type"].get("loop")
        elif "shot" in path.lower():
            return Analyze.mapper["type"].get("shot")
        description = self._process_name(name=name)
        for word in description:
            match = Analyze.mapper["type"].get(word)
            if match:
                return match
            else:
                return Analyze.mapper["type"].get("shot")
        raise Exception

    def tags(self, path: str) -> list:
        parts = list(pathlib.Path(path).parts)
        parts.pop(len(parts) - 1)
        for part in parts:
            if part in Analyze.mapper["tags"]:
                singular = part[:-1]
                parts.extend(singular.split(" "))
        for tag in Analyze.mapper["tags"]:
            if tag in parts:
                parts.remove(tag)
        return parts

    def tempo(self, name: str) -> str:
        description = self._process_name(name=name)
        for word in description:
            if "bpm" in word:
                tempo = word.split("bpm")
                bpm = tempo[0].replace(" ", "")
                try:
                    return int(bpm)
                except:
                    raise Exception

    def art(self, name: str) -> str:
        description = self._process_name(name=name)
        for word in description:
            match = Analyze.mapper["art"].get(word)
            if match:
                return match
