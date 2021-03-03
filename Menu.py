import os
import re
from time import sleep


class Menu():

    def __init__(self):
        self.progress = 0
        self.zipcode = ''
        self.start = 0
        self.end = 48

    def render(self):
        self.clear()
        self.get_zipcode()
        self.get_start_hour()
        self.get_end_hour()
        self.clear()
        self.progress_bar()

    def clear(self):
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def try_again(self):
        response = None
        invalid = True
        question = "\nMay the odds be with you!\n\nOr you could double check... Would you like to try again? (Y/N):\n\n"

        while invalid:
            response = input(question)

            if response.lower() == "quit":
                self.quit_routine()

            if response.lower() != 'y' and response.lower() != 'n':
                self.invalid_response(
                    "You did not enter a 'Y' or 'N' to indicate yes or no, please try again.")
                continue
            else:
                invalid = False

        if response.lower() == 'y':
            return True
        else:
            return False

    def quit_routine(self):
        self.clear()
        print("You entered the 'quit' command. Exiting the program now.")
        sleep(2)
        quit()

    def invalid_response(self, message):
        self.clear()
        print("[INVALID ENTRY]: " + message)
        sleep(3)
        self.clear()

    def try_parse_int(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    def progress_bar(self):
        qm = "Type 'quit' to exit the program at anytime."
        p0 = "Progress [                              ] 0%"
        p3 = "Progress [##########                    ] 33%"
        p6 = "Progress [####################          ] 66%"
        p1 = "Progress [##############################] 100%"
        sp = "----------------------------------------------"

        if self.progress == 0:
            print(qm)
            print(sp)
            print(p0)
            print(sp + "\n")

        if self.progress == 33:
            print(qm)
            print(sp)
            print(p3)
            print(sp)
            print(f'[ Zip Code: {self.zipcode} ]')
            print(sp + "\n")

        if self.progress == 66:
            print(qm)
            print(sp)
            print(p6)
            print(sp)
            print(f'[ Zip Code: {self.zipcode} | Start: {self.start} ]')
            print(sp + "\n")

        if self.progress == 100:
            print(qm)
            print(sp)
            print(p1)
            print(sp)
            print(
                f'[ Zip Code: {self.zipcode} | Start: {self.start} | End: {self.end} ]')
            print(sp + "\n")

    def get_zipcode(self):
        response = None
        invalid = True
        question = "Where do you want to go for a walk?\nEnter the five digit zip code (US only):\n"

        self.clear()

        while invalid:
            self.progress_bar()
            response = input(question)

            if response.lower() == "quit":
                self.quit_routine()

            if not (re.match(r'\d{5}', response)):
                self.invalid_response(
                    "Your entry did not meet the five digit criteria, please try again.")
                continue
            else:
                self.zipcode = response
                self.progress = 33
                invalid = False

    def get_start_hour(self):
        response = None
        invalid = True
        question = "How many hours from now will your walk window start?\nEnter a digit between 0 (now) and 46:\n"

        self.clear()

        while invalid:
            self.progress_bar()
            response = input(question)

            if response.lower() == "quit":
                self.quit_routine()

            isInt = self.try_parse_int(response)

            if isInt:
                asInt = int(response)

                if asInt < 0 or asInt > 46:
                    self.invalid_response(
                        "You did not enter an integer between 0 and 46.  Please try again.")
                    continue

                if asInt >= 0 and asInt <= 46:
                    self.start = asInt
                    self.progress = 66
                    invalid = False
            else:
                self.invalid_response(
                    "You did not enter an integer.  Please try again.")
                continue

    def get_end_hour(self):
        response = None
        invalid = True
        question = f'How many hours from now will your walk window end?\nEnter a digit between {self.start + 1} (start time + 1 hour) and 47:\n'

        self.clear()

        while invalid:
            self.progress_bar()
            response = input(question)

            if response.lower() == "quit":
                self.quit_routine()

            isInt = self.try_parse_int(response)

            if isInt:
                asInt = int(response)

                if asInt < (self.start + 1) or asInt > 47:
                    self.invalid_response(
                        f"You did not enter an integer between {self.start + 1} and 46.  Please try again.")
                    continue

                if asInt >= (self.start + 1) and asInt <= 47:
                    self.end = asInt
                    self.progress = 100
                    invalid = False
            else:
                self.invalid_response(
                    "You did not enter an integer.  Please try again.")
                continue
