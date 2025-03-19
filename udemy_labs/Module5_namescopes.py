# In this course when we say the scope of a name, we will refer to a variable name
# The scope of a name is the part of the code where the name is properly recognizable and can be used
# Take a look at the following code:
def show_truth():
    print(mysterious_var)

show_truth()

# Obviously the output to the above code with show an error
# mysterious_var was never defined so it can't be printed
# In other words, Python doesnt recognize the name mysterious_var
# One thing we can do naturally is define mysterious_var inside the function definition as shown below:
def show_truth():
    mysterious_var = 'Surprise!'
    print(mysterious_var)

show_truth()
#Output:
Surprise!

# Can we define the variable outside the function definition before the function call like below:
def show_truth():
    print(mysterious_var)
    
mysterious_var = 'Surprise!'
show_truth()

#Output:
Surprise!

# The asnwer to the above question is yes, we can.
# This is because variables that exist outside the function, like the one here at the time of a function call have a scope inside the functions body
# This means that functions can see them and use them
# Now lets do the following experiment:
def show_truth():
    mysterious_var = 'New Surprise!'
    print(mysterious_var)
    
mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)

#Output:
Surprise!
New surprise!
Surprise!

# First we define mysterious_var as having the value of surprise!, and we print surprise! to the output on line 1
# Now we call the show_truth() function, which assigns the new value of new surprise! to mysterious_var and then print it so we can see new surprise in the output
# Now when we exit the function and we return to the main code and print mysterious_var again on line three you can see the old value 
# How is this possible?
# We changed mysterious_var inside the function body
# So why is the old value back after we exit the function in python?
# This phenomenon is called shadowing
# When we call a  function like here and we try to modify myseterious_var python can see that there is already a variable named myseterious_var outside the function
# So for the purpose of the function, a second temporary variable with the same name is created
# Here we used a local variable named myseterious_var and then after we move back to using the global variable named myseterious_var
# They are two different variables with two seperate values
# We can say that the local variable inside the function shadows the global variable 
# The global variable myseterious_var is available before and after the function call, so surprise on line one and surprise on line three
# But during the function call its shadowed by the local variable with the same name
# This is why you get new surprise! in the middle on line 2

# When we work on complex real life applications, we often use hundreds of functions written by other people
# The chance that we will have at least one gloabl variable with the same name as the local variables in one of these functions is very high
# If there was no shadowing, then functions written by other people could accidentally change the values of our global variables and we wouldnt really know what's happening 
# Thanks to shadowing, we can be sure that our function will not modify something accidentally
# But if you still want to modify a global variable within a function, you can use a new keyword to that end
# Take a look here:
def show_truth():
    global mysterious_var
    mysterious_var = 'New Surprise!'
    print(mysterious_var)
    
mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)

#output;
Surprise!
New surprise!
New surprise!

# NOw you can see that the new surprise! is printed after we exit the functions body
# We added a new instruction at the beginning of our function body global mysterious_var
# This instruction means don't use shadowing for the variable mysterious_var
# In other words dont create a second temporary variable name mysterious_var, instead use the global variable with this name
 # when we assign the new value of "New Surprise!"
# In many cases, using the global keyword will do more harm then good 
# So as a general rule we try to avoid it
# Theres one more thing you need to pay extra attention to when working with lists specifically
# Here you can see a standard example of shadowing:
def show_truth():
    mysterious_var = ['New Surprise!']
    print(mysterious_var)
    
mysterious_var = ['Surprise!']
print(mysterious_var)
show_truth()
print(mysterious_var)

#Output:
['Surprise!']
['New Surprise!']
['Surprise!']
# Here you can see a standard example of shadowing inside the function body
# We created a local variable with the same name as global variable, and we assigned name mysterious_var
# So when we exit the function and we print msyterious_var again, you can see that the list with the initial value of surprise is unaffected
#But now take a look at the following:
def show_truth():
    mysterious_var.append ('New Surprise!')
    print(mysterious_var)
    
mysterious_var = ['Surprise!']
print(mysterious_var)
show_truth()
print(mysterious_var)

#Output:
['Surprise!']
['Surprise!', 'New Surprise!']
['Surprise!', 'New Surprise!']

# Note that here we dont use the assignment operator
# At the beginning of the course we said that a variable with a given name is created when we first assign a value to it using the equals operator
# Here we never use the equals operator, which means we never create a local version of the variable 
# As a consequence This also means that the method works on the global variable that points to the list
# And this means the original list from the global variable is changed
# And just like this, you can see that we add a second element to the listwith new surprise and print it to the output on line two 
# Then we exit the function adn we print the list again, you can see both elements inside
# In other words, if you assign a new list to the same variable in a function, shadowing works fine 
# But if you change the list using a method user square brackets or the del instruction the list outside the function will reflect the change
# This rule applies to lists & dictionaries because they are mutable and you can change there contents 
# This rule does not apply to tuples as they are immutable and once created cannot be modified so theres no risk of changing tuples inside function bodies


















































