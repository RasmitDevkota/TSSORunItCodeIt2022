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