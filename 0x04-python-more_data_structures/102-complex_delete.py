#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary.
    """
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]
    
    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary

if __name__ == "__main__":
    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
    new_dict = complex_delete(a_dictionary, 'C')
    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")
    print("--")
    
    for key, value in sorted(new_dict.items()):
        print(f"{key}: {value}")
    print("--")
    print("--")
    
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")
    print("--")
    
    for key, value in sorted(new_dict.items()):
        print(f"{key}: {value}")

