# You already know how to create a variable with a list inside such as this:
number = [1, 2, 3, 4]

# Now imagine you need to create a really long list
# lets say we want to have a list with numbes from 1 to 100, you could manually type all of this yourself but it would require a lot of time and space
# Alternatively, you could think of using a loop the following way

number = []
for i in range(1, 101)
    numbers.append(i)
print(numbers)
# The out put for the following would be the new list known as numbers now appended with numbers 1-100 as individual elements

# This certainly does the job, but it takes alot of space.
# Turns out that python has a unique feature designed to speed up this process of creating a list 

# The feature is called list comprehension :
numbers = [i for i in range(1, 101))
print(numbers)

# This code above creates the exact same list for us but it only takes one line of code to create 
# It's almost as if we moved the loop into the square brackets of the list 
# Note that we had to add the control variable name in front of the loop 
# Note that we had to add the control variable name in front of the loop 
# Remember about this because otherwise you'll see the following error invalid syntax 

# List comprehensions can be even ore complicated than this
# Imagine we want to generate the same list from 1 -100 but this time we want to exclude numbers divisible by 3

numbers = [i for i in range(1, 101)if i % 3 != 0)
print(numbers)
# Note how short the syntax is for list comprehension
# No newline character, indentations, everything is done on a single line 
# Short and sweet
# So we may think of a list comprehension as an actual list which is created on the fly when you run python programs 
# List comprehensions are not necessary in programming, and many programming languages don't have them but its a nice shortcut in python that many developers use in their everyday work 
