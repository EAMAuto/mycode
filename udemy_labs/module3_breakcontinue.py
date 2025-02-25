# We already know two important types of loops while & for
# Ther are also two important keywords that influence how your loop's body is excecuted break & continue

# When Python encounter a break instruction, it immediately exits the loop and moves on to the next instruction outside the loop
    # Usually break instructions are used inside loops with if statements as shown below
while True:
    name = input('Enter your name or Exit to close the program: ')
    if (name == 'Exit'):
    break
print('Hello', name)

# In the above code we are asking a user for name endlessly and printing Hello and the user's name endlessly until the user types exit then we are breaking out of the loop 

# The other word frequently used in loops iis continue
# Continue is used to excape the current iteration and move on to next one 
# Also typically used with if statment when we sometimes want to skip a certain iteration


#Lets say we want to show all numbers from 1 to 20 except those that can be divided by 5
for i in range(1,21):
    if i % 5 == 0:
        continue 
    print(i)
#In this example we use a trick to check if the number is divisible by 5, modulo division, if a number module divided by 5 gives 0, it means the number is divisble by 5. In such cases we use continue statement and thus we dont print the number but if we encounter a number which is divisible by 5, we dont exit the whole loop instead we just move on to the next value.
