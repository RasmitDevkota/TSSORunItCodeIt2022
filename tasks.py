def palindrome_checker(word):
    return word == word[::-1] # Returns True if param:word is a palindrome

def vowel_consonant_counter(word):
    vowels = 0
    consonants = 0
    for vowel in "aeiou":
            vowels += word.lower().count(vowel)
    consonants = len(word)-vowels
    return str(vowels) + " " + str(consonants) # Returns # of Vowels; (space); # of Consonants for param:word
    
def add_numbers(string):
    return int(string.split()[0]) + int(string.split()[1]) # Returns First Number + Second Number

def subtract_numbers(string):
    return int(string.split()[0]) - int(string.split()[1]) # Returns First Number - Second Number

def multiply_numbers(string):
    return int(string.split()[0]) * int(string.split()[1]) # Returns First Number multiplied by Second Number

def divide_numbers(string):
    return int(string.split()[0]) / int(string.split()[1]) # Returns First Number divided by Second Number

def area_of_circle(string):
    return int(string)*3.14*int(string) # Returns area of circle given radius