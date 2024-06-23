from os.path import join
import os
def filelist(path: str) -> list[str]:
    return [file for file in os.listdir(path) if os.path.isfile(join(path, file))]