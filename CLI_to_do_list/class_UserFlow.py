import readchar

from class_ToDoList import ToDoList
from helper_functions import clear_terminal


class UserFlow:
    def __init__(self, menu, task_list):
        self.options = []
        self.menu = menu
        self.task_list = task_list


    @staticmethod
    def get_input():
        return readchar.readkey().upper()
        # return input()

    def main_page(self):
        self.menu.display_menu("main")
        if self.task_list.task_info: self.task_list.display_tasks(None)
        option_key = self.task_list.option_keys

        key = self.get_input()
        options = {option_key[0]: self.adding_tasks,
                   option_key[1]: self.settings}
        clear_terminal()

        # using error handling for user flow
        # input matches one of the menu options
        try:
            options[key]()

        except KeyError:
            # checks if the key is in the task keys and if there is a task assigned to it.
            try:
                if key in self.task_list.task_keys and self.task_list.task_info[self.task_list.task_names[self.task_list.task_keys.index(key)]]:
                    self.selecting_tasks(key)

            # nothing is assigned to the inputted key
            except (IndexError, ValueError):
                pass
                clear_terminal()

    def adding_tasks(self):
        if len(self.task_list.task_names) >= 10:
            self.menu.display_menu("adding_cap")
        else:
            self.menu.display_menu("adding")
        new_task = input("> ")
        clear_terminal()

        if new_task.strip() == "":
            return
        elif len(self.task_list.task_names) >= 10:
            return
        else:
            self.task_list.add_tasks(new_task)


    def settings(self):
        option_key = self.task_list.option_keys

        self.menu.display_menu("settings")
        if self.task_list.task_info: self.task_list.display_tasks(None)

        key = self.get_input()
        clear_terminal()

        if key == option_key[0]:
            return
        elif key == option_key[1]:
            self.changing_keybinds()


        elif key == option_key[2]:
            ...
        else:
            pass

    def changing_keybinds(self):
        while True:
            self.menu.display_menu("edit_keybinds")
            self.task_list.display_tasks("empty")

            key = self.get_input()
            clear_terminal()

            if key == ".":
                clear_terminal()
                return

            # page 2
            elif key in self.task_list.task_keys or key in self.task_list.option_keys:
                self.menu.selected_key = key

                clear_terminal()

                while True:
                    self.menu.display_menu("change_keybind")

                    task_key = self.get_input()
                    print(task_key)

                    if task_key == ".":
                        clear_terminal()
                        break
                    elif not task_key in ["", " ", "\n"] and task_key not in self.task_list.task_keys and task_key not in self.task_list.option_keys:
                        self.task_list.change_keybind(key, task_key)
                        break
                    else:
                        pass
                    clear_terminal()
            else:
                pass
            clear_terminal()



    def selecting_tasks(self, user_input):
        task_key = user_input

        option_key = self.task_list.option_keys
        while True:
            self.menu.display_menu("selecting")
            self.task_list.display_tasks(task_key)

            key = self.get_input()
            clear_terminal()

            if key == option_key[0]:
                return
            elif key == option_key[1]:
                action = self.deleting_task(task_key)
                if action == "delete":
                    self.task_list.remove_tasks(task_key)
                    return

            elif key == option_key[2]:
                self.task_list.mark_tasks(task_key)
            else:
                continue

    def deleting_task(self, key):
        task_key = key
        option_key = self.task_list.option_keys

        options = {option_key[0]: "delete", option_key[1]:"cancel"}
        while True:
            self.menu.display_menu("deleting")
            self.task_list.display_tasks(task_key)

            key = self.get_input()
            clear_terminal()

            try:
                return options[key]
            except KeyError:
                pass
            clear_terminal()