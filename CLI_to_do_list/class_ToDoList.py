import random

from helper_functions import *


class ToDoList:
    def __init__(self, box_length = 50):
        self.task_info, self.task_keys, self.option_keys = load_file()
        self.task_names = [task for task in self.task_info]


        # display
        self.box_length = box_length
        self.key_space = 5
        self.check_space = 5
        self.task_space = box_length - (self.key_space + self.check_space)

    def display_tasks(self, key) -> None:
        """Prints out the task list."""
        display_format = "┃{key}┃{task}┃{status}┃"

        print(display_format.format(key="Key".center(self.key_space),
                                               task="Task".center(self.task_space),
                                               status="Check".center(self.check_space)))

        # === prints empty tasks and their keybinds when changing keybinds ===
        if key == "edit_keybinds":
            for i in range(TASK_PAGE_CAP):
                keybind = KEY_COLOR + "[" + self.task_keys[i] + "]" + Fore.RESET
                key_center = self.key_space + 10 # handles invisible color codes

                print(format_box(BoxVariant.C_SIDE, self.box_length, row="╋", extra_offset = 0))

                print(display_format.format(key=keybind.center(key_center),
                                            task=" ".center(self.task_space),
                                            status=" ".center(self.check_space)))

            print(format_box(BoxVariant.BOTTOM, self.box_length, row="┻", extra_offset=0))
            return

        # === prints created tasks ===
        for index, task in enumerate(self.task_info):
            keybind = KEY_COLOR + "[" + self.task_keys[index] + "]" + Fore.RESET
            status = self.task_info[task]["status"]
            key_center = self.key_space + 10 # handles invisible color codes
            status_center = self.check_space + 10 if len(status) > 3 else self.check_space # handles invisible color codes

            # === prints only the selected task ===
            if key:
                if index == self.task_keys.index(key):
                    print(format_box(BoxVariant.C_SIDE, self.box_length, row="╋", extra_offset=0))
                    print(display_format.format(key = keybind.center(key_center),
                                                           task = task.center(self.task_space),
                                                           status = status.center(status_center)))
                    break
                else:
                    pass

            # === prints all the tasks ===
            else:
                print(format_box(BoxVariant.C_SIDE, self.box_length, row="╋", extra_offset= 0))
                print(display_format.format(key=keybind.center(key_center),
                                                       task=task.center(self.task_space),
                                                       status=status.center(status_center)))

        print(format_box(BoxVariant.BOTTOM, self.box_length, row="┻", extra_offset=0))

    def adapt_box_length(self) -> None:
        """Scales the display box length dynamically if a newly inputted task name doesn't fit the UI"""
        for task in list(self.task_info.keys()):
            if len(task) > self.task_space:
                self.box_length += len(task) - self.task_space
                self.task_space += len(task) - self.task_space

    def remove_tasks(self, key):
        """ Removes the task passed as a parameter and saves the change."""
        task_keys = list(self.task_info.keys())
        task = task_keys[self.task_keys.index(key)]

        del self.task_info[task]
        self.task_names = [task for task in self.task_info]
        save_file((self.task_info, self.task_keys, self.option_keys))

    def add_tasks(self, task_name):
        self.task_info.update({task_name: {"status": "[ ]"}})
        self.task_names = [task for task in self.task_info]
        save_file((self.task_info, self.task_keys, self.option_keys))

    def mark_tasks(self, key):
        task = self.task_names[self.task_keys.index(key)]

        if not self.task_info[task]["status"] == Fore.GREEN + "[x]" + Fore.RESET:
            self.task_info[task]["status"] = Fore.GREEN + "[x]" + Fore.RESET
        else:
            self.task_info[task]["status"] = "[ ]"
        save_file((self.task_info, self.task_keys, self.option_keys))

    def change_keybind(self, old_key, new_key):
        if old_key in self.task_keys:
            key_index = self.task_keys.index(old_key)
            self.task_keys.insert(key_index, new_key)
            self.task_keys.remove(old_key)

        if old_key in self.option_keys:
            key_index = self.option_keys.index(old_key)
            self.option_keys.insert(key_index, new_key)
            self.option_keys.remove(old_key)

        save_file((self.task_info, self.task_keys, self.option_keys))


