import os
import pathlib

from typing import List, Tuple


def counter(path: str, ignore: list = [], ext: list = []) -> List[Tuple]:
    counted_files = []

    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)

            if filepath not in ignore:
                if ext:
                    file_ext = pathlib.Path(filepath).suffix
                    if file_ext not in ext:
                        continue

                with open(filepath, 'r') as reader:
                    file_lines = len(reader.readlines())

                counted_files.append((filepath, file_lines))
    
    return counted_files