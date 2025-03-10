# Tuples are a bit similar to lists
# They are also collections of multiple elements, and all the elements can have the same or different data types
# You know that lists are created with square brackets []
# Tuples are created with round brackets ()
# To create an empty tuple we can do the following:
empty_tuple = ()
# To create a one element tuple we have two options:
# Option A:
one_el_tuple_a = (1.)
# Option B:
one_el_tuple_b = 1,
# here the round brackets are optional but note that we had to introduce a comma after the element in both cases the comma might seem strnage, but is required due to syntax reasons
# Python must somehow understand that you are trying to create tuple and not an ordinary single value
# When you have more than one value in your tuple, the final comma is optional
three_el_tuple = 1, 2, 3
# You may or may not add round brackets as well
# Note that no matter if you add or choose to omit the comma at the end the print function will always show your tuples in the very same way

three_el_tuple = 1, 2, 3
print(three_el_tuple)
#output:
(1, 2, 3)

# Note that the round brackets were still printed to the output even though we omited them, if we decided to add a comma to the end of the tuple it would print the exact same way as before

# tuples prefer round brackets, while lists prefer squared brackets 
# Both types of collections can have many elements separated by commas
# This is not the biggest difference between the two but to understand the biggest difference between them we must first understand mutability in programming

# In general there are two kinds of python data, mutable and immutable
# Mutable data can be freely updated any time you want
# Lists are a good example of mutable data
# When you create a list, you can easily add new elements to it, delete unwanted elements, swap the places and so on

# tuples are different
# When you first create a tuple it stays this way forever
# You could of course assign a new tuple to the same variable as shown below;
user_data = ('John', 'American', 1964) # We could start with a tuple like this 
user_data = ('Katya', 'Russian', 1980) # Then using the assignment operator again we can assign a new tuple to the user_data variable
# In the second case we get rid of the old tuple with john and replace it with a new tuple with katya
# This is a legit operation in python, but there is no way to add new elements to a tuple
# remember how we used the append method to add elements to a list, it will not work with tuples as shown below:
user_data.append('Teacher')
# output:
# You will get back an error saying tuple object no attribute to append 

# We can however use index and slicing to get tuple elements but you cannot use indexing to change individual elements only to read as shown below:
user_data = ('Katya', 'Russian', 1980)
print(user_data[0])
# output:
Katya

user_data = ('Katya', 'Russian', 1980)
user_data[0] = 'Mark''
 # output:
 # You will get an error message saying tuple object does not support item assignment
 
 
 # SO in short the biggest difference between lists and tuples is that lists are mutable and tuples are immutable 
 
 # You can freely add, delete, and modify list elements, but you cont do the same with tuples
 
 # Incidentally, strings in python are also immutable
 # You can access individual characters in a string but you cannot replace individual characters























