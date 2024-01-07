#!/usr/bin/python3
def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :

    Args:
    - text (str): Input text.

    Raises:
    - TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = [".", "?", ":"]
    current_line = ""

    for char in text:
        current_line += char
        if char in characters:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line.strip():
        print(current_line.strip())
