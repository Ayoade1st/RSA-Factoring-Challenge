#!/usr/bin/python3
import sys

def factorize(number):
    factors = []
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            factors.append((i, number // i))
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        for line in file:
            number = int(line.strip())
            factorizations = factorize(number)
            for factorization in factorizations:
                print("{}={}*{}".format(number, factorization[0], factorization[1]))

if __name__ == "__main__":
    main()
