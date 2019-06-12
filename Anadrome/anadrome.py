'''
An anagram is a word or phrase formed by rearranging the letters of a different word of phrase.
For example, "Sool" is an anagram for "Solo".

A palindrome is a word or phrase which reads the same backward as forward, such as "madam".

An anadrome is a word or phrase if any of its anagrams form a palindrome.

For example:
Input: "SoloSolo"
Output: yes ("SoollooS" is an anagram of "SoloSolo" which is also a palindrome).

Write a program to determine if the user input is an anadrome or not.
'''

import math

def palindrome_check(string_var):
    string_length = len(string_var)
    total_runs = math.ceil(string_length / 2)
    palindrome = True
    for i in range(total_runs):
        if string_var[i] != string_var[-i-1]:
            palindrome = False
            break
    return palindrome

def anogram_generator(string_var):
    length_var = len(string_var)
    total_permutations = math.factorial(length_var)
    
    
def cyclic_permutation(vector):
    cycled_vector = vector[1:]
    cycled_vector.extend(vector[0])
    return cycled_vector

def set_creator(array):
    array_length = len(array)
    array_set = {array[0]}
    for i in range(array_length-1):
        array_set.add(array[i+1])
    return array_set

input_string = input("Enter Test String \n")
# palindrome_check(input_string)
print(set_creator(input_string))