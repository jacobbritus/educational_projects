from colorama import Fore

from helper_functions import logo, key_color

class Menu:
    def __init__(self):
        pass

    @staticmethod
    def display_menu(page, task_list):
        box_length = task_list.box_length
        tasks = task_list.task_info
        option_keys = task_list.option_keys

        options = ""
        sentence1 = ""
        sentence2 = ""
        return_option = ""
        side_characters = 2
        box_length += side_characters # to do list has some extra characters
        top = "┏" + "━" * box_length + "┓"
        title = ""
        def color_option(number):
            return key_color + "[" + option_keys[number] + "]" + Fore.RESET

        option_key_zero = color_option(0)
        option_key_one = color_option(1)
        option_key_two = color_option(2)

        if page == "main":
            title = "Main Menu"
            sentence1 = "Press an assigned key [ ] to interact."
            options = ["New task", "Settings"]

        elif page == "settings":
            title = "Settings"
            return_option = "Back"
            options = ["Change Keybinds", "Nothing yet..."]

        if page[0] == "edit keybinds":
            title = "Edit Keybinds"

            if page[1]:

                key = page[2]
                sentence1 = f"Replace [{key}] with what?"
                sentence2 = "Press \".\" to cancel."

            else:
                sentence1 = "Press the assigned key you want to change."
                sentence2 = "Press \".\" to cancel."
                return_option = " "
                options = [" ", " "]

        elif page == "selecting":
            title = "Selecting Task"
            return_option = "Back"
            options = ["Delete", "Mark Task"]



        elif page == "adding":
            title = "New Task"
            if len(task_list.task_names) >= 10:
                sentence1 = "You have reached the maximum amount of tasks."
                sentence2 = "Press \"Enter\" to continue."
            else:
                sentence1 = "Please give this new task a name."
                sentence2 = "Press \"Enter\" to cancel."



        elif page == "deleting":
            title = "Deleting Task"
            sentence1 = "Are you sure you want to delete this task?"
            options = ["Yes", "No"]



        logo()
        print(top)
        print(f"┃{title.center(box_length)}┃")
        print("┣" + "━" * box_length + "┫")
        if sentence1: print(f"┃{sentence1.center(box_length)}┃")
        if sentence2: print(f"┃{sentence2.center(box_length)}┃")
        if options and not return_option: print("┃" + " " * box_length + "┃")
        if return_option:
            print(f"┃ {option_key_zero} {return_option.ljust(box_length - 5)}┃")
            if options: print("┃" + " " * box_length + "┃")
            print(f"┃ {option_key_one} {options[0].ljust(box_length - len(options[1]) - 11)} {option_key_two} {options[1]} ┃")
        if not return_option and options:

            print(f"┃ {option_key_zero} {options[0].ljust(box_length - (len(options[1]) + 11))} {option_key_one} {options[1]} ┃")

        if not tasks or page == "adding" or page[1] == True:
            print("┗" + "━" * box_length + "┛")

        else:
            key_space = check_space = 5
            task_name_space = box_length - (key_space + check_space) - side_characters
            print("┣" + "━" * key_space + "┳" + "━" * task_name_space + "┳" + "━" * check_space + "┫")