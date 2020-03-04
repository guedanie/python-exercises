# Exercises for Numpy

import numpy as np

# Following array for questions: 

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#Q1: How many negative numbers are there? 4
negative_n = a < 0
sum(negative_n)

#Q2: How many positve numbers are there? 5, not counting the zeros
positive_n = sum(a > 0)

#Q3: How many even positive numbers are there?  3
even_positive = len(a[(a > 0) & (a % 2 == 0)])

#Q4: If you were to add 3 to each data point, how many positive numbers 10
array_plus_three = a + 3
positve_n = sum(array_plus_three > 0)

#Q5: If you squared each number, what would the new mean and standard deviation be?
sqr_array = a ** 2
sqr_array.mean() # = 74.0
sqr_array.std() # = 144.02

#Q6: A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the center of the data is at 0. 
# This is done by subtracting the mean from each data point. 
# Center the data set.

centered_array = a - a.mean()

#Q7: Calculate the z-score for each data point. 

z_score = (a - a.mean()) / a.std()

## Numpy_exercises_part_1

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of 
# all the numbers in above list

sum_of_a = sum(a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of 
# all the numbers in
#  the above list

min_of_a = min(a)

# Exercise 3 - Make a variable 
# named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)

# Exercise 4 - Make a variable named mean_of_a to hold the average 
# of all the numbers in the above list

mean_of_a = sum(a)/ len(a)

# Exercise 5 - Make a variable named product_of_a to hold the 
# product of multiplying all the numbers in the above list together

product_of_a = [x * x for x in a]

# Exercise 6 - Make a variable named squares_of_a. 
# It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = [x ** 2 for x in a]

# Exercise 7 - Make a variable named odds_in_a. 
# It should hold only the odd numbers

odds_in_a = [x for x in a if x % 2 != 0]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = [x for x in a if x % 2 ==0]

## What about life in two dimensions? A list of lists is matrix, a table, 
# a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, 
# sum, product, and list of squares for this list of two lists.

b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, 
# you'll first need to make sure that the "b" variable is a numpy array**
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)

b_np = np.array(b)

b_np.sum() # = 33

# Exercise 2 - refactor the following to use numpy. 
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
# min_of_b is assigned the smallest value, unless there is a tie, in which case the
# we store the second occurence of that min value

b_np.min()

# Exercise 3 - refactor the following maximum calculation to find 
# the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

b_np.max()

# Exercise 4 - refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

b_np.mean()

# Exercise 5 - refactor the following to use numpy for calculating the product of 
# all numbers multiplied together.
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number

b_np.prod()

# Exercise 6 - refactor the following to use numpy to find the list of squares 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)

sqr_array = b_np ** 2

# Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)

odds_in_b_np = b_np[b_np % 2 != 0]

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)

evens_in_b_np = b_np[b_np % 2 == 0]

# Exercise 9 - print out the shape of the array b.
# how to count number of elements in a 1D, 2D & 3D Numpy array, also how to count number of rows & columns of a 2D numpy array and number of elements per axis in 3D numpy array.
# https://thispointer.com/how-to-get-numpy-array-dimensions-using-numpy-ndarray-shape-numpy-ndarray-size-in-python/

b_np.shape

# Exercise 10 - transpose the array b.
# The transpose of a matrix is obtained by moving the rows data to the column and columns data to the rows.
# https://www.journaldev.com/32984/numpy-matrix-transpose-array

print(b_np.T)

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

print(b_np.reshape(1,6))

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

print(b_np.reshape(6,1))

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c_np = np.array(c)

# Exercise 1 - Find the min, max, sum, and product of c.

c_np.min()

c_np.max()

c_np.sum()

c_np.prod()

# Exercise 2 - Determine the standard deviation of c.

c_np.std()

# Exercise 3 - Determine the variance of c.

c_np.var()

# Exercise 4 - Print out the shape of the array c

c_np.shape

# Exercise 5 - Transpose c and print out transposed result.

print(c_np.T)

# Exercise 6 - Get the dot product of the array c with c. 

c_np.dot(c)

# Exercise 7 - Write the code necessary to sum up the 
# result of c times c transposed. Answer should be 261

c_s = (c_np * (c_np.T)).sum()

# Exercise 8 - Write the code necessary to determine the product of
#  c times c transposed. Answer should be 131681894400.

c_p = (c_np * (c_np.T)).prod()

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d_np = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d

np.sin(d_np)

# Exercise 2 - Find the cosine of all the numbers in d

np.cos(d_np)

# Exercise 3 - Find the tangent of all the numbers in d

np.tan(d_np)

# Exercise 4 - Find all the negative numbers in d

neg_d = d_np[d_np < 0]

# Exercise 5 - Find all the positive numbers in d

pos_d = d_np[d_np > 0]

# Exercise 6 - Return an array of only the unique numbers in d.

unique_n = np.unique(d_np)

# Exercise 7 - Determine how many unique numbers there are in d.

len(unique_n) # = 11

# Exercise 8 - Print out the shape of d.

d_np.shape

# Exercise 9 - Transpose and then print out the shape of d.

print(d_np.T)

# Exercise 10 - Reshape d into an array of 9 x 2

d_np.reshape(9, 2)