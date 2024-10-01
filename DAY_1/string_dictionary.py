"""
String Manipulation
Challenge: Write a program that takes a sentence as input and returns a dictionary where the keys are the words and the values are the lengths of those words.
Objective: Practice string splitting, looping through strings, and working with dictionaries.
"""
phrase = "In the year 2050 a king was born in the planet of Mercury"

def str_dic(s):
    # Write code here
    words = s.split()
    word_dict = {}
    for word in words:
        word_dict[word] = len(word)
    return word_dict

print(str_dic(phrase))