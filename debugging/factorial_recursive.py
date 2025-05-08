#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        print(factorial(n))
    except IndexError:
        print("Usage: ./factorial.py <non-negative integer>")
    except ValueError as e:
        print(f"Error: {e}")
