import os
import pathlib

from typing import List, Tuple


def count_directory(path: str, ignore: list = [], ext: list = []) -> List[Tuple[str]]:
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

                counted_files.append((filepath, str(file_lines)))
    
    return counted_files


def count_file(path: str) -> List[Tuple[str]]:
    with open(path, 'r') as reader:
        file_lines = len(reader.readlines())
    
    return [(path, str(file_lines))]
