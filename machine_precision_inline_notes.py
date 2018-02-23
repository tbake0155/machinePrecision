#!/usr/bin/env python3

import sys

#This function contains a standard algorithm to find the floating point decimal limit for a machine
#visit https://en.wikipedia.org/wiki/Machine_epsilon for more information
def machinePrecision() :
    a = 4.0 / 3.0
    b = a - 1.0
    c = b + b + b
    precision = abs(c - 1.0) # Value for the machine precision determined by machinePrecision()

    return precision

#This function is the first call when the program is executed
def main() :
    if len(sys.argv) < 2 : # System libray call that allows access to the passed command line arguments
        precision = machinePrecision()
        print(precision)
    else :
        precision = machinePrecision()
        print("Machine precision :", precision)

if __name__ == "__main__":
    main()

