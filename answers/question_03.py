"""
Create a function that takes a string of lowercase characters and returns that string reversed and in upper case.

Examples:
    reverse_capitalize("abc") ➞ "CBA"

    reverse_capitalize("hellothere") ➞ "EREHTOLLEH"

    reverse_capitalize("input") ➞ "TUPNI"
"""
string = input('Input the string : ')

def reverse_capitalize(string):
    x = string
    new_string = x[::-1].upper()
    return new_string
print(reverse_capitalize(string))
