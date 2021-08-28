from pathlib import Path
import json

from month.month import Month
from month.x_month import XMonth
from month.month import MDelta

# include meta:
meta_file_name = 'meta.json'
dir_path = Path(__file__).resolve().parent
meta_path = dir_path.joinpath(meta_file_name)

try:
    with open(meta_path) as file:
        meta = json.load(file)
    del file
except FileNotFoundError:
    meta = dict()


def _set_meta(meta_dict):
    attrs = list()
    for attr, value in meta_dict.items():
        globals()[attr] = value
        attrs.append(attr)

    return attrs


__all__ = ['Month', 'XMonth', 'MDelta', *_set_meta(meta_dict=meta)]

del (Path, json, meta_file_name, dir_path, meta_path, meta, _set_meta)
