from helper_functions import *

class Menu:
    def __init__(self, task_list):
        self.selected_key = None
        self.task_list = task_list

    def display_menu(self, page) -> None:
        extra_offset = 2
        box_length = self.task_list.box_length + extra_offset
        option_keys = self.task_list.option_keys

        def color_option(number):
            return key_color + "[" + option_keys[number] + "]" + Fore.RESET

        option_key_zero = color_option(0)
        option_key_one = color_option(1)
        option_key_two = color_option(2)

        pages = {
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

        page_content = pages[page]

        print_logo(key_color)
        print(format_box(BoxVariant.TOP, box_length))
        print(format_box(BoxVariant.SIDE, box_length, content = page_content["title"].center(box_length)))
        print(format_box(BoxVariant.C_SIDE, box_length))

        for sentence in page_content.get("sentences", []):
            print(format_box(BoxVariant.SIDE, box_length, content = sentence.center(box_length)))

        return_option_offset = 5

        if page_content.get("return_option"):
            print(format_box(BoxVariant.SIDE,
                             box_length,
                             content = f" {option_key_zero} {page_content["return_option"].ljust(box_length - return_option_offset)}"))

        if page_content.get("options"):
            option1, option2 = page_content["options"]
            print(format_box(BoxVariant.SIDE, box_length))
            print(format_box(BoxVariant.SIDE,
                             box_length,
                             content=f" {option_key_one} {option1.ljust(box_length - (len(option2) + 11))} {option_key_two} {option2} "))

        if page in ["adding", "adding_cap", "change_keybind"] or not self.task_list.task_info:
            print(format_box(BoxVariant.BOTTOM, box_length))


        else:
            print(format_box(BoxVariant.COLUMN_SEPARATOR, box_length))

