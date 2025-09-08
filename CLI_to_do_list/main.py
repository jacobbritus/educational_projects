import time

from class_ToDoList import ToDoList
from class_Menu import Menu
from class_UserFlow import UserFlow
from helper_functions import *

to_do_list = ToDoList()

menu_test = Menu(to_do_list)

user = UserFlow(menu_test, to_do_list)

def opening_animation():
    for i in range(2):
        for color in COLORS:
            print_logo(color)
            time.sleep(0.1)
            clear_terminal()
    clear_terminal()

def main():
    # opening_animation()
    input()
    while True:
        to_do_list.adapt_box_length()
        user.main_page()


main()

