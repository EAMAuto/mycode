# # # # Dictionaries # # # #
# Dictionaries are collections used to store key value pairs 
emails = {
    'Anne Stahl': 'astahl@gmail.com',
    'Peter small': 'peters@yandex.com',m
    'Mark steel': 'mark@steel.com'
}
# In the above dictionary we have a simple collection of three individuals names and phone numbers kind of like a phone book 
# You can use a dictionary to look up some ones email using the following code
print(emails['Mark steel'])
# output
mark@steel.com
# In other words what this set of instructions is saying is show me the email address for the individual named mark steel 

# In lists's and tuples we access the indvidual elements by providing their index within square brackets
# In dictionaries we can access specific values by providing the key within the same square brackets 

# Another example of a dictionary could be a language dictionary 
# We could have a simple example from English to spanish like this:
spanish_animals = {
    'dog': 'el perro',
    'cat': 'el gato',
    'horse': 'el caballo',
    'bird': 'el pajaro'
    }
# Now if you want to look up the spanish translation for example bird you can do the following:
print(spanish_animals['bird'])
# output 
el pajaro

# Now that we have a general understanding of what dictionaries are let us explain the rules we must follow when creating them
# Dictionaries are created with curly brackets and inside of those curly brackets you provide KEY:VALUE pairs
# We add a comma and then we can introduce another KEY:Value pair and so on 
# Each Key in the KEY: VALUE pair must be unique because If not Pyhton would not know what to return for a given key 
# For example if you wanted to add a synonym for bird inside our previous spanish animals dictionary as seen below:
spanish_animals = {
    'dog': 'el perro',
    'cat': 'el gato',
    'horse': 'el caballo',
    'bird': 'el pajaro',
    'bird': 'el ave'
    }
# if we know print the whole dictionary you will see that python replaces the old value with the new one as seen below:
print(spanish_animals)
# Output:
{'dog': 'el perro', "cat': 'el gato', 'horse': 'el caballo','bird': 'el ave'}
# there is no way to keep them both in separate pairs with the same key

# Note that when you use square brackets to find a value for a key, this only works one way
# You cannot provide a value to try to find its key
# As a general rule a dictionary is a one way tool
# in both our examples the keys were strings but the keys can also be of any other immutable data type such as integers, floats, or even tuples as keys but not lists
# here we will show an example where in the dictionary the keys are integers and the values will be strings
tennis_ranking = {
    1 : 'Ashleigh Barty',
    2 : 'Naomi Osaka',
    3 : 'Simon Halep'
    }
# The above example is a way to create a dictionary and it will work because the integers being used as keys are immutable in nature
# if we to try and put lists in place of the integers by adding square brackets around the integers this will not work 
# Though lists cannot be keys in a dictionary they can be values
# for example:
city_rankings = {
    'Bangkok': [7, 4, 7, 5],
    'Hanoi': [7, 6, 4, 5],
    'Manila': [6, 6, 4, 4, 5]
    }



























