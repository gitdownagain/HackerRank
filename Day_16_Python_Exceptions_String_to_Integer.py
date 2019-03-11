#!/bin/python3

import sys

def convert_to_int(data):
    try:
        data = int(data)
        print(data)
    except:
        print("Bad String")
    return data

S = input().strip()

convert_to_int(S)

# Task 
# Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.

#Note: You must use the String-to-Integer and exception handling constructs built into your submission language. 
# If you attempt to use loops/conditional statements, you will get a  score.
