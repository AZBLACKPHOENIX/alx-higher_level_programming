#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.
    """
    if a_dictionary:
        # Find the key with the maximum value in the dictionary
        best_key = max(a_dictionary, key=a_dictionary.get)
        return best_key
    else:
        return None

if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))

