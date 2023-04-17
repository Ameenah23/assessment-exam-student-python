"""
Given two strings, create a function that returns the total number of unique characters from the combined string.

Examples:
    count_unique_chars("apple", "play") ➞ 5
    "appleplay" has 5 unique characters:  "a", "e", "l", "p", "y"

    count_unique_chars("sore", "zebra") ➞ 7

    count_unique_chars("a", "soup") ➞ 5

Notes:
 - Careful with empty strings
 - All characters will be lowercase.

"""

string_1 = input('Input string_1 :')
string_2 = input('Input string_2 :')

def count_unique_chars(string_1, string_2):
    result = []
    for ch in string_1:
        if ch in string_1 and not ch in result:
            result += ch
    for ch in string_2:
        if ch in string_2 and not ch in result:
            result += ch
    return result
    
print(len(count_unique_chars(string_1, string_2)))
print(count_unique_chars(string_1, string_2))
    