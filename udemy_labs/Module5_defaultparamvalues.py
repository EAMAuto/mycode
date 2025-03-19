# In module 2 we introduced the sep and end parameters of the print function like this:
print('Hello', 'How are you?', end='.', sep'-')

# we then said that end and sep are keyword arguments 
# These are arguments which you use at the end of a function invocation after all the positional arguments 
# They are always optional and always have a default value 
# In this case of the print function, the end argument has the default value of a new line character, and sep argument has the value of a whitespace character
# These are the most frequently userd values, so the creators of python chose them as defaults
# Now lets see how keyword arguments work when you create your own functions:
def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter;
            counter += 1
    print('Number of', letter, 'is', counter)

# Now lets say that we'll be mostly counting the letter A in the string, Which means we can provide the parameter letter with a defualt value of a:
def print_letter_count(text, letter = 'a'):
    counter = 0
    for char in text:
        if char == letter;
            counter += 1
    print('Number of', letter, 'is', counter)
    
# After the function name, we only need to add an equals sign followed by a default value
# We cna now invoke the function with only one value, the string, and we wills ee the letter a being used as the default value
print_letter_count('How many letters a are here?')
#output:
Number of a is 3

# We can also provide default values for both parameters
# So lets say that tect will now have the default value of 'This si the default string to search':
def print_letter_count(text = 'This is the default string to search', letter = 'a'):
    counter = 0
    for char in text:
        if char == letter;
            counter += 1
    print('Number of', letter, 'is', counter)
# Now we can invoke the function with no arguements because both of the parameters have defualt values:
print_letter_count()
# Output:
Number of a is 2

# When defining a value and its parameters, you can mix parameters with and without default values
# But those with the default value must appear at the end meaning if you do the following you will receive an error;

def print_letter_count(text = 'This is the default string to search', letter):
    counter = 0
    for char in text:
        if char == letter;
            counter += 1
    print('Number of', letter, 'is', counter)

# The same applies to positional and keyword arguments when you call the function
# When you call the function that you define keyword arguments must appear at the end meaning that the following is not possible either and will result in an error;
print_letter_count(letter = 'a', 'Search here')

# However you can do the opposite:
print_letter_count('Search here', letter = 'a')
# Output;
Number of a is 1

# # # # REMEMBER # # # #
# All positionl arguments must appear before any named arguments otherwise python wouldn't know which argument goes to which parameter



























