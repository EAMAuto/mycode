# In this lab we are going to learn how to add a new element to an existing list
# To that end we will need to understand what methods are
# In general, we can say that functions in python dont belong to anything
# They can get some data from you in the form of arguments
# When you use a function such as print('hello') you provide the data to be consumed by the function and then shown to the output 
#but the date you provide is not related to the print function in any way

# Functions can also give you some data back when you use the input function like this 
# It will give you the data that your user enters, but again when you get the data the input function no longer has any control over the data 
# Now methods are a specific kind of functions 
# You could say that a method is owned by the data it works for
# methods exist alongside the data they belong to 

#Here is an example:
# Here we have a list of integers
book_ratings = [7, 9, 5, 6, 8] # Here are some ratings for a book on a scale from 0 to 10
# Lets say another person has read the book and wants to give a new rating of four 
# To that end we'll use a method named append
book_ratings.append(4) # Adds the integer to the list with append method 
print(book_ratings) -> book_ratings = [7, 9, 5, 6, 8, 4]
# append is a method it belongs to the book ratings list
# You can see that a method is invoked using its name and a pair of brackets with arguments inside
# But unlike normal functions, methods are invoked with a dot after the data they work on 
# In other words, you could not call append like print or input
# If you tried the following you would get an error: append(4) , This is because there is no function named append and Python wouldn't know what to do with the value.
# On the other hand, there is a method named append 
# We invoke the method on our specific list
#We provide the name of the list with a dot (.) and then provide the method name and the arguments inside the parenthesis 
# And now python knows that you are trying to use a method named append which belongs to the list name book_ratings 
# It is important to understand that without the list there is no method named append

# # # # Methods are functions that 'belong' to specific data # # # #

# By just using the append method we append our changes to the list to the very end of the list 
# There is also another method which can be used to add an element to other places in the list 
# we will begin with the initial value of the book_ratings list
book_ratings = [7, 9, 5, 6, 8]
# We would like to insert a new rating  of 10 to the index 1 place (2nd element) of the list and to do this we will use the .insert method
book_rating.insert(1, 10)
print(book_ratings) -> [7, 10, 9, 5, 6, 8]
# This method invocation adds the value of ten which is the second argument to index one which is the first argument. All the values that were previously in the list have been shifted tothe right to make space for the new value. Meaning that as 9 was previousl in the 2nd element and index position number one it is now in the 3rd element and in index position number two

