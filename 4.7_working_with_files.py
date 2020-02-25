# 4.7_working_with_files
#Q1 Read the contents of your last exercise file into a variable.

with open('function_exercises.py') as f:
    file_contents = f.read()
    file_content_with_lines = f.readlines()

    # Print out every line in the file

    print(file_contents)

    # Print out every line in the file, but add a line numbers

with open('function_exercises.py') as f:
    for cnt, line in enumerate(f, start=1):
        print("[{}]: {}". format(cnt, line))

#Write some python code to create a grocery list.

    # Create a variable named grocery_list. It should be a list, 
    # and the elements in the list should be a least 3 things that you 
    # need to buy from the grocery store.

grocery_list = ['bananas', 'bread', 'ice cream', 'oats', 'beer', 'milk', 'chocolate']


    # Create a function named make_grocery_list. When run, this 
    # function should write the contents of the grocery_list variable 
    # to a file named my_grocery_list.txt.

def make_grocery_list(list):
    string = ','.join(list)
    with open('my_grocery_list.txt', 'a') as f:
        for item in grocery_list:
            f.write(string + '\n')

    # Create a function named show_grocery_list. When run, it should 
    # read the items from the text file and show each item on the grocery 
    # list.

def show_grocery_list(text_file):
    with open(text_file) as f:
        print(f.read().split(','))

    # Create a function named buy_item. It should accept the name of an 
    # item on the grocery list, and remove that item from the list.

def buy_item(name):
    groceries_remove = grocery_list
    with open('my_grocery_list.txt', 'a') as f:
        if name in groceries_remove:
            groceries_remove.remove(name)
            groceries_remove = ','.join(groceries_remove)
            with open('my_grocery_list.txt', 'w') as f:
                f.write(groceries_remove)

    ## What if we need to add new items, to an existing list?

def add_item(name):
    with open("my_grocery_list.txt", 'a') as f:
        f.write(f',{name}')