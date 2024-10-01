"""
<Assignment 2>

Copyright (c) 2021 -- This is the 2021 Spring B version of the Template
Licensed
Written by <Wenjie Zheng> <----- PLEASE, WRITE YOUR NAME HERE

# you can also rely on the docstring documentation from pandas on how to format
# https://pandas.pydata.org/pandas-docs/stable/development/contributing_docstring

"""

def function1(var1, var2, var3):
    """
    :param var1: please describe
    :param var2: please describe
    :param var3: please describe
    :return:
    """
    return

def function2(var1, var2, var3):
    """
    :param var1:
    :param var2:
    :param var3:
    :return:
    """
    return

def dict_func(dictionary, input_key):
    """
    :param dictionary: A dictionary whose values are to be converted to uppercase
    :param input_key: A key to be checked for existence in the dictionary
    :return: List of key, value tuple pairs of the dictionary
    """
    # Convert all elements in the dictionary values to uppercase and print the result
    upper_case_dict = {key: str(value).upper() for key, value in dictionary.items()}
    print("Dictionary with uppercased values:", upper_case_dict)

    # Check if input_key exists in the dictionary
    key_exists = input_key in dictionary
    print("Does the input_key exist in the dictionary?", key_exists)

    # Convert dictionary to a list of key, value tuple pairs and return
    dict_as_list = list(upper_case_dict.items())
    return dict_as_list

if __name__ == "__main__":
    # Main functions to Run
    function1(var1=123, var2=456, var3=678)

    # Creating the Canada dictionary
    Canada = {
        "Indigenous groups": ["Cree", "Inuit", "Métis", "Haida", "Ojibwe"],
        "National parks": ["Banff", "Jasper", "Gros Morne", "Yoho", "Prince Albert"],
        "Provinces": ["Ontario", "Quebec", "British Columbia", "Alberta", "Manitoba"]
    }
    
    # Example usage of dict_func with the Canada dictionary and key 'Indigenous groups'
    result = dict_func(Canada, 'Indigenous groups')
    print("List of key, value tuple pairs:", result)


	
