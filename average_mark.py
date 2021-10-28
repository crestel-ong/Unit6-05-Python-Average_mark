#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Oct 2021
# this program calculates the average mark
# this program uses lists


def calculate_average(list_of_marks):
    # this function averges the marks
    # declare
    average = 0
    single_mark = 0
    total = 0

    for single_mark in list_of_marks:
        # this gets the total of all the marks
        total = total + single_mark
    # this gets the average the len part is finding the # of items in the list
    average = total / len(list_of_marks)
    # this rounds the average
    average = round(average, 2)

    return average


def main():
    # this program aceppts marks from user (ints) and calulates the average
    # if a -1 is entered it ends the list

    marks_list = []
    inputted_mark = 0

    # tell the user what to do
    print("This program calculates the average of inputted marks.")
    print("Please enter 1 mark at a time. Enter -1 to end. ")
    print("The marks must be from 0 to 100.")
    print("")

    while True:
        inputted_mark_as_string = input("What is the mark? (as %): ")
        try:
            # convert string to integer
            inputted_mark = int(inputted_mark_as_string)
            if inputted_mark >= 1 and inputted_mark <= 100:
                marks_list.append(inputted_mark)

            elif inputted_mark == -1:
                break
            else:
                print("Invalid input, that won't be", end="")
                print(" inculded in calculating the average.")

        except Exception:
            print("Invalid input, that won't be included", end="")
            print(" in calculating the average.")

    # call function
    returned_average = calculate_average(marks_list)

    print("\nThe average is {0}%".format(returned_average))

    print("\nDone.")


if __name__ == "__main__":
    main()
