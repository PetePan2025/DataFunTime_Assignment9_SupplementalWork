# File Name : teamMember02.py
# Student Name: Nathan Sharpe
# email: sharpenn@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/16/25
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Complete an incomplete module that processes data from a dataset and produces an interesting output.
# Brief Description of what this module does: Familiarizes us with working with datasets and extracting insights from them
# Citations: https://blog.finxter.com/5-best-ways-to-calculate-element-frequencies-in-percent-range-using-python/
# Anything else that's relevant:

class teamMember02:
    """
    Analyzes a list of dictionaries pulled from a csv containing car data and extracts the percentages of each transmission type.
    """
    def print_something_interesting(self, data):
        """
        Analyzes the percentage of automatic, semi-automatic and manual transmissions in cars from a dataset.
        @param data dict: The dictionary containing the car data read from the csv
        @return None
        """
        automatic_count = 0
        manual_count = 0
        semi_automatic_count = 0
        total_cars = 0

        for car in data:
            if "Transmission" in car:
                transmission = car["Transmission"].lower()
                if "semi-automatic" in transmission:
                    semi_automatic_count +=1
                elif "automatic" in transmission:
                    automatic_count += 1
                elif "manual" in transmission:
                    manual_count += 1
                total_cars += 1

        automatic_percentage = (automatic_count / total_cars) * 100
        manual_percentage = (manual_count / total_cars) * 100
        semi_automatic_percentage = (semi_automatic_count / total_cars) * 100

        print(f"\nteam member 02 Nathan Sharpe\nAutomatic percentage: {automatic_percentage} Semi-automatic percentage: {semi_automatic_percentage} Manual percentage: {manual_percentage}\n")