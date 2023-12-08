#!/usr/bin/env python3
# Script:                       Op Challenge 9
# Author:                       Andrew Carroll
# Date of latest revision:      12/7/2023
# Purpose:                      Python Conditionals

# Assign values to variables a and b
a = 10
b = 5

# Check if a is equal to b
if a == b:
    print("a is equal to b")

# Check if a is not equal to b
elif a != b:
    print("a is not equal to b")

# Check if a is greater than b
if a > b:
    print("a is greater than b")

# Check if a is less than or equal to b
elif a <= b:
    print("a is less than or equal to b")

# Check if both conditions are met using 'and'
if a > 5 and b < 7:
    print("Both conditions are met (a > 5 and b < 7)")

# Check if either condition is met using 'or'
if a > 15 or b < 3:
    print("Either condition is met (a > 15 or b < 3)")

# Nested if statement
if a > 8:
    print("a is greater than 8")
    if b < 3:
        print("b is less than 3")

# Create an if statement with pass
if a < 3:
    pass
else:
    print("a is not less than 3")
