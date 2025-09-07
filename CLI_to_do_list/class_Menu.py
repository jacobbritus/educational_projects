from colorama import Fore

from helper_functions import logo, key_color

class Menu:
    def __init__(self, task_list):
        self.selected_key = None
        self.task_list = task_list

        pass

    def display_menu(self, page, task_list):
        box_length = self.task_list.box_length
        option_keys = self.task_list.option_keys

        return_option = ""
        side_characters = 2
        box_length += side_characters # to do list has some extra characters
        top = "┏" + "━" * box_length + "┓"
        def color_option(number):
            return key_color + "[" + option_keys[number] + "]" + Fore.RESET

        option_key_zero = color_option(0)
        option_key_one = color_option(1)
        option_key_two = color_option(2)

        PAGES = {
            "main": {
                "title": "Main Menu",
                "sentences": [
                    "Press an assigned key [ ] to interact."
                ],
                "options": ["New Task", "Settings"]
            },

            "settings": {
                "title": "Settings",
                "return_option": "Back",
                "options": ["Change Keybinds", "Nothing yet..."]
            },

            "edit_keybinds": {
                "title": "Edit Keybinds",
                "sentences": [
                    "Press the assigned key you want to change.",
                    "Press \".\" to cancel."
                ],
                "return_option": " ",
                "options": [" ", " "]
            },
            "change_keybind": {
                "title": "Edit Keybinds",
                "sentences" : [
                    f"Replace [{self.selected_key}] with what?",
                    "Press \".\" to cancel."
                ]

            },
            "selecting": {
                "title": "Selecting Task",
                "return_option": "Back",
                "options": ["Delete", "Mark Task"]
            },
            "adding": {
                "title": "New Task",
                "sentences" : [
                    "Please give this new task a name.",
                    "Press \"Enter\" to cancel."
                ]
        },

            "adding_cap": {
                "title": "New Task",
                "sentences": [
                    "You have reached the maximum amount of tasks.",
                    "Press \"Enter\" to continue."
                ]
            },

            "deleting": {
                "title": "Deleting Task",
                "sentences": [
                    "Are you sure you want to delete this task?"
                ],
                "options": ["Yes", "No"]
            },

        }


        page_content = PAGES[page]

        logo()
        print(top)
        print(f"┃{page_content["title"].center(box_length)}┃")
        print("┣" + "━" * box_length + "┫")

        if page_content.get("sentences"):
            for sentence in page_content["sentences"]:
                print(f"┃{sentence.center(box_length)}┃")


        if page_content.get("options") and not page_content.get("return_option"): print("┃" + " " * box_length + "┃")

        if page_content.get("return_option"):
            print(f"┃ {option_key_zero} {page_content["return_option"].ljust(box_length - 5)}┃")
            if page_content.get("options"): print("┃" + " " * box_length + "┃")
            print(f"┃ {option_key_one} {page_content["options"][0].ljust(box_length - len(page_content["options"][1]) - 11)} {option_key_two} {page_content["options"][1]} ┃")


        if not page_content.get("return_option") and page_content.get("options"):
            print(f"┃ {option_key_zero} {page_content["options"][0].ljust(box_length - (len(page_content["options"][1]) + 11))} {option_key_one} {page_content["options"][1]} ┃")

        if page in ["adding", "adding_cap", "change_keybind"]:
            print("┗" + "━" * box_length + "┛")

        else:
            key_space = check_space = 5
            task_name_space = box_length - (key_space + check_space) - side_characters
            print("┣" + "━" * key_space + "┳" + "━" * task_name_space + "┳" + "━" * check_space + "┫")