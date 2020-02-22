## Conditional Basics:

#a. prompt the user for a day of the week, print out whther the day is 
# Monday or not

day = input("What day of the week is today? ")

if day.lower() == 'monday':
    print("Today is " + day.title())
else:
    print("Today is not " + day.title())


# b. Prompt the user for a day of the week, print out whether the day is a 
# weekday or a weekend
week = ['Monday', 'Tueday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']

day_of_week = input( "Pick a day: ")

if day_of_week in week:
    print(day_of_week.title() + " is part of the week")
elif day_of_week in weekend:
    print(day_of_week.title() + " is part of the weeekend")
else:
    print("That's not a day of the week")

# c. create variables and make up values for

# * the number of hours worked in one week
# * the hourly rate
# * how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours

while True: 

    n_hours_worked = int(input("How many hours did you work this week? "))
    hourly_rate = int(input("What was your hourly rate? "))
    difference = 0


    if n_hours_worked <= 40:
        pay_check = n_hours_worked * hourly_rate
    elif n_hours_worked > 40:
        difference =  n_hours_worked - 40
        pay_check = (40 * hourly_rate) + ((difference * 1.5) * hourly_rate)
        
    print(f'You made ${pay_check} this week, you worked {n_hours_worked} hour(s) for an hourly rate of ${hourly_rate}')
        
    
    try_again = input("Would you like to calculate a different set of numbers? (y/n)")
    if try_again == 'y':
        continue
    else:
        break

## Loop Basics
# a. While
#     * Create an integer varible i with a value of 5
#     * Create a while loop that runs so long as i is less than or equal to 15
#     * Each loop iteration, output the current value of i, then increment i by one

i = 5

while i <= 15:
    print(i)
    i += 1

# * Create a while loop that will count by 2's starting with 0 and 
# ending at 100. Follow each number with a new line
# * Alter your loop to count backwards by 5's from 100 to -10
# * Create a while loop that starts at 2, and displays 
# the number squared on each line while the number is less than 1,000,000. 

i = 0

while i <= 100:
    print(i)
    i += 2
    

# * Write a loop that uses print to create the output shown below

i = 100 

while i >= 5:
    print(i)
    i -= 5

## For Loops

# * Write some code that prompts the user for a number,
#  then shows a multiplication table up through 10 for that number.

input_number = int(input("Pick a number: "))

for i in range(1,11):
    print(f"{input_number} x {i} = {input_number*i}")

# * Create a ```for``` loop that uses ``` print ``` to create the ourput shown

for i in range(1,10):
    print(str(i)*i)

#### Break and Continue

# * Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if
#  they enter invalid input.   
#     (Hint: use the isdigit method on strings to determine this).     
#     Use a loop and the continue statement to output all the odd 
# numbers between 1 and 50, except for the number the user entered.

while True:
    odd_number_to_skip = input("Pick an odd number between 1 and 50: ")

    while odd_number_to_skip.isdigit() == False or int(odd_number_to_skip) % 2 == 0 or int(odd_number_to_skip) not in range(1,50):
        print(f"{odd_number_to_skip} is cool, but we need a odd number between 1 and 50: ")
        odd_number_to_skip = input("Pick an odd number between 1 and 50 ")

    while odd_number_to_skip.isdigit() == True and int(odd_number_to_skip) % 2 != 0 and int(odd_number_to_skip) in range(1,50):
            for i in range(1,50):
                    if i % 2 != 0:
                        if i == int(odd_number_to_skip):
                            print('Yikes! Skipping number: {}' .format(odd_number_to_skip))
                        else:
                            print('Here is an odd number: {}' .format(i))
            break

    power_user_var = input("Would you like to choose another number? (y/n): ")
    if power_user_var.lower() == 'y':
        continue
    else:
        print("This was fun!")
        break

# * The ```input``` function can be used to prompt for input and use that
#  input in your python code. Prompt the user to enter a positive
#  number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a
#  valid number, also note that the ```input``` function returns
#  a string, so you'll need to convert this to a numeric type.)

while True:
    input_positive_number = input("Pick a positive number ")
    i = 0

    while input_positive_number.isdigit() == False or int(input_positive_number) < 0:
        input_positive_number = input("Pick a positive number ")

    while input_positive_number.isdigit() == True and i <= int(input_positive_number):
        print(i)
        i += 1
        
    user_power = input("Would you like to give it another go? (y/n): ")
    if user_power.lower() == 'y':
        continue
    else:
        print('It was nice counting for you!')
        break

# * Write a program that prompts the user for a positive integer.
#  Next write a loop that prints out the numbers from the number the
#  user entered down to 1.

