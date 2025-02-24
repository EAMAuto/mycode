# Python offers a special instruction to make conditional decisions called a condtional statement or if- statement
user_age = int(input('What is your age? ')) 
if user_age > 30: 
    print('You are over 30 years old')
    print ('Sorry, you do not qualify')
elif user_age == 30:
    print('You are exactly 30 years old')
    print('You will need to meet additioanl conditions to qualify')
else:
    print('You are 30 years old or younger')
    print ('Congratulations, you do qualify!')
# You can use multiple elif statement to include multiple conditions

# NOTE that we use two equal signs to check if the age equals 30 

# USing only one equal sign in python assigns a value to a variable and will not check eqaulity

# Remember that iF statements begin with the keywork if

#on top of that you may have no elif statement or as many as youd like 

# or you can have zero or exactly one else statement

# IF is necesary

#elif is optional but is used to assign additional conditions 

# else is also optional but can only be used one so is used as a catchall or back up plan type of conditional
