#len()
# The len() function will return the amount of characters in a string

# Keyword/ Named arguements
#arguments which you can use at the end of a function invocation after all the other arguments, they are introduced by using the argument name such as end and equals sign (=).

#w/o key work argument
# print('Hello, World!')
# print('Python speaking!")
# output
# Hello,World!
# Python speaking!
# w/ keyword argument
#print('Hello, World!, end='.')
#print(Python speaking!')
# output
# Hello, World!.Python speaking!


# keyword arguments are always optional
#python functions are constructed in such a way that all keyword arguments must have default values
#for example the end argument for the print function specified what is put at the end of a print invocation and the default value is a new line character
#If you dont specify the end argument, the default value will be used instead

# another important keyword argument for the print function is the sep argument
#It specifies the seperator between the values printed to the output
#The default value is the space character
#W/O sep and end
#first_name = 'john'
#print('your first name is', first_name, 'Welcome!')
#output 
#your first name is john Welcome!

#W/ sep and end
#print('your first name is', first_name, 'Welcome!',sep='-',end='=')
#output
#your first name is-john-Welcome!=

