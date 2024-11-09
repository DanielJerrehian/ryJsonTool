import os


def walk(location) -> list:
    if not os.path.exists(location):
        raise Exception

    output = []
    for root, directories, files in os.walk(location):
        for name in files:
            if name.endswith(".wav"):
                absolute = os.path.join(root, name)
                relative = os.path.relpath(absolute, location)
                output.append(relative)
    return output
