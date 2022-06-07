#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created June 2022
# This program generates two arrays and finds the average.

import random


def find_average(num_array):
    # this function finds the average of num_array

    total = 0
    num_quantity = 0

    for counter_array in num_array:
        for single_num in counter_array:
            total += single_num
            num_quantity += 1

    average = total / num_quantity

    return average


def main():
    # this function generates a row/column array, calls a function to
    # calculate average, then outputs the average

    num_array = []

    print("This program calculates the average of a 2D array.\n")

    # input
    try:
        rows = int(input("Enter the number of rows you would like: "))
        columns = int(input("Enter the number of columns you would like: "))
        print("")

        if rows <= 0 or columns <= 0:
            0 / 0  # causes crash if negative or zero, skipping to except

        # process & output
        for counter_rows in range(0, rows):
            temp_array = []
            for counter_columns in range(0, columns):
                random_num = random.randint(0, 50)
                temp_array.append(random_num)
                print("{} ".format(random_num), end="")
            num_array.append(temp_array)
            print("")

        # call function
        average = find_average(num_array)

        # output
        print("\nThe average of all numbers is {0:.2f}.".format(average))

    except Exception:
        print("Your rows/columns are invalid. Please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
