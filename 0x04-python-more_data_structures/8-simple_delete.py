#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.
    """
    # Check if the key exists in the dictionary before attempting to delete
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]}
    
    new_dict = simple_delete(a_dictionary, 'track')
    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")
    print("--")
    
    for key, value in sorted(new_dict.items()):
        print(f"{key}: {value}")
    print("--")
    print("--")
    
    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")
    print("--")
    
    for key, value in sorted(new_dict.items()):
        print(f"{key}: {value}")

