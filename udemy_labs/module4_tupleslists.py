# Python allows you to put tuples as list elements and lists as tuple elements 
# let us begin by going over how tuples can be elements inside of lists 
# We will create a tuple that represents some basic information about London, the capital of UK
city_1 = ('London', 'UK', 8.98)
# here is the country the city and the population in million 
# Now we will create a similar tuple with some basic info about canberra, the capital of australia
city_2 = ('Canberra', 'Australia', 0.4)
# and finally we will do algiers the capital of algeria 
city_3 = ('Algiers', 'Algeria', 3.9)

# Here we have 3 seperate variables with three seperate cities, so it perhaps makes sense to have them in a single list such as here:
capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), city_3 = ('Algiers', 'Algeria', 3.9)]
# Here we have a list introduced with square brackets and inside we have 3 elements 
# Each of the elements is a tuple and we can work with such lists in the usual way.
# For example we can use for loop as shown below
capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), city_3 = ('Algiers', 'Algeria', 3.9)]
for capital in capitals:
    print('Name:', capital[0], ',country:,', capital[1], ', Population:', capital[2]
# output:
Name: London , Country: UK , Population: 8.98
Name: Canberra , Country: Australia , Population: 0.4
Name: Algiers , Country: Algeria , Population: 3.9

# # # # # Now we will go over lists inside of tuples # # # # #
# Lets say we have a user tuple with some basic user data
user_data = ('John', 'American', 1964)
# Now John would like to be able to keep track of his weight
# So after a comma we add to following list to the tuple:
user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])

# So here we have an interesting example of a list inside a tuple
# we gathered together various pieces of information about John under a single tuple and one of the tuples elements is a list of his weight changes

# Even thought the tuple itself is immutable and you can add new elements to the tuple, the tuples last element which is a list is still mutable, so you cannot add another list to the tuple or get rid of existing elements in the tuple but you can add new weight measurements to the list inside of the tuple 

user_data[3].append(79.6)
print(user_data)
#output:
(('John', 'American', 1964, [77.0, 78.2, 77.5, 79.6]) # The change is added to the mutable list 

# In short a tuple is immutable and cannot be changed only written over, but if your tuple contains a list which is mutable then you can make changes to that list without needing to overwrite the entire tuple 