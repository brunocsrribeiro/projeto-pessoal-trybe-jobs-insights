from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode="r", encoding="utf-8") as file:
        path_csv = csv.DictReader(file, delimiter=",", quotechar='"')
        data_path = []
        for row in path_csv:
            data_path.append(row)
    return data_path
