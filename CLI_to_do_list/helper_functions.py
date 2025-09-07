import os
import json
from colorama import Fore

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE]
key_color = Fore.MAGENTA

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    print("\033c\033[3J")

def logo():
    print(key_color + r"""   ▁▁             ▁▁      ▁▁▁
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





