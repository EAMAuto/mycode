# We already know how to handle an exception using the try except statements
# Now an interesting aspect of exception handling is when have multiple functions calling eachother
# Take a look at the following program:
def get_day(user_info):
    day = int(input('What is the day of your bday? '))
    user_info.append(day)

def get_month(user_info):
    month = int(input('What is the month (1-12) of your bday? '))
    user_info.append(month)
    
def get_year(user_info):
    year = int(input('What is the year of your bday? '))
    user_info.append(year)
    
def get_user_bday(user_info):
    get_day(user_info)
    get_month(user_info)
    get_year(user_info)
    print('So your bday is', user_info)
    
print('Hi, i will collect some info about your bday!')
user_info = []
get_user_bday(user_info)

# The program above collects some basic information about a user's Birthday
# Ther is a function called get_user_bday that calls three other functions get_day, get_month, get_year

# Each of the three functions collects a piece of information about the user & puts a piece of information into a common list name user_info
# You can see that we used the int function in these function we created 
# We know that the int function acts up when we input anything not expected in such as a letter instead of a number 
# We already know that in order to combat exceptions that could be thrown at our user we can use try and except statements and for this example if we decided to go that route we would need to do this for all 3 of our information gathering functions but instead we can do something else, we can use a signle try and except statement in the get_user_bday function as shown below:
def get_day(user_info):
    day = int(input('What is the day of your bday? '))
    user_info.append(day)

def get_month(user_info):
    month = int(input('What is the month (1-12) of your bday? '))
    user_info.append(month)
    
def get_year(user_info):
    year = int(input('What is the year of your bday? '))
    user_info.append(year)
    
def get_user_bday(user_info):
    try:
        get_day(user_info)
        get_month(user_info)
        get_year(user_info)
        print('So your bday is', user_info)
    except ValueError:
        print('You entered incorrect data, bye!')
    
print('Hi, i will collect some info about your bday!')
user_info = []
get_user_bday(user_info)
# Upon adding this try and except statement we can now handling the ValueError exception and prompt our user with 'You entered incorrect data, bye! and exit the program' no matter which function raised the exception
# How does this work?
# there is a rule that states the following: Exceptions are propagated through functions in python
# Basically we can say that exceptions in python are propagated, if a function that raises an exception doesnt have a try except block, the exception is propagated to the function that called it 
# If that function doesnt have a try except block either then the exception is then propagated again until it reaches a try and except block somewhere in the function call chain
# If no try except block is found anywhere in the function call chain hen python will simply show a nasty error message that we have seen many times
# You can also delegate or propagate the exceptions to the functions above


