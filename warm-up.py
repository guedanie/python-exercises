# Take the word EASY: Its first three letters — E, A and S — are the fifth, first, and nineteenth letters, 
# respectively, in the alphabet. If you add 5, 1, and 19, you get 25, which is the value of the 
# alphabetical position of Y, the last letter of EASY.

## Cna you think of a common five-letter word that works in the opposite way - 
# in which the value of the alphabetical positions of its last four letters add up to the 
# value of the alphabetical position of its first letter? 
import pandas as pd

with open('/usr/share/dict/words') as f:
    words = f.read().split('\n')
    
five_words = [x for x in words if len(x) == 5]

def find_value_of_letter(string):
    string = string.lower()
    letters = pd.Series(list(string))
    alphabet = pd.Index(list("abcdefghijklmnopqrstuvwxyz"))
    last_three = letters[-4:]
    first = letters[0]
    count_last = 0
    count_first = 0
    list_of_words = []
    for x in last_three:
        count_last += alphabet.get_loc(x) + 1
    for x in first:
        count_first += alphabet.get_loc(x) + 1
    if count_last == count_first:
        list_of_words += [string]
    return count_last == count_first

    words_value = [x for x in five_words if find_value_of_letter(x)] 

    words_value