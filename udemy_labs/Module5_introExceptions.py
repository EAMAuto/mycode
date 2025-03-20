# # # Introduction to exceptions # # #
# It is extremely difficult to write computer programs that never fail and contain no errors
# So we sometimes end up seeing nasty error message when working with python
# One of the most popular errors is the syntax error
# this error is seen when you make a mistake in the syntax of your program for example, When you forget to indent code
# For example
if True:
print('hooray')
#output:
File <insert file path here>, line on which error is occuring
    instruction which is incorrect
    Errortype: error FAIL_REASON
# When you see an error, there are a few interesting pieces of information
# You can see the line that produced the error
# You can see the name of the error
# And you can see a descriptive message which will help you find out what is actually wrong about your program
# You will usually see the syntax error generators early on when you try to run your program
# Syntax errors are usually quite easy to identify and fix
# They shouldn't come to you as a surprise, and they always mean that you made a mistake in your code and didn't comply with the python language rules 
# An already made python program should not contain any syntax errors at all
#However sometimes there are errors generated through no fault of your own
# For instance you may aska  user to provide a number and they provide something else instead, in such situations you will see a different kind of error
# Here is an example:
# The code below is meant to ask a user for and integer and tries to compute the inverse of the integer
value = int(input('Enter an integer'))
print('The inverse of', value, 'is', 1/value)
# Now if we dont put and integer and instead provide the letter a for example you recieve the following error:
ValueError: invalid literal for int() with base 10: 'a'
# This is a value error meaning our program is syntactically correct, its just that our user provided an incorrect or non accepted value
# formally speaking, both syntax errors and value errors are exceptions
# You may think of exceptions as just any kind of errors that python generates, but a more formal definition is as follows:
# An exception is an event which occurs during the execution of a program that disrupts the normal flow

# When we ask a user to provide a number and they do provide a number this is known as the normal flow 

# We get a number from our user, so we may continue with the normal execution of our program

# However when the user provides something different than a number, it is an unwanted event basically we got something we didnt expect
# By default, python doesn't know what to do in such situation 
# SO it raises an exception and stops the program 
# In many cases, exceptions are not the end of the world 
# There are many situations where you can somehow handle the exception and react to it so that the program execution continues normally
# To handle exceptions, we need to use a new special kind of structure which is called try except as shown below:
try:
    value = int(input('Enter an integer'))
    print('The inverse of', value, 'is', 1/value)
except:
    print('You did not provide a number, so i will not calculate the inverse')
# In the code shown above we introduced a new keyword 'try', followed by a colon and then an indented block of code
# This is the place where we put code that we expect could be risky and could raise an exception
# In this specific case, we expect that the user could enter a word instead of a number and python would know what to do about it 
# We then enter another new keyword 'except' we then put another colon after the keyword and below it another indented line of code containing how to handle the exception
# Keep in mind that the code placed in between try and except is executed in a very special and the exception which occurs here will not terminate the program execution
# Now if you take a look at our program, you will see that there is more than one thing that can go wrong
# We already know that the user may try to provide something that is not a number
# This was alreadu covered in our appect block, but what happens if the user provides a number but it is a 0 
# well python would try to divide by 0 but dividing by 0 is not possible 
# So python will raise an exception 
# the problem is this is a different type of exception 
# As the code is now it will provide the same error message You did not provide a number, so i will not calculate the inverse which in the case of providing a 0 is not  accurate 
# A number was provided but just that 0 is a special case and cannot be used
# Ideally we would like to provide a different error message when we get a 0 but how do we do that?
# Firstly, we need to note down the specific names of the exceptions thrown when the user provides something other than a number and when the user provides 0 
# So for anything other than a number we already know we will get a value error 
# For when a user provides a 0 the error is called a ZeroDivision error 
# Fortunately, we cann expand out try except construction to distinguish between these two situations as shown below:
try:
    value = int(input('Enter an integer'))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a number, so i will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible, sorry')
# here we have provided a second except branch and have specified the name of the exception 
# In this case, each oof the expected exceptions has its own way of handling the error 
# But it must be emphasized that only one of all the branches can intercept control 
# If one of the branches executes it, all the other branches remain unused
# The number of accepted branches is not limited 
# You can specify as many of them as you need, but don't forget that none of the exceptions can be specified more than once 
# Now we have specified two exceptions and created ways for the code to interact with those exceptions and let the user know what is going on 
# The question that remains is what if we forget to add an exception scenario to our code, what will happen if an exception we did not account for happens?
# Fortunately, we can protect ourselves from such situation in a final except block
# We can add a general except block with no specific exception name as shown below:
try:
    value = int(input('Enter an integer'))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a number, so i will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible, sorry')
except:
    print('Something strange happened here, sorry')
# Now the program works in the following way 
# If a ValueError is raised we will see you did not provide a number, so i will not calculate the inverse
# If a ZeroDivisionError is raised we will see You provided 0 and division by 0 is not possible, sorry
# If any other type of exception is raised we will see Something strange happened here, sorry

# # # # # # # # A big EXCEPTION to this entire lesson on EXCEPTIONS is the SyntaxError, when trying to combat these in your code it is always best to explicitly list them in an except block as the general except block will not work against SyntaxErrors # # # # # # # # 


































