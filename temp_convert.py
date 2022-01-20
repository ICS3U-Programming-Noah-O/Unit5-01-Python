#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 18, 2022
# This program allows a user to convert
# a temperature from celsius to farhenheit

import time


def calculate_fahrenheit():
    # Asks questions and gets user input
    print("This program converts temperature in celsius to fahrenheit.")
    print(" ")
    time.sleep(1)
    temp_celsius = (input("Enter the temperature in degress celsius: "))
    print(" ")
    time.sleep(1)

    try:
        # Make sure user input is a float
        temp_celsius_float = float(temp_celsius)
        # Use formula to convert from celsius to fahrenheit
        temp_fahrenheit = (9 / 5) * temp_celsius_float + 32
        print("{} degrees celsius is equivalent ".format(temp_celsius) +
              "to {} degrees fahrenheit".format(temp_fahrenheit))

    except Exception:
        # Prevent crash by displaying error messsage
        print("'{}' is not a number".format(temp_celsius))


def main():
    # Call the function to calculate farenheit
    calculate_fahrenheit()


if __name__ == "__main__":
    main()
