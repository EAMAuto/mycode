# The second type of loop in python is the for loop
# In some situations you can convert a while loop into a for loop or the other way around 
# For loops are typically used in other situations than while loops

# In python we typically use for loops to go through all the elements in a specific sequence

# Sequences in python are special data structures that can store more than one value and can be browsed sequentially meaning element by element 

# one sequence type we already know of are strings
# a string in pythono is a special sequence type that can be used to store multiple characters in it 
# When you have a string such as 'Hello!' internally you have a sequence of character H e l l o !

# The for loop allows us to scan all elements of any sequence type
# For example we canbrowse all letter in a string

for letter in 'hello!':
    print('current letter:', letter)

# The loops starts with the keyword for
# no conditions like while loops 
# Condtitions are checked for you internally
# after the keyword we define the name of the so-called control variable
# for this example we chose letter but you can change it to any valid variable name
# Python will automatically assign the letters from the string to this variable one by one 
# Again you dont have to think about incrementing counter or anything like this, This is done automatically for you
# Then we have the keyword in which is used to introduce the range of possible values or the sequence
# In this case we are instructing python to scan all the character of the string 'hello!'
# each time we enter the loop body python will automatically assign another character as the value of the control variable
# So the first time we enter the loop body letter will have the value of h
# The second time we enter the loop body letter will have the value of e
# and so on
#python knows when the sequence ends so it knows when to exit the loop
# When we talk about for loops, we often use the term iterating, scanning or browsing a sequence is often called iterating a sequence and entering a loops body once is called iteration
# for this example there are 6 iterations

counter = 1
while counter < 11:
    print(counter)
    counter += 1
print('Finished!')

# The above and below are programs that achieve the same end goal one using a while loop and one using a for loop 
#Lets understand how

for counter in range (1,11):
    print(counter)
print('Finished!')

#you can see that in the for loop example we use less code
# In the for loop we needed to introduce a new function to achieve the same goal as the while loop named range()
# The range() function is a very special function which generates all the desired integer values for our controlled variable
# The first arguement number one here is the start value or the first integer value to generate
# The second argument 11 is the stop value, which is the value at which our sequence generation will end
# NOTE that the start value is inclusive in the sequence, but the stop value is exclusive
# This means that when we define 11 as the stop value, the last value that we will get will be 10


# Ther are as many as 3 versions of the range() function
# 1. If you just provide a single number within the range function this value will be treated as the stop value and the default start value of 0 will be used, and each each generated value will be increased by 1 which is the default increase value 
# 2. if you provide 2 numbers, then you have the start and stop value we saw before.
# 3. If you provide 3 numbers in which case the last argument will be the increase amount 
