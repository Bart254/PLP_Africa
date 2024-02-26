#!/usr/bin/python3
"""A Module for list methods
"""
my_list = []
for n in [10, 20, 30, 40]:
    my_list.append(n)
my_list[1] = 15
my_list.extend([50, 60, 70])
my_list.pop()
my_list.sort()
print(my_list.index(30))
