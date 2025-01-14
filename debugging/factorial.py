#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) < 2:
    print("Usage: {} <number>".format(sys.argv[0]))
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        sys.exit(1)
    f = factorial(n)
    print(f)
except ValueError:
    print("Error: The argument must be an interger.")
    sys.exit(1)