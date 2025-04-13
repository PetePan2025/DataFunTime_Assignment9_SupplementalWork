# File Name: teamMember03.py
# Student Name: Peter Phan
# email: phanpv@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 04/16/2025
# Course #/Section: IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Complete the method in the class of a incomplete module to process data and generate some interesting output. 
# Brief Description of what this module does: Learn about accessing a database and producing results from the data. 
# Citations: W3Schools: https://www.w3schools.com/python/ref_dictionary_setdefault.asp
#            StackOverflow: https://stackoverflow.com/questions/73694901/how-to-chain-pythons-set-add-while-updating-dictionary-values-being-sets
# Anything else that's relevant: N/A

class teamMember03:
    """
    Searches the data from a CSV file to extract the number of models from each brand.
    """
    def print_something_interesting(self, data):
        """
        Searches the data for the number of models from each brand from the dataset.
        @param data dict: The dictionary containing the car data 
        @return None
        """
        brand_model_count = {}

        for car in data:
            brand = car.get('Brand')
            model = car.get('Model')
            if brand and model:
                brand_model_count.setdefault(brand, set()).add(model)

        print("team member 03 Peter Phan - Number of Models per Brand:")
        if brand_model_count:
            for brand, models in brand_model_count.items():
                print(f"{brand}: {len(models)} models")
        else:
            print("No 'Brand' or 'Model' data found")


         