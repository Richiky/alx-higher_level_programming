#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10  # Using modulo (%) operator to get the last digit
    print("The last digit of", number, "is:", last_digit)
    return last_digit

# Example usage:
number = 12345
last_digit = print_last_digit(number)
