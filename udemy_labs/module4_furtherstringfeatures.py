# Now that we know lists and we understand concepts such as indexing, slicing, and using methods, lets see how we can apply these features to have more control over our strings since strings are sequences just as lists are
# first of all,  we can use indexing and slicing with strings to read individual characters or groups of characters
from pip._vendor.pygments.unistring import Me
fav_band = 'Green Day'
print(fav_band[6])
#output:
D
print(fav_band[;6])
#output:
Green
# Note however that you cannot use indexing to change individual characters within a string
fav_bands[6] = 'M'
#output:
# You will receive an error "STR object does not support item assignment"

# Next, strings in python have many built in methods just like lists, with lists you've seen methods such as append, insert, and sort. Strings dont offer these methods but they offer many others

# Here we will go over a few
# For instance, we have methods that transform our string somehow and give us a new string back such as upper and lower
text = 'please capitalize me'
text_cap = text.upper
print(text_cap)
#output:
PLEASE CAPITALIZE ME 

# We also have quite a few string methods that return True or False.
# for example: is numeric checks whether your string contains digits only
# This could be helpful when you use the input function to get a number from the user
# Example:
user_number = input('Please provide a number: ')
if user_number.isnumeric():
    print('Thank you, thats a correct number')
else:
    print('Sorry,', user_number, 'is not a number')
#output:
Please provide a number: #<- first the script will ask for user input
2 # we provide an input of 2 
Thank you, thats a correct number #<- returns the if  condition statement output because we provided a number

# OR #

Please provide a number: #<- first the script will ask for user input
hello # we provide an input of 'hello"
Sorry, hello is not a number #<- returns else condition statement

# Other methods like this are for example:
# islower- which verifies if the string only contains all lowercase characters 
# isspace - which verifies if the string only contains white spaces

# There are many more built in string methods that you can use in your applications but it doesnt make sense to memorize them all. Rather you should look them up when you need something specific
































