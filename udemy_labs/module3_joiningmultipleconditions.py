# Our If statement so far focused on single conditions that were satisfied or not 
# but sometimes we want a more complicated logic 
# We may want to excecute some code when two or more conditions are met at the same time
#Or we may want to excecute some code when at least one of many conditions is met
# To that end we will use the so called BOOLEAN OPERATORS

#THERE ARE 3 SUCH OPERATORS IN PYTHON
# AND 
# OR 
# OR NOT

#AND EXAMPLE
# user_age = int(input('What is your age? '))
# user_country = input('What is your country? ')

# if user_age < 25 and  user_country =='Germany':
   # print('You can apply for a german student exchange programme')

# else:
#    print('Sorry, you do not qualify')

# OR EAMPLE
# user_country = input('What is your country? ')

# if user_country == 'Sweden' or  user_country =='Denmark' or user_country == 'Norway':
#    print('You can apply for a scandenavian student exchange programme')

# else:
#    print('Sorry, you do not qualify')

# IF NOT EXAMPLE
# user_country = input('What is your country? ')
# if not user_country == 'Germany':
#    print('Your are not from Germany!')

# else:
#    print('Your are from Germany')

# You can also join all three operators and, or , or not in the same complex condition
user_age = int(input('What is your age? '))
user_country = input('What is your country? ')
if not user_country =='Germany' and user_age < 25 or \
        user_country == 'Germany' and user_age < 23: # if line of code is going to be supe long and you would like to continue on seperate line you can use the | (backslash to extend statment to seperate line)
    print('You qualify!')
else:
    print('You don\'t qualify!')

#order of Booleans
# 1. not
# 2. and
# 3. or
