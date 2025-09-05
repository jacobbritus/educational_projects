import time
import readchar
import os

class Calculator:
    def __init__(self):
        self.first_number: str or int or float = ""
        self.arithmetic_expression: str = ""
        self.second_number: str or int or float = ""
        self.result: str or int or float = ""

    @staticmethod
    def clear_terminal() -> None:
        """Clears the terminal whenever the calculator updates."""
        os.system("cls" if os.name == "nt" else "clear")

    def error_message(self) -> None:
        """Shows an error message for a second upon invalid inputs"""
        # this variable is set as self.result is either "" or the actual result.
        current_result_string = self.result
        self.result = "ERROR"
        self.update_display()
        time.sleep(1)
        self.result = current_result_string

    def update_number_input(self, user_input, attr_name) -> bool:
        """Reads the keyboards and updates numbers."""
        current_value = getattr(self, attr_name)

        # === adds numbers and one decimal point ===
        if user_input.isdigit() or self.first_number and user_input == "." and not "." in current_value:
            setattr(self, attr_name, current_value + user_input)
            return True

        # === removes the last input ===
        elif current_value and user_input == readchar.key.BACKSPACE:
            setattr(self, attr_name, current_value[:-1])
            return True

        # === clears current value ===
        elif user_input == "c":
            setattr(self, attr_name, "")
            return True

        else:
            return False

    def get_first_number(self) -> None:
        """Gets the first number."""
        while True:
            user_input = self.get_input()
            is_valid_input = self.update_number_input(user_input, attr_name = "first_number")

            # === move on to the second input ===
            if user_input in ["+", "-", "/", "*"] and self.first_number:
                self.arithmetic_expression = user_input
                self.first_number = self.first_number
                self.update_display()
                return

            # === display error message ===
            elif not is_valid_input:
                self.error_message()

            self.update_display()

    def get_second_number(self) -> None:
        """Gets the second number."""
        while True:
            user_input = self.get_input()
            is_valid_input = self.update_number_input(user_input, "second_number")

            # === move on to the calculation ===
            if user_input in ["=", readchar.key.ENTER] and self.second_number:
                self.update_display()
                return

            # === clear everything ===
            elif user_input == "c":
                self.first_number = self.arithmetic_expression = ""
                return

            # === display error message ===
            elif not is_valid_input:
                self.error_message()

            self.update_display()


    def perform_calculation(self) -> None:
        """Performs the calculation and continuing with the result logic."""

        arithmetic_operations = {
            "+": lambda num1, num2: num1 + num2,
            "-": lambda num1, num2: num1 - num2,
            "*": lambda num1, num2: num1 * num2,
            "/": lambda num1, num2: "ERROR" if num2 == "0" else round(num1 / num2, 2),

        }
        a = int(self.first_number) if not "." in self.first_number else float(self.first_number)
        b = int(self.second_number) if not "." in self.second_number else float(self.second_number)

        self.result = arithmetic_operations[self.arithmetic_expression](a, b)

        # === turns floats with 0 as decimal to integer ===
        if isinstance(self.result, float) and self.result.is_integer():
            self.result = int(self.result)

        self.update_display()

        while True:
            continue_with_result = self.get_input()

            if continue_with_result in ["+", "-", "*", "/", "c"]:
                break
            else:
                self.error_message()
            self.update_display()

        # === continue with result ===
        if continue_with_result in ["+", "-", "*", "/"] and not self.result == "ERROR":
            self.first_number = str(self.result)
            self.arithmetic_expression = continue_with_result

        # === reset calculator ===
        elif continue_with_result == "c":
            self.first_number = ""
            self.arithmetic_expression = ""
        self.second_number = self.result = ""

        self.update_display()

    @staticmethod
    def get_input():
        """Reads the keyboard."""
        return readchar.readkey()

    def update_display(self) -> None:
        """Formats, updates and prints the numbers, arithmetic expressions and result."""
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
        print(self.ascii_art_calculator(display))

    @staticmethod
    def ascii_art_calculator(user_input) -> str:
        """The ASCII calculator art wherein the display gets printed."""
        ascii_art_string = f"""
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
        return (ascii_art_string
        )

    def run(self) -> None:
        """The flow."""
        self.update_display()
        if not self.first_number:
            self.get_first_number()

        self.get_second_number()

        self.perform_calculation()

calc = Calculator()
while True:
    calc.run()


