from os import listdir, mkdir

if "raw_files" not in listdir():
    mkdir("raw_files")

from PikachuXd.converter.converter import convert

__all__ = ["convert"]
