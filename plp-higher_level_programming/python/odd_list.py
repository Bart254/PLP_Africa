#!/usr/bin/python3
"""Module returns a list of words having odd
number length
"""
import sys
try:
    my_list = sys.argv[1:]
    odd_list = [word for word in my_list if len(word) % 2 == 1]
    print(odd_list)
except Exception:
    print('Usage: ./odd_list.py words')
