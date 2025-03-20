# There is one interesting type of function in python and that is called a generators
# They are typically used when you want to return alot of values one by one 
# Let us look at an example:
def get_number():
    for i in range(1, 4):
        yield i
# Here we are iterating over the numbers 1 to 3 with a control variable named i
# Inside the loop we use a new keyword yield
# Whenever you use the keyword yiel instead of the keyword return, your function becomes a generator
# Now how can we use this function?
# It turns out you can't simply print the output of the generator like this:
print(get_number())
# You will see a very technical description of the generator object like this:
<generator object get_number at 0x00000163c08B4CA8>

# The function returned a very special kind of object for us, a generator 
# We can now ask the generator to provide us with values one by one, using a special instruction
# to do that we must first store the generator inside of a variable as shown below
genertaor = get_number()
print(next(generator))
print(next(generator))
print(next(generator))
# output:
1
2
3
# In the example shown above we are using a special instruction named next with the generator variable as its argument
# Now whenever we use the print function, we get a new value 1, 2, 3 etc etc.
# This is how generators work, they generate certain values for us one by one and we can ask for another using the next function
# The generator from the given value always remembers the last value that it returned so that the next function call will always work correctly
# You will get new values with next as long as your function code allows it
# In this function we can get number until 4 exclusively meaning up until 3 because of the range we provided before
# If you have reached the highest number provided in your function and you try to generate another number you will get an error: stop iteration

# You can also use a for loop with a generator in the following way:
for x in get_number():
    print(x)
#output:
1
2
3

# Here we use the get_number generator in the place where we normally use the range function and it worked
# One more thing you can do with generators is turn them into lists using the list function
# So again we will use the get_number generator and we will do the following :
numbers = list(get_number())
print(numbers)
#output:
[1, 2, 3]
# here you can see that the values from the generator are turned into a list







































