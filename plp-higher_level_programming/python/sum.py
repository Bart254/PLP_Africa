#!/usr/bin/python3
""" module accepts user's input and returns the sum of data
passed"""
import sys


def sum(my_list=[]):
    """Prints the sum of data passed
    """
    try:
        sum = 0
        for n in my_list:
            sum += int(n)
        print(sum)
    except Exception:
        print("Usage: ./sum.py numbers")


if __name__ == "__main__":
    numbers = sys.argv[1:]
    sum(numbers)
