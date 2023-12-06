#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the replaced values
    new_list = []

    # Iterate through each element in the original list
    for element in my_list:
        # Replace the element if it matches the search value, otherwise keep the original element
        new_list.append(replace if element == search else element)

    return new_list
