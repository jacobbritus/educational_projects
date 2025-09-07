import os
import json
from colorama import Fore
from enum import Enum, auto



colors = [
    Fore.RED,
    Fore.LIGHTRED_EX,
    Fore.YELLOW,
    Fore.LIGHTYELLOW_EX,
    Fore.GREEN,
    Fore.LIGHTGREEN_EX,
    Fore.CYAN,
    Fore.LIGHTCYAN_EX,
    Fore.BLUE,
    Fore.LIGHTBLUE_EX,
    Fore.MAGENTA,
    Fore.LIGHTMAGENTA_EX,
    Fore.WHITE,
    Fore.LIGHTWHITE_EX,
    Fore.BLACK,
    Fore.LIGHTBLACK_EX,
]
key_color = Fore.MAGENTA

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    print("\033c\033[3J")

def print_logo(color):
    print(color + r"""   ▁▁             ▁▁      ▁▁▁
  ╱ ╱▁▁▁▁▁  ▁▁▁▁▁╱ ╱▁▁▁▁▁╱  ╱
 ╱ ▁▁╱ ▁▁ ╲╱ ▁▁▁╱ ╱╱▁╱ ▁▁  ╱ 
╱ ╱▁╱ ╱▁╱ (▁▁  ) ,< ╱ ╱_╱ ╱  
\▁▁╱╲▁▁,▁╱▁▁▁▁╱▁╱│▁│╲▁▁,▁╱ """ + Fore.RESET)


FILE_NAME = "save_file"
def save_file(info):
    with open(FILE_NAME, encoding = "utf-8", mode = "w") as f:
        json.dump(info, f)

def load_file():
    try:
        with open(FILE_NAME, encoding = "utf-8", mode = "r") as f:
            return json.load(f)
    except (FileNotFoundError, ValueError):
        return {}, ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"], ["Z", "X", "C"]


def format_box(variant, box_length = 50, **kwargs):
    sides = variant.value
    content = kwargs.get("content")
    whitespace = kwargs.get("whitespace")

    if variant.name in [BoxVariant.COLUMN_SEPARATOR, BoxVariant.BOTTOM_CLOSER]:
        print(variant)
        extra_offset = 2
        key_space = check_space = 5
        task_name_space = box_length - (key_space + check_space) - extra_offset

        return sides[0] + "━" * key_space + "┳" + "━" * task_name_space + "┳" + "━" * check_space + sides[1]

    if content:
        return f"{sides[0]}{content}{sides[1]}"

    seperator = "━" if not whitespace else " "
    return sides[0] + seperator * box_length + sides[1]


class BoxVariant(Enum):
    COLUMN_SEPARATOR = ["┣", "┫"]
    BOTTOM_CLOSER = ["┗", "┛"]
    TOP =    ["┏", "┓"]
    SIDE =   ["┃", "┃"]
    C_SIDE = ["┣", "┫"]
    BOTTOM = ["┗", "┛"]