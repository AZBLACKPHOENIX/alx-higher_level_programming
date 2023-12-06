#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary

if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
    
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    for key, value in sorted(new_dict.items()):
        print(f"{key}: {value}")
    print("--")
    
    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")
    print("--")
    print("--")
    
    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    for key, value in sorted(new_dict.items()):
        print(f"{key}: {value}")
    print("--")
    
    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")

