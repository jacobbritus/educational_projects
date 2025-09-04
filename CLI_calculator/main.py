import time
import readchar
import os

class Calculator:
    def __init__(self):
        self.first_number = ""
        self.arithmetic_expression = ""
        self.second_number = ""
        self.result = ""

    @staticmethod
    def clear_terminal():
        os.system("cls" if os.name == "nt" else "clear")

    def error_message(self):
        result_pre = self.result
        self.result = "ERROR"
        self.print_input()
        time.sleep(1)
        self.result = result_pre

    def update_number_input(self, user_input, attr_name):
        num = getattr(self, attr_name)

        if user_input.isdigit() or self.first_number and user_input == "." and not "." in num:
            setattr(self, attr_name, num + user_input)
            return True
        elif num and user_input == readchar.key.BACKSPACE:
            setattr(self, attr_name, num[:-1])
            return True
        elif user_input == "c":
            setattr(self, attr_name, "")
            return True
        else:
            return False

    def get_first_number(self):
        while True:
            user_input = self.get_input()
            valid = self.update_number_input(user_input, attr_name = "first_number")
            if user_input in ["+", "-", "/", "*"] and self.first_number:
                self.arithmetic_expression = user_input
                self.first_number = self.first_number
                self.print_input()
                return
            elif not valid:
                self.error_message()

            self.print_input()

    def get_second_number(self):
        while True:
            user_input = self.get_input()
            valid = self.update_number_input(user_input, "second_number")
            if user_input in ["=", readchar.key.ENTER] and self.second_number:
                self.second_number = self.second_number
                self.print_input()
                return
            elif user_input == "c":
                self.first_number = self.arithmetic_expression = ""
                return
            elif not valid:
                self.error_message()

            self.print_input()


    def get_result(self):
        arithmetic_operations = {
            "+": lambda num1, num2: num1 + num2,
            "-": lambda num1, num2: num1 - num2,
            "*": lambda num1, num2: num1 * num2,
            "/": lambda num1, num2: "ERROR" if num2 == "0" else round(num1 / num2, 10),

        }
        a = int(self.first_number) if not "." in self.first_number else float(self.first_number)
        b = int(self.second_number) if not "." in self.second_number else float(self.second_number)

        self.result = arithmetic_operations[self.arithmetic_expression](a, b)

        if str(self.result)[-1] == "0":
            self.result = int(self.result)

        self.print_input()



        while True:
            continue_with_result = self.get_input()

            if continue_with_result in ["+", "-", "*", "/", "c"]:
                break
            else:
                self.error_message()
            self.print_input()


        if continue_with_result in ["+", "-", "*", "/"] and not self.result == "ERROR":
            self.first_number = str(self.result)
            self.arithmetic_expression = continue_with_result


        elif continue_with_result == "c":
            self.first_number = ""
            self.arithmetic_expression = ""
        self.second_number = self.result = ""

        self.print_input()

    @staticmethod
    def get_input():
        return readchar.readkey()

    def print_input(self):
        self.clear_terminal()
        if self.result or self.result == 0:
            display = f"{self.result}"

        elif self.second_number:
            display = f"{self.first_number} {self.arithmetic_expression} {self.second_number}"

        elif self.arithmetic_expression:
            display = f"{self.first_number} {self.arithmetic_expression}"

        elif self.first_number:
            display = f"{self.first_number}"
        else:
            display = ""
        print(self.ascii_art(display))


    def ascii_art(self, user_input):
        calc = f"""
     _____________________
    |  _________________  |
    | | {user_input.center(15) } | |
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
    """
        return (calc
        )

    def run(self):
        self.print_input()
        if not self.first_number:
            self.get_first_number()

        elif not self.second_number:
            self.get_second_number()

        elif self.second_number:
            self.get_result()


calc = Calculator()
while True:
    calc.run()