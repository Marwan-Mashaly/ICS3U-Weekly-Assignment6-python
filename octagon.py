#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program tells user the month afte typing the number

import math


def area_octagon(side):
    # This function calculates the area of the octagon

    area = (2 * (1 + (math.sqrt(2))) * side * side)
    return area


def main():
    # This function takes input from user and calls other functions

    while True:
        side = input("Enter the side of the octagon (cm): ")
        print("")
        try:
            side_check = int(side)
            final_answer = area_octagon(side_check)
            print("the solution is : {0:.2f} (cm^2)".format(final_answer))
            print("")
        except Exception:
            print("Invalid Integer ")
            print("")


if __name__ == "__main__":
    main()
