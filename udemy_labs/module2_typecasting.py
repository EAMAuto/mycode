# given the following code you can see an error

#height_cm = input('Heigh converter : Enter your height in cm: ')
#print('Your height in feet is ', height_cm / 30.48 )
# This piece of code is designed to recieve and input in cm from the user and divide that input by 30.48 (float) to then return the users height in feet, the porblem here is that the input command will only return a string datat type by default and strings cannot be mathematically divided

# how do we fix this?
# We must incorporate the float() function

#The float() function accepts one argument, a string value, and the function tries to convert that value into a float
# there are a few ways to introduce this new function into our code
# you can introduce a new variable 
#height_cm = input('Heigh converter : Enter your height in cm: ')
#float_cm = float(height_cm)
#print('Your height in feet is ', float_cm / 30.48 )
#THIS WILL PROVIDE THE CORRECT OUTPUT ALTHOUGH WE ARE USING ADDITIONAL STEPS AND INTRODUCING UNECESARY VARIABLES

#We can also nest the input command within the float command
#height_cm = float(input('Heigh converter : Enter your height in cm: '))
#print('Your height in feet is ', height_cm / 30.48 )
#THIS IS COMMON PRACTICE

#IF A FLOAT IS NOT DESIRED FOR CACLUATION AND INSTEAD AN INTEGER IS THE DESIRED DATA TYPE WE CAN USE THE Int() function instead
#year_born =int(input('What year were you born? '))
#print('In 2100, you will be', 2100 - year_born, 'years old, provided you live this long!')


#There is also a reverted function which will convert an integer or float into a string using the str() function.
#This can be useful for including the results of a mathematical calulation in a string
#temp_c = input('Enter the temperature today in celsius degree: ')
#temp_f = float(temp_c) * 1.8 + 32
#temp_statement = str(temp_c) + ' degrees Celsius ' + str(temp_f) + ' degrees Fahrenheit'
#print(temp_statement)
#This program asks the user to provide the temperature today in Celsius degrees, then it calculates the temperature in Fahrenheit degree, it the creates a new string that is a result of multiple concatinations.

#NOTE 2 things
# changing between data type types for example string to floats, floats to strings, floats to integers, integers to strings, etc. is reffered to as TYPE CASTING
# The functions we have discussed above ( float(), int(), str() ) only attempt to cast the values but may fail, for example if you ask a user for a number but they provide a name the program will fail
