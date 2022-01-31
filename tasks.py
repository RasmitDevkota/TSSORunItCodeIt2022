def isint(number):
    if number.isdecimal():
        return True
    elif number.startswith("-") and number[1:].isdecimal():
        return True
    else:
        return False

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def palindrome_checker(string):
    if len(string) <= 2048:
        return string == string[::-1]
    else:
        return "Please enter a piece of text of length less than or equal to 2048 characters!"

def vowel_consonant_counter(string):
    if not string.isalpha() or len(string) > 2048:
        return "Please enter a single word with 2048 or less alphabetical characters!"

    vowels = 0

    consonants = 0

    for vowel in "aeiou":
        vowels += string.lower().count(vowel)

    consonants = len(string) - vowels

    return "Input word has {} vowels and {} consonants".format(vowels, consonants)

def arithmetic(string):
    if len(string.split()) < 2:
        return "Please only input integers < 2000000000 without commas!"
    elif not isint(string.split()[0]) or not isint(string.split()[1]):
        return "Please only input integers < 2000000000 without commas!"

    numbers = [int(number) for number in string.split()]

    n1, n2 = numbers
    
    if n2 == 0:
        return "Please make sure the second number isn't 0 (cannot divide by 0)!"

    return "{n1}+{n2}={sum}, {n1}-{n2}={difference}, {n1}*{n2}={product}, and {n1}/{n2}={quotient}".format(
        n1=n1, n2=n2, sum=n1+n2, difference=n1-n2, product=n1*n2, quotient=n1/n2
    )

def area_of_circle(string):
    if not string.isdecimal():
        return "Please only input positive integers < 2000000000 without commas!"

    radius = int(string)

    if not radius < 2000000000:
        return "Please only input positive integers < 2000000000 without commas!"

    area = round(3.14159 * radius ** 2, 2)

    return "Area of a circle with radius {}: {}".format(radius, area)

def even_odd_checker(string):
    if not isint(string):
        return "Please only input integers < 2000000000 without commas!"

    number = int(string)

    if not number < 2000000000:
        return "Please only input integers < 2000000000 without commas!"

    parity = "This number is even!" if number % 2 == 0 else "This number is odd!"

    return parity

def factorial(string):
    if not isint(string):
        return "Please only input integers betweeen 0 and 100, inclusive!"

    number = int(string)

    if number < 0:
        return

    if number == 0:
        return 1

    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i

    return factorial

def fibonnaci_series(string):
    if not string.isdecimal():
        return "Please only input integers between 1 and 100, inclusive!"

    count = int(string)

    zero = 0
    one = 1

    if count < 1 or count > 100:
        return "Please enter an integer between 1 and 100, inclusive!"
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

def seconds_to_whole_years(string):
    if not string.isdecimal():
        return "Please only input positive integers without commas!"

    seconds = int(string)

    if seconds >= 2000000000:
        return "Please enter a positive number of seconds less than 2000000000 without commas!"

    years = seconds//31556952

    return years

def nand(string):
    bitstrings = string.split()
    
    if len(string.split()) < 2:
        return "Please enter two space-separated bitstrings of length < 128!"
    elif len(bitstrings[0]) >= 128 or len(bitstrings[1]) >= 128:
        return "Please enter two space-separated bitstrings of length < 128!"

    if bitstrings[0].isdecimal() and bitstrings[1].isdecimal() and len(bitstrings[0]) == len(bitstrings[1]):
        nand_result = ""

        for i in range(len(bitstrings[0])):
            bit1str = bitstrings[0][i]
            bit2str = bitstrings[1][i]

            if bit1str in ["0", "1"] and bit2str in ["0", "1"]:
                bit1 = 1 if bit1str == "1" else 0
                bit2 = 1 if bit2str == "1" else 0
            else:
                return "Please enter two space-separated bitstrings!"

            nand_result += str(not (bit1 & bit2))

        return nand_result.replace("True", "1").replace("False", "0")
    else:
        return "Please enter two space-separated bitstrings!"

