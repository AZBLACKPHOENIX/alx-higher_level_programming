#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create a new list to store True or False based on whether the integer is a multiple of 2
    result_list = []
    
    # Check if the input list is empty
    if not my_list:
        return result_list

    # Iterate through the original list
    for num in my_list:
        # Check if the integer is a multiple of 2
        result_list.append(num % 2 == 0)
    
    return result_list
