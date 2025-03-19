# Functions can typically do two things in general:
# 1 Cause some effect
# 2 Return a meaningful value
# There exists function that can do both of these things at the same time 
from builtins import None

# Print is an example of a function that doesnt return any meaningful value, it only causes some effect by showing some text to the console
print('hello')
# Len in turn doesnt cause any effect but instead returns a meaningful value which is the number of elements in a collection such as strings
len('hello')

# We can then assign this return value to a variable and we can use it in a loop:
length= len('hello')

# Finally, input is a function that does both things at the same time
# it causes an effect by prompting the user to provide a value and it also returns the value to us so we can do the following:
number= input('What is the number')
# output:
what is the number? 
# our input will be:
5
# And now you can see that the value of 5 is stored inside the number 
# So input returns the value of 5 to us 
# NONE is used to describe a null value or no value at all
# the tricky part about none is that it is a special value 
#none is not zero
#none is not false
# none is not the same as an empty string 
# only none can be none 
# take a look at the example below:
x = None

if x:
    print('None is True')
elif x is False:
    print('None is False')
else:
    print('None is not True, or False, None is just None')
    
#Output:
None is not True, or False, None is just None

# You can see here that none is very unique, its neither true nor false
# However you can do the following in your code:
x = None
if x is None:
    print('Yes')
if x = None:
    print("it does")
#output:
yes
it does
# Here you can see both of these things work fine
# So you can assign none to a variable like here on line 1
# and you can check if the value of a variable equals none, like here on line two and four

#none is a value returned implicitly by functions that dont return anything meaningful 

























