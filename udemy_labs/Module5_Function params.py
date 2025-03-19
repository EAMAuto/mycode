# In this lesson we will discuss parameters which are various values that we pass to a function
# Lets say we need to find the average from multiple numbers in a list:
input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]
sum = 0.0
for number in input_numbers: 
    sum += number
average = sum / len(input_numbers)

print(average)
#Output :
7.24

# Now we want to turn this code into a function
# In order to do that we must add the def keyword to define the function we would like to create:

input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers: 
        sum += number
    average = sum / len(input_numbers)
    print(average)
    
#Note that a new element appeared in the round brackets after the function name, this is the parameter
# A parameter is actually a special kind of variable 
#A parameter can only be defined inside the pair of square brackets after the function name, and it only exists inside the given function
# In our example above we defined a single parameter named input_numbers
# We later on iterate the parameter and sum its elements
# Now we may be wondering what is the value of the parameter inside the function?
# We never assign a value to this parameter and yet we iterate over it
# We assign the value to a parameter when we invoke the function 
# Here we create a function with a single parameter, and the code of the function sums all the numbers from the parameter
# Now our job elsewhere in the code is to call or invoke the function and provide it with a value for this parameter
# So now we can do the following;

input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers: 
        sum += number
    average = sum / len(input_numbers)
    print(average)
    
get_average9[5.0, 3.5, 7.8, 9.9, 10.0])

# Output:
7.24
# So this value, the list assigned to the parameter input numbers and the function sums all the values in the list passed
# Incidentally when you pass a value like this during a function call, this is called and argument
# We can say that we call the function get_average with this argument and the value of the argument is assigned to the parameter input numbers
# These two words are sometimes confused people sometimes call parameters, arguments and vice versa
# When you invoke a function, you must provide all of its arguments
# If you try something like this you will get an error:
get_avergae()

# You must also make sure that you pass the correct type of value 
# In this example we were expecting a collection, such as a list or a tuple with numbers inside 
# If you pass something else then python will show an error too:
get_average(5)
# This will also through an error

# naturally, you can also define functions with more than one parameter
#Lets create a simple example of a function that takes tow parameters
# Now we'll have a function that takes a string and a letter and counts the number of times the letter appears in the string:
def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter;
            counter += 1
    print('Number of', letter, 'is', counter)
# You can see that we now have two parameters within the round brackets, sperated by a comma
# Now when you invoke a function somewhere in your code you need to provide both of them
#Take a look:
print_letter_count('welcome', 'e')
#Output:
Number of e is 2
print_letter_count('People say nothing is impossible, but i do nothing every day.', 'a')
#Ouput:
number of a is 2

# NOte that the order of arguments is important in our function definition 
# We first expect the parameter with the text or the string and then with the letter
# So if you confuse the order and provide the letter first, you function will not work correctly:
print_letter_count('e', 'welcome')
# Output:
Number of welcome is 0
# This is not what we want this function to do 
# Because the order of arguments is important here we call them positional arguments
# the argument values are assigned to the parameters based on the position
# So the value of the first argument will be assigned to the first parameter, the value of the second argument to the second parameter and so on
# Positional arguments are the most frequently used type of arguments, not only in python but in most programming languages in general

# Python also allows you to provide named arguments also known as keyword arguments
# Take a look at the following invocation;
print_letter_count(text = 'welcome', letter = 'e')
#output;
Number of e is 2
# Here we used the parameter name with the equals operator to specify which value should go to which parameter 
# Now that we used named arguments, we can swap the places and the function call will still work:
print_letter_count(letter = 'e', text = 'welcome')
# Output;
Number of e is 2










