## Exercises 4.5_function_exercises.py

# Q1: Define a function named is_two. 
# It should accept one input and return True if the passed input 
# is either the number or the string 2, False otherwise.

def is_two(x):
    if x == 2 or x == '2':
        return True
    else:
        return False

## The easier and shorter way to write this is:

#def is_two(x):
    #return x == 2 or x == '2'

# Q2: Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.
vowels = "aeiouAEIOU"
def is_vowel(x):
    if x in vowels:
        return True
    else:
        return False


# This could be written as:

#def is_vowel(x):
    #return len(x) == 1 and x in vowels

#Q3: Define a function named is_consonant. 
# It should return True if the passed string is a consonant, 
#False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(x):
    if x not in vowels:
        return True
    else:
        return False

#Q4: Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word 
# if the word starts with a consonant.

def title_word(string):
    string = str(string)
    if string[0] not in vowels:
        return string.title()
    else:
        return string

#Q5: Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) and 
# the bill total, and return the amount to tip.

percentage = 0
total = 0
def calculate_tip(percentage, total):
    return total * percentage

# Q6: Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.

def apply_discount(price, discount_percentage):
    new_price = price - (price * discount_percentage)
    return f"The new total price is ${new_price}"

# Q7: Define a function named handle_commas. 
# It should accept a string that is a number that 
# contains commas in it as input, and return a number as output.

def handle_commas(string):
    if string.isdigit() == False and ',' in string:
        string = string.replace(',','')
        string = int(string)
        return string
    else:
        return 'Input not a string that is a number or a number with a comma'

# Q8: Define a function named get_letter_grade. 
# It should accept a number and return the letter 
# grade associated with that number (A-F).

def get_letter_grade(number):
    if number in range(90,100):
        return f"{number} is an A"
    elif number in range(80,89):
        return f"{number} is an B"
    elif number in range(70,79):
        return f"{number} is an C"
    elif number in range(60,69):
        return f"{number} is an D"
    else:
        return f"{number} is a failing grade, F"

# Q9: Define a function named remove_vowels 
# that accepts a string and returns a 
# string with all the vowels removed.

def remove_vowels(string):
    for x in string.lower():
        if x in vowels:
            string = string.replace(x, '')
    return (string)

#Q10: Define a function named normalize_name. 
# It should accept a string and return a valid python identifier, 
# that is:
#anything that is not a valid python identifier should be removed
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores
#for example:
#Name will become name
#First Name will become first_name
#% Completed will become completed

not_python_identifiers = '@, #, %, &, *, !, $, ^'
def normalize_name(string):
    for letter in string:
        if letter in not_python_identifiers:
            string = string.replace(letter, '')
    return string.lower().strip().replace(' ', '_')
        
   

#Q11: Write a function named cumsum that accepts a list 
# of numbers and returns a list that is the cumulative sum of 
# the numbers in the list.
#cumsum([1, 1, 1]) returns [1, 2, 3]
#cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumsum(list):
    s = list
    for number in range(1, len(s)):
        s[number] += s[number - 1]
    return s

## Bonus n.1

# Create a function named twelveto24. It should accept a
#  string in the format 10:45am or 4:30pm and
#  return a string that is the representation of the time
#  in a 24-hour format. Bonus write a function that
#  does the opposite.

def twelveto24(string):
    if (string[-2:] == 'am' or string[-2:] == "AM") and string[:2] == '12':
        return '00' + string[2:-2]
    elif string[-2:] == 'am' or string[-2:] == "AM":
        return string[:-2]
    elif (string[-2:] == "PM" or string[-2:] == 'pm') and string[:2] == '12':
        return string[:-2]
    else:
        return str(int(string[:2]) + 12) + string[2:8]

#mini bonus:
def twentyfourto12(string):
    if string[0] != '0' or string[0] != ' ':
        new_number = str(int(string[:2]) - 12) + string[2:8] + 'PM'
    else:
        new_number =  string + 'AM'
    return new_number

# Bonus n. 2
# Create a function named col_index. It should accept
#  a spreadsheet column name, and return the index number
#  of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27
# max rows = 'XFT' = 16,384

single_letters = "abcdefghijklmnopqrstuvwxyz"
position = 0
def col_index(column_name):
    column_name = column_name.lower()
    length = len(column_name)
    if length == 1:
        return single_letters.index(column_name) + 1
    elif length > 1:
        if column_name[0] in single_letters: 
            index = single_letters.index(column_name[0]) + (26 * (single_letters.index(column_name[0])+ 1))
            if column_name[0] == 'a':
                index += 1
            else: 
                index -= (single_letters.index(column_name[0]) - 1)
        if column_name[1] in single_letters:
            index += single_letters.index(column_name[1])
    return index

# ## If col_index is three digits:
# single_letters = "abcdefghijklmnopqrstuvwxyz"
# position = 0
# def col_index(column_name):
#     column_name = column_name.lower()
#     length = len(column_name)
#     index = 0
#     if length == 1:
#         return single_letters.index(column_name) + 1
#     elif length == 2:
#         if column_name[0] in single_letters: 
#             index = single_letters.index(column_name[0]) + (26 * (single_letters.index(column_name[0])+ 1))
#             if column_name[0] == 'a':
#                 index += 1
#             else: 
#                 index -= (single_letters.index(column_name[0]) - 1)
#         if column_name[1] in single_letters:
#             index += single_letters.index(column_name[1])
#     elif length == 3:
#         if column_name[0] in single_letters: 
#             index = single_letters.index(column_name[0]) + (26 * (single_letters.index(column_name[0])+ 1)) 
#             if column_name[0] == 'a':
#                 index += 1
#             else: 
#                 index -= (single_letters.index(column_name[0]) - 1)
#         if column_name[1] in single_letters:
#             index = index * (single_letters.index(column_name[1]) + ( 26 * (single_letters.index(column_name[1])+ 1)))
#             if column_name[0] == 'a':
#                 index += 1
#             else: 
#                 index -= (single_letters.index(column_name[0]) - 1)
#         if column_name[2] in single_letters:
#             index += single_letters.index(column_name[2])
        
            
#     return index

## Alternative:

# def col_index(column_name):
#     index = 0
#     if len(column_name) == 1:
#         for letter in column_name:
#             index = single_letters.index(column_name[0]) + 1
#     if len(column_name) == 2:
#         for letter in column_name:
#         index = (single_letters.index(column_name[0]) + 1) + (single_letters.index(column_name[1])) + 26
#     if len(column_name) == 3:
#         for letter in column_name:
#         index = (single_letters.index(column_name[0]) + 1) * (26 * (single_letters.index(column_name[1]) + 1)) * (26 * (single_letter.index(column_name[2]) + 1))
#     return index