def compound_interest(string):
    if len(string.split()) < 3:
        return "Please enter a principal < 1000000, rate < 2, and time in years < 100 without any dollar signs or commas!"
    
    numbers = [number for number in string.split(" ")]
    
    if all(isfloat(number) for number in numbers):
        numbers = [float(number) for number in numbers]
    else:
        return "Please enter a principal < 1000000, rate < 2, and time in years < 100 without any dollar signs or commas!"

    principal, rate, time = numbers[0], numbers[1], numbers[2]

    if not all(number > 0 for number in numbers) or len(numbers) != 3 or principal >= 1000000 or rate >= 2 or time >= 100:
        return "Please enter a principal < 1000000, rate < 2, and time in years < 100 without any dollar signs or commas!"

    interest = int(round(principal * rate ** time, 2))

    return "Total interest earned: {}".format(interest)

def constant_shift_caesar_cipher(string):
    if len(string) >= 128:
        return "Please enter a plaintext string of length < 128!"

    shift = 7

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    encrypted_string = ""

    for plaintext in string:
        if plaintext in alphabet:
            plaintext_index = alphabet.index(str.capitalize(plaintext))

            ciphertext_index = plaintext_index + shift

            ciphertext = alphabet[ciphertext_index]

            if ciphertext.islower():
                ciphertext = ciphertext.lower()

            encrypted_string += ciphertext
        else:
            encrypted_string += plaintext

    return encrypted_string

def coordinate_distance(string):
    if not string.startswith("(") or not string.endswith(")"):
            return "Please enter coordinates in the format (x, y, z, ...)!"
    
    trimmed_string = string.replace("(", "").replace(")", "").replace(" ", "").split(";")

    string_coordinates = [coordinate.split(",") for coordinate in trimmed_string]

    number_coordinates = []
    
    expected_dimension = 0

    for coordinate in string_coordinates:
        if len(coordinate) > 10:
            return "Please enter coordinates with 10 or less dimensions!"

        number_coordinate = []
        
        if expected_dimension == 0:
            expected_dimension = len(coordinate)
        else:
            if len(coordinate) != expected_dimension:
                return "Please enter coordinates with the same number of 10 or less dimensions!"

        for ordinate in coordinate:
            if not isint(ordinate):
                return "Please enter coordinates with integer values between -1024 and 1024, inclusive!"
            elif int(ordinate) < -1024 and int(ordinate) > 1024:
                return "Please enter coordinates with integer values between -1024 and 1024, inclusive!"
            else:
                number_coordinate.append(int(ordinate))
        
        number_coordinates.append(number_coordinate)

    squared_distance = 0

    for i in range(len(number_coordinates[0])):
        squared_distance += (number_coordinates[1][i] - number_coordinates[0][i]) ** 2

    distance = round(squared_distance ** 0.5, 4)

    return distance

def secret_linear_function(string):
    if not isint(string):
        return "Please enter a single integer < 1000000!"

    x = int(string)

    if x >= 1000000:
        return "Please enter a single integer < 1000000!"

    y = 11 * x + 22

    return y

def binary_to_decimal(string):
    if not string.isdecimal() or len(string) >= 32:
        return "Please enter a single bitstring of length < 32!"
    
    for bit in string:
        if not bit in ["0", "1"]:
            return "Please enter a single bitstring of length < 32!"

    decimal_num = int(string, 2)

    return decimal_num

def text_to_unicode(string):
    if len(string) >= 128:
        return "Please enter a piece of text of length < 128!"

    unicode_string = " ".join(str(ord(char)) for char in string).replace("\'", "")

    return unicode_string

