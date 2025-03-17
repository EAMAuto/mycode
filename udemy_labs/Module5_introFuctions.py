# In this final module of this course, we learn how to write our own functions
# Functions that we have used up until this point such as print and len are built in function which someone else has prepared for us
# Its time we started to create our own functions 
# Writing functions can help divide our code into well isolated pieces 
# By using functions, especially with longer programs you can organize your code so that its easier to read and easier to maintain later on 
# With well defined and well named functions you have the chance to make your code more readable 
# The second important reason we write functions becomes more obvious when you repeat some operations over and over in your code instead of copy pasting your code into 5 different places you can simply write a function once and then call it in all of these places, if you later find some bug in your code you only have to fix it in one place rather than in 5 different places
# In theory the simplest function that we can write in python looks something like this:
def greeet():
    print('Hello, my dear!')
# lets analyze the piece of code above:
# firstly, we must understand that function definition begins with the word def which is short for define
# Then after the space we provide the functions name 
# You can give any name that you want, and the rules for naming functions are the same as for naming variables
# After the functions name you must provide a pair of round brackets ()
# For now they are empty but this will change soon
# After the round brackets you must end the line with a colon 
# On he next line this is where the function body begins
# Just like with IF statements and loops, you need at least a single indented instruction which is to be executed whenever the function is invoked
# This function we have created only has one purpose and that is to print the words "Hello, my dear!"as the output
# Note that if we were to run this piece of code as it is nothing would happen and that is because all we have done is define the function we havent invoked it anywhere

# Now in order to actually call the function we must give the functions name and a pair of round brackets as shown below :

def greeet():
    print('Hello, my dear!')
    
greet()
#Output:
Hello, my dear!

# You can also call the function as many times as you would like:
def greeet():
    print('Hello, my dear!')
    
greet()
greet()
greet()
# Output:
Hello, my dear!
Hello, my dear!
Hello, my dear!

# Keep in mind that you cannot invoke a function before it has been defined
# A good practice is to keep all your function definitions at the top of your file
























