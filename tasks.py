def main():
    print("Welcome to the TeslaOS v.2")
    print("Choose a task to begin with!")

main()

# Easy Tasks

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

def arithmetic(string):
    # Split input string into a list of each number as integers
    numbers = [int(number.replace(",", "")) for number in string.split()]

    n1, n2 = numbers

    # Returns First Number divided by Second Number
    return "{n1}+{n2}={sum}, {n1}-{n2}={difference}, {n1}*{n2}={product}, and {n1}/{n2}={quotient}".format(
        n1=n1, n2=n2, sum=n1+n2, difference=n1-n2, product=n1*n2, quotient=n1/n2
    )

def area_of_circle(string):
    # Convert input string to radius integer
    radius = int(string.replace(",", ""))

    # Returns area of circle given radius
    return 3.14 * radius ** 2

def nand(string):
    bitstrings = string.split(" ")

    if bitstrings[0].isdigit() and bitstrings[1].isdigit() and len(bitstrings[0]) == len(bitstrings[1]):
        nand_result = ""

        for i in range(len(bitstrings[0])):
            bit1 = int(bitstrings[0][i])
            bit2 = int(bitstrings[1][i])

            if not isinstance(bit1, bool):
                return

            nand_result += str(not (bit1 & bit2))

        return nand_result.replace("True", "1").replace("False", "0")
    else:
        return

def compound_interest(string):
    numbers = [int(number.replace(",", "")) for number in string.split(" ")]

    if not all(number > 0 for number in numbers):
        return

    principal, rate, time = numbers[0], numbers[1], numbers[2]

    interest = principal * rate ** time

    return interest

def even_odd_checker(string):
    number = int(string.replace(",", ""))

    return number % 2 == 0

def factorial(string):
    number = int(string.replace(",", ""))

    if number < 0:
        return

    if number == 0:
        return 1

    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i

    return factorial

# Intermediate Tasks

def fibonnaci_series(string):
    count = int(string)

    zero = 0
    one = 1

    if count < 1:
        return
    if count == 1:
        return "0"
    else:
        series = "0 1"

        for i in range(2,count):
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

    number_coordinates = [int(ordinate) for coordinate in string_coordinates for ordinate in coordinate]

    squared_distance = 0

    for i in range(len(number_coordinates[0])):
        squared_distance += (number_coordinates[1][i] - number_coordinates[0][i]) ** 2

    distance = squared_distance ** 0.5

    return distance

def seconds_to_whole_years(string):
    seconds = int(string.replace(",", ""))

    years = seconds//31556952

    return years

# Hard Tasks

def text_to_ascii(string):
    ascii_string = " ".join([str(ord(char)) for char in string])

    return ascii_string

def binary_to_decimal(string):
    if not string.isdigit():
        return

    string_reversed = string[::-1]

    decimal_num = sum([2 ** n if string_reversed[n] == "1" else 0 for n in range(len(string_reversed))])