while True:
    input_negative_number = input("Pick a positive number ")
        
    i = input_negative_number

    while input_negative_number.isdigit() == False or int(input_negative_number) < 0:
        input_negative_number = input("Pick a positive number ")

    while input_negative_number.isdigit() == True and int(i) > 0:
        i = int(i)
        print(i)
        i -= 1
    
    continue_variable = input("Would you like to do it again? (y/n): ")
    if continue_variable.lower() == 'y':
        continue
    else:
        print("It was a pleasure counting for you!")
        break
    

### Fizzbuzz

# One of the most common interview questions for entry-level programmers is 
# the FizzBuzz test. Developed by Imran Ghory, the test is designed
#  to test basic looping and conditional logic skills.

# * Write a program that prints the numbers from 1 to 100.
# * For multiples of three print "Fizz" instead of the number
# * For the multiples of five print "Buzz".
# * For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,101):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

### Display a table of powers

# * Prompt the user to enter an integer.
# * Display a table of squares and cubes from 1 to the value entered.
# * Ask if the user wants to continue.
# * Assume that the user will enter valid data.
# * Only continue if the user agrees to.

input_number = int(input("What number would you like to go up to? "))

print("Number| Squared | Cubed")
for i in range(1, input_number + 1):
    print(f"{i + 1}     | {i ** 2}     |    {i ** 3}")

    
# Bonus:

 while True:
    user_power_request = 0
    while True:
        user_power_request = input("What number would you like to go up to? ")
        if not user_power_request.isdigit():
            continue
        
        user_power_request = int(user_power_request)
        break
    print("number | squared | cubed ")
    print("------ | ------- | ------ ")
    for n in range(1, user_power_request + 1):
        print(("{:<7}|{:<9}|{:<8}").format(n, n ** 2, n ** 3))
    
    user_continue = input("Do you want to continue (y/n)? ")
    if user_continue.lower() == "y":
        continue
    else:
        break

### Convert given number grades into letter grades

# * Prompt the user for a numerical grade from 0 to 100.
# * Display the corresponding letter grade.
# * Prompt the user to continue.
# * Assume that the user will enter valid integers for the grades.
# * The application should only continue if the user agrees to.

# >Grade Ranges:

# >A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0   

while True:

    grades = int(input("Please pick a number between 0 and 100 : "))

    while type(grades) == int:
        if grades in range(88,100):
            print(f"{grades} is an A, good job!")
            break
        elif grades in range(80,87):
            print(f"{grades} is a B")
            break
        elif grades in range(67, 79):
            print(f"{grades} is a C")
            break
        elif grades in range(60, 67):
            print(f"{grades} is a D")
            break
        elif grades in range(0,59):
            print(f"{grades} is an F, you Fail")
            break
    
    continue_var = input("Would you like to continue? (y/n) ")
    if continue_var.lower() == 'y':
        continue
    else:
        print("Goodbye")
        break
        

        
#  Create a list of dictionaries where each dictionary represents a book
#  that you have read. Each dictionary in the list should have the keys
#  title, author, and genre. Loop through the list and print out
#  information about each book.

# * Prompt the user to enter a genre, then loop through your books list and
#  print out the titles of all the books in that genre.   

books = [
    {
        "title": "Enders Game",
        "author": "Carl Orson Scott",
        "genre": "Science Fiction"
    },
     {
        "title": "Genetic Algorithms and Machine Learning for Programmers",
        "genre": "Education",
        "author": "Frances Buontempo"
    },
    {
        "title": "The Visual Display of Quantitative Information",
        "genre": "Education",
        "author": "Edward Tufte"
    },
    {
        "title": "Practical Object-Oriented Design",
        "author": "Sandi Metz",
        "genre": "Education"
    },
    {
        "title": "Weapons of Math Destruction",
        "author": "Cathy O'Neil",
        "genre": "Eduction"
    },
    {
         "title": "Harry Potter and the Philosophers Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy"
    },
     {
         "title": "Harry Potter and the goblet of fire",
        "author": "J.K. Rowling",
        "genre": "Fantasy"
    },
     {
         "title": "Ride of a lifetine",
        "author": "Bob Iger",
        "genre": "Non-Fiction"
    },
    {
         "title": "Snowball",
        "author": "Warren Buffet",
        "genre": "Non-Fiction"
    }
    
]

# Loop to run through all book titles
for book in books:
    print(f"'{book['title']}' by '{book['author']}' is about '{book['genre']}'")

# Query to ask for input and return titles based on genre selected by user
while True:
    genre_input = input("Pick a genre : ")
    if genre_input.title() in [book['genre'] for book in books]:
        book_titles = [book["title"] for book in books if book["genre"].lower() == genre_input.lower()]
        print(*book_titles, sep = "\n")
    else:
        print(f"Sorry, there are no books about {genre_input}")
    promp = input("Would you like to pick a different genre? (y/n) :")

    if promp.lower() == 'y':
        continue 
    else:
        print("Have a nice day!")
        break