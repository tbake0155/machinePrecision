#!/usr/bin/env python3

import sys

def machinePrecision() :
    a = 4.0 / 3.0
    b = a - 1.0
    c = b + b + b
    precision = abs(c - 1.0)

    return precision

def main() :
    if len(sys.argv) < 2 :
        precision = machinePrecision()
        print(precision)
    else :
        precision = machinePrecision()
        print("Machine precision :", precision)

if __name__ == "__main__":
    main()

