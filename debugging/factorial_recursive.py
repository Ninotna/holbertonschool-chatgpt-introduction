#!/usr/bin/python3
import sys

# Function to calculate the factorial of a given number using recursion
# @param n: an integer representing the number for which the factorial is to be calculated
# @return: the factorial of the given number n; returns 1 if n is 0, otherwise n * factorial(n-1)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate the factorial of the number passed as the first argument from the command line
f = factorial(int(sys.argv[1]))

# Print the calculated factorial value
print(f)