def main():
    print("""
             Welcome to the TeslaOS v.20.22!
    -------------------------------------------------
    | 1.  Palindrome checker                        |
    | 2.  Vowel/Consonant counter                   |
    | 3.  Arithmetic calculator                     |
    | 4.  Area of a circle calculator               |
    | 5.  Even/odd checker                          |
    | 6.  Factorial calculator                      |
    | 7.  Fibonacci series generator                |
    | 8.  Compound interest calculator              |
    | 9.  Seconds to whole number of years          |
    | 10. NAND gate calculator                      |
    | 11. Constant-shift Caesar cipher encryption   |
    | 12. Coordinate distance calculator            |
    | 13. Secret linear function                    |
    | 14. Binary-to-decimal converter               |
    | 15. Text-to-Unicode converter                 |
    -------------------------------------------------
    """)

    task = input("Choose a task to run by entering the corresponding number!\n").replace(".", "")

    if not task.isdecimal():
        return print("Please enter a valid task number between 1 and 15!")

    task_num = int(task)

    output_string = ""

    if task_num == 1:
        print("This task will check whether or not a given piece of text is a palidrome.")
        input_string = input("Please enter a word or phrase to check!\n")
        output_string = palindrome_checker(input_string)
    elif task_num == 2:
        print("This task will count the number of vowels and consonants in a given word.")
        input_string = input("Please enter a single word with only alphabetical characters!\n")
        output_string = vowel_consonant_counter(input_string)
    elif task_num == 3:
        print("This task will calculate the sum, difference, product, and quotient of two numbers.")
        input_string_1 = input("Please enter an integer < 2000000000!\n")
        input_string_2 = input("Please enter a second non-zero integer < 2000000000!\n")
        input_string = input_string_1 + " " + input_string_2
        output_string = arithmetic(input_string)
    elif task_num == 4:
        print("This task will calculate the area of a circle with two-decimal place precision given an integer radius.")
        input_string = input("Please enter a single positive integer < 2000000000 without commas!\n")
        output_string = area_of_circle(input_string)
    elif task_num == 5:
        print("This task will determine whether an integer is even or odd.")
        input_string = input("Please enter a single integer < 2000000000 without commas!\n")
        output_string = even_odd_checker(input_string)
    elif task_num == 6:
        print("This task will calculate the factorial of a number.")
        input_string = input("Please enter a single integer betweeen 0 and 100, inclusive!\n")
        output_string = factorial(input_string)
    elif task_num == 7:
        print("This task will generate the Fibonacci series up to a given term.")
        input_string = input("Please enter a single integer between 1 and 100, inclusive!\n")
        output_string = fibonnaci_series(input_string)
    elif task_num == 8:
        print("This task will calculate the yearly compound interest earned from the principal, rate, and time.")
        input_string_1 = input("Please enter the principal amount as a positive decimal < 1000000 without dollar signs or commas!\n")
        input_string_2 = input("Please enter the interest rate as a positive decimal < 2!\n")
        input_string_3 = input("Please enter the time in years as a positive decimal < 100!\n")
        input_string = input_string_1 + " " + input_string_2 + " " + input_string_3
        output_string = compound_interest(input_string)
    elif task_num == 9:
        print("This task will convert a number of seconds to a whole number of years, only rounding down as necessary.")
        input_string = input("Please enter a single positive integer < 2000000000 without commas!\n")
        output_string = seconds_to_whole_years(input_string)
    elif task_num == 10:
        print("This task will compute the bitwise NAND operation between two bitstrings.")
        input_string = input("Please enter two space-separated bitstrings of length < 32!\n")
        output_string = nand(input_string)
    elif task_num == 11:
        print("This task encrypts messages using a Caesar cipher with a constant, predetermined shift, leaving non-alphabetical characters the same.")
        input_string = input("Please enter a plaintext string to encrypt!\n")
        output_string = constant_shift_caesar_cipher(input_string)
    elif task_num == 12:
        print("This task will calculate the Euclidean distance with four-decimal place precision between two coordinates in less than 10 dimensions with integer values between -1024 and 1024, inclusive.")
        input_string_1 = input("Please enter the first coordinate in the format (x, y, z, ...)!\n")
        input_string_2 = input("Please enter the second coordinate in the format (x, y, z, ...)!\n")
        input_string = input_string_1 + ";" + input_string_2
        output_string = coordinate_distance(input_string)
    elif task_num == 13:
        print("This task will input the given value into a linear function of the form y=mx+b, with m and b being constant, predetermined values.")
        input_string = input("Please enter a single integer without commas!\n")
        output_string = secret_linear_function(input_string)
    elif task_num == 14:
        print("This task will convert a bitstring (binary base) to a number in decimal base.")
        input_string = input("Please enter a single bitstring of length < 32!\n")
        output_string = binary_to_decimal(input_string)
    elif task_num == 15:
        print("This task will convert a piece of text into its decimal Unicode representation.")
        input_string = input("Please enter a piece of text to convert!\n")
        output_string = text_to_unicode(input_string)
    else:
        output_string = "Please select a valid task!"

    print(output_string)

main()
