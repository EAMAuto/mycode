# This lesson will be going over how we can return a meaningful value from our own function
from builtins import True, False
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers: 
        sum += number
    average = sum / len(input_numbers)
    print(average)
    
# This function which is used to get the average from a list of numbers does not return anything meaningful, behind the scenes it returns a null or none 
# previously we only focused on the effect of the function which was to print the average value to the output
# It isnt typically common practice to create a function whose purpose is to print anything to the console
# we typically write functions that return a value instead of showing it to the output 
# We will modify the following piece of code above for this purpose:
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers: 
        sum += number
    average = sum / len(input_numbers)
    return average
# All we have to do is change the our last instruction which was printing the average to the following return average
# We don't use brackets around the keyword return because return id not a function 
# Our function no longer prints the average to the output or in general, it doesn't cause any effect
# It now instead returns a meaningful value, But in the code we don't do anything with the value we simply ignore it
# Let us explore how we can change this:
# The most obvious thing we can do is print the return value to the output:
print('The average is', get_average([5.0, 3.5, 7.8, 9.9, 10.0]))
# Here we have the print invocation and inside the brackets 'The average is" & then the result of the call
# We can also save the return value in a variable and then later use it in our code somehow 
# For example look at the following piece of code:
average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
if average > 5.0:
    print('The average is too high')
# In the piece of code above we store the result from get_average in the average variable and then if average is greater then 5 print the average is too high 
# The keyword return actually does 2 things at the same time 
# It gives the result as you could see, but it also immediately exits the function 
# This means that any instruction after the return statement will be ignored 
# Here we have a modified version of the get_average function with an additional print invocation after their return statement 
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers: 
        sum += number
    average = sum / len(input_numbers)
    return average
    print('Show me')

get_average([2])
#output:
2.0

# You can see here that even though we included the print('show me') function 'Show me" was not printed to the screen 
# the function execution was terminated before it could reach this instruction
# This feature is sometimes used when we want to exit a function without returning anything meaningful
# all we have to do is use the keyword return alone without any expression or value
# Let us explore another function, below we have a function that checks whether the first and last elements in the list are equal:
def is_first_last_equal(number_list):
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False
# If they are we return True, If they aren't we return False
# For example if we input the following:
print(is_first_last-equal)([10,20,30,40,10])
#ouput: 
True
# But if we input 
print(is_first_last-equal)([10,20,30,40,50])
#Output:
False
# Now if we pass an empty list as the argument we get an index error

# We can however modify the function:
def is_first_last_equal(number_list):
    iflen(number_list)== 0:
    return
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False
# Above we have modified the function by introducing a new line of code which basically states if the length of the number_list we provide is 0 immediately return(or exit) from the function
# What this will do is instead of throwing an error if an empty list is provided it will return a null character or 'None'































