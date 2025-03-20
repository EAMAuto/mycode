# So far we have only seen python raise exceptions for us
# But what if we want to raise exceptions by ourselves?
# There are two ways to do that, and for the exam you will only need to know one of the ways...Assertions
# # # # What are Assertions? # # # #
# Assertions are certain assumptions in our program that should always be true
# Take a look at the following program:
def calculate_inverse(number):
    assert (number != 0), 'Got 0 as number!'
    return 1/number

#This simple function uses a new keyword assert
# After this keyword, we put one or more conditions inside round brackets
 # These are conditions that we assume should always be true for this specific function
 # If the condition or conditions are true then Python simply moves to the next line
 # If the condition is not true then python shows an error that we specify after a comma
 # Let us see this in practice:
 # If we provide an input of 5 for our function to calculate as shown below then the function works exactly as intended and does the calculation:
calcluate_inverse(5)
 #output:
 0.2
 # if we provide an incorrect input such as 0, we are thrown an AssertionError:
 calculate_inverse(0)
 #output:
AssertionError: Got 0 as a number!

# above we are observing a new exception which has appeared, an AssertionError exception
# whenever we use the assert keyword and the condition provided with in the brackets is not satisfied an AssertionError will always be the kind of exception that is raised

# assertions are a simple concept, but we need to understand when and when no to use them
# we typically only use assertions for 1 of 2 reasons:
# 1. For debugging/ Testing our code
# 2. For documenting your code

# # # # DO NOT # # # #
# 1. Validate user input with assertions
# 2. Handle AssertionErrors in try...except blocks

# you can also use assertion as sanity checks at the beginning of a function to make sure that is recieves the correct data 
# Assertions are also sometimes used to document your code
# This way you can communicate to other developers what you expect in your functions 
# On the other hand, you should not use assertions for validating user input, this is because it is impossible to turn assertions off when you publish a program to your users
# Turning off assertions in this case would mean that you lose all the code that validates user input
# Apart from that, assertions are not an error handling tool
# the purpose of assertions is to notify you about bugs during development, so you can catch and fix bugs quickly, because of that you should not write code that handles assertion errors using try except assertion error blocks
