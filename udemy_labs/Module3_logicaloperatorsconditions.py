# available logical operators

# < Less than
# > Greater than
# <= Less than or equal to
# >= Greater than or equal to 
# == Equals
#!= Not equals

# Not equals example#
password = input('Do you know the secret password? ')
if password != '--secret':  # conditions#
    print('not correct')
else:
    print('Correct password')
# When python sees a condition with one of the logical operators, it checks wether the condition is met or not (BOOlEAN LOGIC)

#BOOLEAN LOGIC RECAP#
# Boolean variables can have one of two value True or False 

#if blcoks are only executed when the condition equals true, if changed to false it will not execute

#example
if True:
    print('Condition met')
#output will always be "condition met"

if False:
    print('condition met')

#output will always be blank for this

# # # # # # REMEMBER # # # # # #
# = ASSIGNING VALUES
# == CHECKING EQUALITY
