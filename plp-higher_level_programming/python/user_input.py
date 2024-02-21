#!/usr/bin/python3
"""Modules prompts for user input then prints
a customized message"""


def greet(name=None, age=None, loc=None):
    """Prints a customized mesage based on user's input
    """
    print(f'Hello {name}, you are {age} years old and live in {loc}.')


if __name__ == "__main__":
    name = input('Enter your name: ')
    age = input('Enter your age: ')
    location = input('Enter your location: ')
    greet(name, age, location)
