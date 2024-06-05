"""
The code in this file is given to you.
Run this file to call the functions in solutions.py in a way that makes sense.
Feel free to comment out any of it in order to focus only on the functions you are currently working on.
"""

from solutions import *


def main():
    
    # make use of the functions in solutions.py

    # print out a friendly welcome
    print("\n--- WELCOME! ---\n")

    # print out the current year
    year = get_year()
    print("\nThe current year is {}!".format(year))

    # check whether a shape is square or not
    print()  # line break
    if is_square():
        print("Yes - this object is square!")
    else:
        print("Sorry... this object is not square.")

    # print out the greatest of two numbers
    
    print()  # line break
    greatest = get_greatest()
    print("The largest of the two numbers is {}.".format(greatest))

    # print out a person's BMI statistical category
    print()  # line break!
    bmi_category = get_bmi_category()
    print("Your BMI stastical category is {}.".format(bmi_category))

    # print out the total cost of a face masks purchase
    print()  # line break!
    total = get_discount()
    print("The total cost of your face masks is: {}.".format(total))

    # print out whether it's currently a leap year
    print()
    this_year = get_year()
    if is_leap_year():
        print("{} is a leap year!!!!".format(this_year))
    else:
        print("Sorry.... {} is not a leap year.".format(this_year))

    # print out a farewell message
    print()
    print("--- BYE BYE! ---")


# call the main function
main()

