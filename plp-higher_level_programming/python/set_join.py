#!/usr/bin/python3
"""Joins two sets
"""
try:
    my_odd = input("Enter your odd numbers: ")
    my_prime = input("Enter your prime numbers: ")
    my_odd = my_odd.split(' ')
    my_prime = my_prime.split(' ')
    for i in range(len(my_odd)):
        my_odd[i] = int(my_odd[i])
    for i in range(len(my_prime)):
        my_prime[i] = int(my_prime[i])
    my_odd = set(my_odd)
    my_prime = set(my_prime)
    print(f"The odd numbers that are in your prime numbers are:\
{my_odd.intersection(my_prime)}")
except Exception:
    print("You made an error")
