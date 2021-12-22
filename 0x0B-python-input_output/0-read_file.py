#!/usr/bin/python3

def read_file(file_name=""):
    with open(file_name, "r", encoding="UTF-8") as f:
        print(f.read(), end="")