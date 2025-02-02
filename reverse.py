#!/usr/bin/env python3
import os
import re
import glob

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split("(\d+)", s)]

file_list = glob.glob("*.jpeg")
file_list.sort(key=natural_sort_key, reverse=True)

for i, filename in enumerate(file_list):
    new_name = f"{i:04}.jpeg"
    print(f"Renaming {filename} to {new_name}")
    os.rename(filename, new_name)