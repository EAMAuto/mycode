#We've seen nested if statements and we have seen nested loops so it probably wont come as a surprise that python offers nested loops
#List in general are collections of multiple elements 
# For example you can have a list with integer values like below:
numbers = [1, 2, 3, 4]
# By the same token you could have strings instead of integers like below:
countries = ['UK', 'US', 'Germany']
# Python even allows you to mix multiple data types within a single list:
countries = [1, 'UK', 2, 'UK']
# Note that though this is possible it should be avoided, All the elements of a list should have the same data type
# It turns out that lists can have other lists as elements
cells = [['A1','A2','A3' ],['B1', 'B2', 'B3']]
# The outer list name 'cells' contains two elements inside. The first element is a list with three strings inside A1,A2,A3. The second element is another list with three strings inside B1,B2,B3
# Now id you want to access the first element with index zero, you'll see that you get a sub-list in return
cells[0] -> ['A1', 'A2', 'A3'] 
# Now if you want to access a specific element in this sub-list all you have to do is add another index
# For example:
cells[0][0] -> 'A1'
# the first index refers to the element in the outer list the second index refers to the element in the sub-list

# Now lets see what happens when we use a for loop to iterate the list and print its elements 
cells = [['A1','A2','A3' ],['B1', 'B2', 'B3']]
for x in cells:
    print('Element:', x)
#Output:
Element: ['A1','A2','A3' ]
Element: ['B1', 'B2', 'B3']

# The cells list contains just two elements and each of them is a list itself that we print to the output 
# But what if we want to access the individual string elements inside the sublists? in this cse we want to use nested for loops as seen below;
cells = [['A1','A2','A3' ],['B1', 'B2', 'B3']]
for x in cells:
    for y in x:
        print('Element:', y)
#Output:
Element: A1
Element: A2
Element: A3
Element: B1
Element: B2
Element: B3

# Because x itself is a list, we can use a for loop again to get individual items in this sublist

# # # Why do we use nested lists? # # #
# Nested lists or multidimensional lists, are used quite frequently in programming
# They are used to represent multidimensional objects like tables
# if you take a look at our cells variable you may notice that it resembles an excel spreadsheet
# You may think of the lists as rows and the individual items as excel cells
# The common practice when wanting to view individual pieces of the sublists is to give the following instruction:
table = [['A1','A2','A3' ],['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print('Element:', cell)
#Output:
Element: A1
Element: A2
Element: A3
Element: B1
Element: B2
Element: B3
# We can also print the elements in such a way that they do resemble a table
table = [['A1','A2','A3' ],['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()
#output:
A1 A2 A3
B1 B2 B3

# You can also use nested list comprehensions to initialize a multidimensional list
# for example lets say we want to create a list to represent the following table:
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
table = [i for i in range(1,6)]
print(table)
#Output:
[1, 2, 3, 4, 5]

# Now we want to create a list which inside contains four such lists with numbers 1 to 5 for this we will need an extra pair of square brackets and some more code 
table = [[i for i in range(1,6)] for j in range (4)]
print(table)
# output:
[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
# Note that the inner list comprehension uses the i control variable value before the for loop 
# In the outer list comprehension however we put the inner list comprehension 











