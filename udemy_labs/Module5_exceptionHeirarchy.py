# We have already learned about exceptions in python Now we will talk about the exception hierarchy in python
# Python has over 60 built-in exception types
# Naturally, you dont need to memorize them all as a beginner, but its good to have a general understanding of their heirarchy
# Let us examin a chart of exeptions:
# BaseException
    #
    #
    # # # # # # Exception # # # # # # SystemExit # # # # # # KeyboardInterupt ***
                    #
                    #
                    # # # # ArithmeticError # # # # # # LookupError # # # # # # TypeError # # # # # # ValueError ***
                                #                            #
                                #                            #
                                # ZeroDivisionError          # IndexError
 #                                      ***                  #
                                                             #
                                                             # KeyError
# *** Only shows selected exception types

# At the top of the hierarchy theres is BaseException, this exception is used internally by python and you will probably never see it raised in your own programs
# The BaseException serves more as a template for other more specific exception types
# Such templates that are not very specific concrete exceptions are typically called abstract or obstructive exceptions
# One level down in the hierarchy you can see three exceptions, Exception which has many other exceptions underneath , & two others SystemExit & KeyboardInterupt 
# SystemExit is an exception that is raised when we call a special method system exit
# The method is used to terminate or in other words close your program, up until now our programs have closed on their own when they reached and executed the last liine of code
# This exit allows you to close your program manually, it is not used very often, but may sometimes come in handy in a very specific situations
# take a look at this short program:
import sys

user_name = input('What is your name? ')
if user_name == '':
    print('Empty name? i cannot work with that. I am closing the program. Bye!')
    sys.exit()
print('Hello', user_name)
print('Let us get started...')
# In the program above we are checking user input if the user provides an empty name, we use the this to exit the program.
#Note that in order to use this exit, we need to import a special python module named sys
#Importing modules is outside of the scope of this video, Just keep in mind that this line is necessary for a sys.exit to work 

# Next lets go over KeyboardInterupt
# This simple exception is raised when the user presses a key combination that causes an interrupt to the excuting script 
# For example, in jupyter notebook you can use the stop kernel button to see that exception

#Exception is a bit similar to BaseException 
# Both of them often serve as tempalates for other exceptions 
# The difference is that BaseException is typically only used as a template for internal python exceptions, WHile Exception can also be used as a template for your own exceptions 
# In this course we will not create our own exception types as this is a more complex concept and is not needed for your beginner exam
# Exception is also a template for many built in python exceptions 
# In fact all mmost of the exceptions that we have seen so far such as ZeroDicisionError, ValueError and so on, can be found under the Exception hierarchy
# For instance the ArithmeticError we see i nthe diagram under Exception hierarchy is a base class of a variety of mathematical arithmetic errors and under this ArithmeticError base class you can see ZeroDivision which we run into when we try to divide by 0
#there are also other exceptions under this category as you can see in the diagram above

# the LookupError has two children underneath IndexError and KeyError
# These two exceptions will appear when you work with collections such as lists or dictionaries
# IndexError occurs when you try to access an element in a list or dictionary that doesnt exist
# Key errors occur when you work with dictionaries as shown below:
ages = {'Jim' : 30, 'Pam' : 28, 'Kevin' : 33}
ages = ['michael']
# The above block of code is a dictionary which contains 3 indivduals with 3 different ages
# We are trying to access the age of individual that is not in the dictionary and therefore does not exist and because of this we get a Key Error

# Type error occurs when the type of data your trying to use is not correct in the given context
# For example:
age = input('What is your age? ')
print('In 10 years, you will be', age + 10)
# In the case shown above we know that the input function can only return strings and not integers, so when we type an age in the program will try to add 10 to a string which will not work result in the following error
TypeError : can only concatenate str(no 'int') to str

# A ValueError is raised when a function or method recieves an argument that is of the correct type but with an actual value that is invalid for some reason
#For example:
age = int(input('What is your age? '))
# If for this program we provide something like an a instead of a number we will get the following error:
ValueError: invalid literal for int() with base 10: 'a'

# So the difference between the TypeError and the ValueError is that here we use incorrect variable types such as adding a string to an integer or using a string which is expected but the content is not correct


# # # # One thing to keep in mind is that Python will always throw us the most specific exception error possible, for example if you try to divide by 0 you will not receive a general arithmetic error you will always see a ZeroDivision Error because it is placed lower in the hierarchy # # # #























