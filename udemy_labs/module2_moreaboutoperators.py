#BINARY OPERATORS
#Operators that work with 2 operands of values
#examples:  + (plus), - (minus)

#UNARY OPERATORS
#Operators that work with single operands or values
# We can simply use the plus or minus sign before a single number to indicate that the number is above or below zero

# for example +12 and 12 are equivalent in this instance the + is the unary operator and is optional 
# for this example -2 is the only option to represent a negative number and the - (minus operator) is the unary operator but is not optional

#ORDER OF OPERATIONS 
# 1.** EXPONENTATION
# 2. *, /, //, % MULTIPLICATION, DIVISION, MODULOZATION
# 3. +, - ADDITION, SUBTRACTION

#You may provide parenthesis to indicate the order of operations desired same as in regular arithmatic
# for example 2 + 3 * 2 will be equal to 8 because 3 * 2 is calculated first then 2 is added 
# BUT if we add a prenthesis around 2 + 3 it will be calculated first changed the end result 
#( 2 + 3 ) * 2 will be equal to 10

#The precision of floating point numbers in python 
#Copmuters dont generally understand words or numbers the way humans do
#Thanks to high level programming languages such as python we are able to use concepts that we understand but deep down at the lowest levels of your computer, everything is represented in binary
#The binary system only has 2 numbers 0's and 1's 
# This is because the electrical signal in your computers hard ware can only register 2 states (on-1 & off-0)
#Because of that , there are some limitations:
#Most floats cannot be represented exactly as binary fractions
#As a consequence, the floats that you use in python are only aproximated (rounded) when they are stored
#In other words the float #'s are more or less right, but not 100% correct.
#For example python cannot represent the number 0.1 precisely 
#it may be printed to the screen but when trying to multiply it by itself 3 times you will get a littl bit left over and this is not a bug its just the limitation

#REMEMBER
#!!The precision of floats is limited!!

# A TRICKY CASE WITH THE EXPONENTATION OPERATOR
# In a normal arithmetic problem such as the following:
# 2 ** 2 ** 3 you would believe it would be going from left to right 2 ** 2 = 4 then, 4 ** 3 = 64 
# but python doesnt go from lef to right when it comes to th exponentation operator
# python would say 2 ** 2 ** 3 = 256 by going right to left, 2 ** 3 = 2 ** 8 = 256

# ! ! ! REMEMBER ! ! !
# The exponentation operator (**) uses right-sided binding (i.e starts from the right)

# ALL other operators we know up until this point are left - sided bound
