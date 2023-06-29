#!/usr/bin/python3

import sys
import math

def factorize(number):
    factors = []
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append((i, number // i))
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        numbers = file.readlines()

    for number in numbers:
        number = int(number.strip())
        factor_pairs = factorize(number)
        for pair in factor_pairs:
            print(f"{number}={pair[0]}*{pair[1]}")

if __name__ == '__main__':
    main()
