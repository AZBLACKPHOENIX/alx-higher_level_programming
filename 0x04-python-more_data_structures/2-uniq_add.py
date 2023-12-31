#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to store unique integers
    unique_set = set()

    # Iterate through each element in the original list
    for element in my_list:
        # Add the element to the set (sets automatically ignore duplicates)
        unique_set.add(element)

    # Sum the unique integers in the set
    result = sum(unique_set)

    return result

