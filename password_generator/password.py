# Made by TH1RDKEYBLADE
# Password.py

# Files
from characters import *

# Built-in Modules
from datetime import datetime as dt
from os import path
from random import shuffle
from sys import exit

# Installed Modules
from pyclip import copy
from termcolor import cprint

# Password Class
class Password():
    def __init__(self, amount_lower, amount_upper, amount_special, amount_numbers, password, password_length, file_name):
        super().__init__()
        self.amount_lower = amount_lower
        self.amount_upper = amount_upper
        self.amount_special = amount_special
        self.amount_numbers = amount_numbers

        self.password = password
        self.password_length = password_length

        self.file_name = file_name

    # User password character amount customization
    def get_char_amount(self):
        while True:
            self.password = []

            cprint("\nStart", "blue")
            cprint("---------", "white", attrs=["bold"])

            # User Input
            try:
                self.amount_lower = int(input("Enter the amount of lower case letters you'd like: "))
                self.amount_upper = int(input("Enter the amount of upper case letters you'd like: "))
                self.amount_special = int(input("Enter the amount of special characters you'd like: "))
                self.amount_numbers = int(input("Enter the amount of numbers you'd like: "))

                # If the input is less than 0 sets it to zero so Password Length adds correctly
                if self.amount_lower < 0:
                    self.amount_lower = 0
                if self.amount_upper < 0:
                    self.amount_upper = 0
                if self.amount_special < 0:
                    self.amount_special = 0
                if self.amount_numbers < 0:
                    self.amount_numbers = 0

                self.password_length = (self.amount_lower + self.amount_upper + self.amount_special + self.amount_numbers)
                cprint(f"\nYour Password Length is {self.password_length} characters.", "green")

                length_confirmation = input("Would you like to continue? Type: [y/n]").lower()
                if length_confirmation == "n" or length_confirmation == "no":
                    continue
                else:
                    pass
            except ValueError:
                cprint("You must enter a Integer in all of the inputs, try again.\n\n", "red")
                continue
            break

    # Ends program if the user types in num <= 0
    def no_character_detection(self):
        if self.amount_lower <= 0 and self.amount_upper <= 0 and self.amount_special <= 0 and self.amount_numbers <= 0:
            cprint("You've chosen that you do not want a password.\n\n", "red")
            exit()
            
    # File name for Organization Purposes
    def get_file_name(self):
        cprint("\nFile Name", "blue")
        cprint("---------", "white", attrs=["bold"])

        self.file_name = str(input("Now enter the name of this password for organization purposes: ")).capitalize()
        if self.file_name == "" or self.file_name == " ":
            cprint("You've entered no name for your password.", "red")

    # Gets a random Lower Case letter [i] amount of times
    def get_amount_lower(self):
        if self.amount_lower <= 0:
            cprint("You're not using lower case characters in your password.", "red")
        else:
            for i in range(1, self.amount_lower+1):
                shuffle(list_lower_case)
                self.password += list_lower_case[0]

    # Gets a random Upper Case letter [j] amount of times
    def get_amount_upper(self):
        if self.amount_upper <= 0:
            cprint("You're not using UPPER case characters in your password.", "red")
        else:
            for j in range(1, self.amount_upper+1):
                shuffle(list_upper_case)
                self.password += list_upper_case[0]

    # Gets a random Special Character [k] amount of times
    def get_amount_special(self):
        if self.amount_special <= 0:
            cprint("You're not using Special(!*) chracters in your password.", "red")
        else:
            for k in range(1, self.amount_special+1):
                shuffle(list_special_char)
                self.password += list_special_char[0]

    # Gets a random Number [l] amount of times
    def get_amount_numbers(self):
        if self.amount_numbers <= 0:
            cprint("You're not using numbers in your password.", "red")
        else:
            for l in range(1, self.amount_numbers+1):
                shuffle(list_numbers)
                self.password += list_numbers[0]

    # Creates a random password by shuffling all randomized characters
    def get_random_password(self):
        shuffle(self.password)
        self.password = "".join(self.password)

        cprint("\nPassword:", "green")
        cprint(f"{self.password}", "magenta")

        redo = input("Would you like to re-shuffle your password? Type: [y/n]").lower()
        if redo == "y" or redo == "yes":
            self.password = list(self.password)
            shuffle(self.password)
            self.password = "".join(self.password)
        else:
            pass

        copy(self.password)
        cprint("\nPassword copied to clipboard & wrote to Password file (in same directory):", "green")
        cprint(f"{self.password}", "magenta")

    # Writes Password to File in the same directory
    def write_password_file(self):
        time = dt.now()   
        time = time.strftime("%Y-%m-%d  %H:%M:%S")

        # If the user has passwords.txt in the same directory
        try:
            if path.exists("Passwords.txt"):
                with open("Passwords.txt", "a") as f:
                    f.write(f"\n\nDate & Time of Password Creation: {time}\n -{self.file_name} password: {self.password} | Length: {self.password_length}")
        except PermissionError:
            cprint("\nPermission Error", "red")
            print("You're password was not written to a Password File: [Permission Denied]")

        # If the user doesn't have passwords.txt in the same directory
        try:
            if not(path.exists("Passwords.txt")):
                with open("Passwords.txt", "w") as f1:
                    f1.write(f"Date & Time of Password Creation: {time}\n -{self.file_name} password: {self.password} | Length: {self.password_length}")
        except PermissionError:
            cprint("\nPermission Error", "red")
            print("You're password was not written to a Password File: [Permission Denied]")
