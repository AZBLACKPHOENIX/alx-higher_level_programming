#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if not sentence:
        return (0, None)
    
    # Return the length of the sentence and its first character
    return (len(sentence), sentence[0])
