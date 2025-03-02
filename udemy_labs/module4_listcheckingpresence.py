# We already know the 'in' Keyword
# When its used ina loop its used to indicate the range of possible values for a control variable 
# for example take a look at the following code piece:
for char in 'happy message':
    print(char)

# Here the 'in' operator indicates that the loop should check every element in the happy message string
# However the 'in; operator can be used to check whether a given element is present in a list
# Take a look at the following code:
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name in invited_guests:
    print('Welcome!')
else:
    print('You are not invited!')
# This code defines a list of guests and asks the guests there names and if the guests name is in the list they are welcomed and if they are not in the list they are told so

invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name not in invited_guests:
    print('You are not in the list')
else:
    print('Welcome!')

# Taking a look at this nw example above you can see that the logic is reversed when using the 'not in' keyword 
#This code example is taking user input and if not in the list it you are being told so and if you are in the list you get told welcome
