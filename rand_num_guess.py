#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Oct 18, 2023
# This program will ask the user
# for a number and will tell them
# if they guessed correctly using random number

import random


def main():
    # Get the user guess
    print("This program will ask the user for a number between 1 and 10")
    print("then it will display if they guessed correctly or not.")

    user_guess = int(input("Please enter your guess between 1 and 10: "))

    # create generator for correct_guess
    correct_guess = random.randint(1, 10)

    # Check if the user guess is equal to correct guess

    if user_guess == (correct_guess):
        # Display if the user is right

        print("\nCongratulations, you guessed correctly!")
    else:
        # Display if the user is wrong

        print("\nPlease guess again, the correct number was {}".format(correct_guess))


if __name__ == "__main__":
    main()
