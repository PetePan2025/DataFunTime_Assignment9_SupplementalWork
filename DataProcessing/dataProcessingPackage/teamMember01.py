# File Name : teamMember01.py
# Student Name: Eirlys Vo
# email: vopq@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/16/25
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Complete a module in dataProcessingPackage 
# Brief Description of what this module does: Learn how to access and get data from CSV and do some implementations with data.
# Citations: N/A
# Anything else that's relevant: N/A


class teamMember01:
    def print_something_interesting(self, data):
        """
        Print average price of each Fuel Type
        @param data Dictionary: The car data to process
        @return None
        """
        price_fuel_type = {}
        count_dict = {}
        for idx,row in enumerate(data):

            if row['Fuel_Type'] not in price_fuel_type:
                price_fuel_type[row['Fuel_Type']] = float(row['Price'])
                count_dict[row['Fuel_Type']] = 1
            else:
                price_fuel_type[row['Fuel_Type']] += float(row['Price'])
                count_dict[row['Fuel_Type']] += 1

        print('\nTeam member 01 - Eirlys Vo:')
        for key,val in price_fuel_type.items():
            print(f'Average price of fuel type {key}: ${round(val/count_dict[key], 2)}')