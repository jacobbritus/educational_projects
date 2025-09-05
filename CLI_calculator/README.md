CLI calculator

This is the first project I decided to create for this repository.

It differentiates from common CLI calculators by including ASCII art and the readchar module which reads keyboard input.

It currently only allows for addition, subtraction, multiplication and division.

I really like the error message method, the calculator feels like a real one now.

The most important lesson:

    arithmetic_operations = {
            "+": lambda num1, num2: num1 + num2,
            "-": lambda num1, num2: num1 - num2,
            "*": lambda num1, num2: num1 * num2,
            "/": lambda num1, num2: "ERROR" if num2 == "0" else round(num1 / num2, 10)
        }

Before, I used a list of conditionals. This avoids unnecessary code length and allows for scalability.