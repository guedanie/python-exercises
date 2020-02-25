## Q1 Import and test 3 of the functions from the functions exercsies

import function_exercises

# import the module and refer to the function with the ```.``` syntax
function_exercises.is_vowel('a')

# use from to import the function directly

from function_exercises import twelveto24

# use from to import and give the function a different name

from function_exercises import is_two as contains_two

## For the following exercises, read about and use the itertool module from the standard library

#How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

from itertools import combinations
from itertools import combinations_with_replacement
from itertools import product

len(list(product([1,2,3], 'abc')))


#How many different ways can you combine two of the letters from "abcd"?

len(list(combinations("abcd", 2)))

## Save this file as profiles.json inside of your exercises directory. 
# Use the load function from the json module to open this file, it will 
# produce a list of dictionaries. Using this data, write some code that 
# calculates and outputs the following information:

import json
from pprint import pprint

new_dictionary = json.load(open("profiles.json"))

pprint(new_dictionary)

new_dictionary[0].keys() # This returns all keys in a dictionary

# Total number of users

len([x['_id'] for x in new_dictionary])     

# Result = 19

# Number of active users
len([x['_id'] for x in new_dictionary if x['isActive']]) 

# Result = 9

# Number of inactive users

len([x['_id'] for x in new_dictionary if not x['isActive']]) 

# Result = 10

# Grand total of balances for all users

# Turn it into a function: 

def turning_string_to_float(profile):
    return float(profile['balance'].replace('$', '').replace(',',''))

total_balance = sum([turning_string_to_float(profile) for profile in new_dictionary])

# Result is 52667.02


# Average balance per user

total_balance / len(new_dictionary)

# Result = 2771.94

# User with the lowest balance
for profile in new_dictionary:
    profile["balance"] = profile['balance'].replace('$','')
    profile['balance'] = profile['balance'].replace(',','')
    profile['balance'] = float(profile['balance'])

balance = [(profile['name'],profile['balance']) for profile in new_dictionary] 
min(balance, key = lambda item: item[1])                                                  

# Result = 'Avery Flynn', 1214.1)

# User with the highest balance
max(balance, key = lambda item: item[1]) 

min(new_dictionary, key= turning_string_to_float)

# Result =  ('Fay Hammond', 3919.64),

# Most common favorite fruit
fruits = [profile["favoriteFruits"] for profile in new_dictionary]
fruit_count = [(fruit, fruits.count(fruit)) for fruit in set(fruits)]      
# Result = [('banana', 6), ('strawberry', 9), ('apple', 4)]

max(fruit_count)                                                                          
# Out[114]: ('strawberry', 9)

# Least most common favorite fruit
min(fruit_count)                                                                          
# Out[115]: ('apple', 4)

# Total number of unread messages for all users
unread_messages = [profile['greeting'] for profile in new_dictionary] 

int(''.join([c for c in unread_messages if c.isdigit()]))

def get_number_messages(string):
    parts = string.split(' ')
    for part in parts:
        if part.isdigit():
            return int(part)

sum([get_number_messages(profile) for profile in unread_messages])

#Result = 210

# Quick and dirty:

int([profile["greeting"][-19:-17].strip() for profile in new_dictionary])