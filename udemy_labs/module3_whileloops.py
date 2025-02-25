# Loops are used to repeat an instruction or many instructions more than once
# There are two types of loops while and for loops 

#Syntax
#while condition:
#    do_something()
#    do_something2()
# This loop now means so long as the condition is met do_something  and do_something2
# In this loop we will have a program with a while loop which prints numbers from 1 to 10

# First we  create an integer variable named counter and give it the value 1
#counter = 1
# we often such integer variables with loops in programming, especially with the while loop 

#Now we will creat the loop itself
#while counter < 11 :
  #  print(counter)
 #   counter += 1
#print('Finished!')

#BEWARE, alot of the times newbies can forget to incriment the counter by one which will lead to the condition always being true creating an infinite lop which never ends

# Remember #
# Increasing by 1 is called incrementation

# While loops are often used when we dont know how many time we should execute the loop body, 
# This is often the case when we work with user input

secret_number = 14 
print('''
=====================================
========== SECRET NUMBER GAME =======
=====================================
''')
user_input = int(input('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
     print('Wrong')
     user_input = int(input('Try to guess the secret number from 0 to 20: '))
print('Perfect! You have guessed the secret number.')
#In python if you start and end a string with triple quotes (''') you can use multi-line strings and python will print them to the output exactly the way you provide them in the code
