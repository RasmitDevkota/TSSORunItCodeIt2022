# Easy Tasks

from tkinter import Y


def palindrome_checker(word):
    # Checks to see if the string is the same as itself reverse
    # Returns True if param:word is a palindrome
    return word == word[::-1]

def vowel_consonant_counter(word):
    # Create counter variable for number of vowels
    vowels = 0

    # Create counter variable for number of cosonants
    consonants = 0

    # Loop over all possible vowels
    for vowel in "aeiou":
        # Count number of letters in the word that match the current possible vowel and add to the counter
        vowels += word.lower().count(vowel)

    # Since every letter is either a vowel or a consonant,
    # set the number of consonants equal to the number of non-vowel characters
    consonants = len(word) - vowels

    # Returns # of Vowels; (space); # of Consonants for param:word
    return str(vowels) + " " + str(consonants)

def add_numbers(string):
    # Split input string into a list of each number as integers
    numbers = [int(number) for number in string.split()]

    # Returns First Number + Second Number
    return numbers[0] + numbers[1]

def subtract_numbers(string):
    # Split input string into a list of each number as integers
    numbers = [int(number) for number in string.split()]

    # Returns First Number - Second Number
    return numbers[0] - numbers[1]

def multiply_numbers(string):
    # Split input string into a list of each number as integers
    numbers = [int(number) for number in string.split()]

    # Returns First Number multiplied by Second Number
    return numbers[0] * numbers[1]

def divide_numbers(string):
    # Split input string into a list of each number as integers
    numbers = [int(number) for number in string.split()]

    # Returns First Number divided by Second Number
    return numbers[0] / numbers[1]

def area_of_circle(string):
    # Convert input string to radius integer
    radius = int(string)

    # Returns area of circle given radius
    return 3.14 * radius ** 2

def even_odd_checker(string):
    return int(string) % 2 == 0

def factorial(string):
    factorial = 1
    for i in range(1, int(string)+1):
        factorial = factorial * i
    return factorial

# Intermediate Tasks
def fibonnaci_series(count):
    zero = 0
    one = 1
    if int(count) == 1:
        return "0"
    else:
        series = "0 1"
        for i in range(2,int(count)):
            c = zero + one
            zero = one
            one = c
            series += " " + str(c)
        return series

def constant_shift_caesar_cipher(string):
    shift = 7

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    encrypted_string = ""

    for plaintext in string:
        plaintext_index = alphabet.index(str.capitalize(plaintext))

        ciphertext_index = plaintext_index + shift

        ciphertext = alphabet[ciphertext_index]

        if ciphertext.islower():
            ciphertext = ciphertext.lower()

        encrypted_string += ciphertext

    return encrypted_string

def secret_linear_function(string):
    x = int(string)

    y = 11 * x + 22

    return y

def coordinate_distance(string):
    trimmed_string = string.replace("(", "").replace(")", "").split(";")

    string_coordinates = [coordinate.split(",") for coordinate in trimmed_string]

    number_coordinates = [int(ordinate) for coordinate in trimmed_string for ordinate in coordinate]

    squared_distance = 0

    for i in range(len(number_coordinates[0])):
        squared_distance += (number_coordinates[1][i] - number_coordinates[0][i]) ** 2

    distance = squared_distance ** 0.5

    return distance

def seconds_to_datetime(string):
    seconds = int(string)

    minutes = seconds/60

    hours = minutes/60

    days = hours/24

    weeks = days/7

    months = weeks/4

    years = months/12

    return "{} years, {} months, {} weeks, {} days, {} hours, {} minutes, {} seconds".format(round(years), round(months), round(weeks), round(days), round(hours), round(minutes), round(seconds))

# Hard Tasks

ascii_dict = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "E": [],
}

def text_to_ascii(string):
    if not string.isalpha():
        return "String contains non-alphabetical characters"

    ascii_string = ""

    for row in range(8):
        for letter in string:
            ascii_string += ascii_dict[letter.upper()][row]

        ascii_string += "\n"

    return ascii_string