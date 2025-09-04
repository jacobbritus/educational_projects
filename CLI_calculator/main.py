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

    def get_first_number(self):
        while True:
            user_input = self.get_input()
            if user_input.isdigit():
                self.first_number += user_input
            elif user_input in ["+", "-", "/", "*"] and self.first_number:
                self.arithmetic_expression = user_input
                self.first_number = self.first_number
                self.print_input()
                return
            else:
                self.error_message()

            self.print_input()

    def get_second_number(self):
        while True:
            user_input = self.get_input()
            if user_input.isdigit():
                self.second_number += user_input
            elif user_input in ["=", "\n"] and self.second_number:
                self.second_number = self.second_number
                self.print_input()
                return
            else:
                self.error_message()

            self.print_input()

    def get_arithmetic_expression(self):
        self.arithmetic_expression = self.get_input()


        while self.arithmetic_expression not in ["+", "-", "/", "*"]:

            self.arithmetic_expression = self.get_input()


    def get_result(self):
        a = int(self.first_number) if not "." in self.first_number else float(self.first_number)
        b = int(self.second_number) if not "." in self.second_number else float(self.second_number)

        if self.arithmetic_expression == "+":
            self.result = a + b
        elif self.arithmetic_expression == "-":
            self.result = a - b
        elif self.arithmetic_expression == "*":
            self.result = a * b
        elif self.arithmetic_expression == "/":
            try:
                self.result = round(a / b, 6)
                if str(self.result)[-1] == "0":
                    self.result = int(self.result)
            except ZeroDivisionError:
                self.result = "ERROR"

        else:
            self.result = None

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



        if not self.second_number:
            self.get_second_number()
            self.get_result()


calc = Calculator()
while True:
    calc.run()