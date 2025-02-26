# basic data types include integers, floats, booleans, strings
#They are basic because you  can only store one value at a time inside them
#Python offers complecx data types to solve this problem
#These data types are called collections 
# A collection in python is a data type that can store more than one value in a single variable
#The three types of collections we will learn are lists, tuples, dictionaries 

########################### Lists ##########################
#Lists are usually stored with multiple values of the same type, multiple integers, multiple floats or multiple strings

#For exmaple lets say we wanted to keep the names of the top five most popular cities in the US
#We could do it like this: 
city_1 = 'New York City' 
city_2 = 'Los Angeles'
city_3 = 'Chicago'
city_4 = 'Houston'
city_5 = 'Pheonix'
# Unfortunately working with multiple variables like this is not easy
#it's much better to use a single variable with a list inside 

#To declare an empty list all we have to do is provide a pair of square brackets []

empty_list =[ ]

# Anytime you see a variable declaration like this which uses square brackets you should immediately think of it as a list

#Now if you do want some elements inside, you provide them inside the square brackets seperated by commas
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Pheonix']

# Here we have a list with 5 cities inside it 

#if we use this list in conjunction with the print function 
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Pheonix']                      print(top_cities)

#We will see the following output:
['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Pheonix']
#       0            1              2         3           4       <- Elements

# The Elements are indexed which means each element has unique numerical index you can use to get this partocular element out 

# # # IMPORTANT # # #
# lIST INDICES START ARE ZERO NOT AT 1 SO THIS MEANS THE FIRST ELEMENT IN THE LIST HAS THE INDEX OF 0
# To get a specific element and not the whole list we need to provide the elemnts inside square bracket 

top_cities # Gives you the whole list
top_cities [0] # Gives you the first element in the list 'New York City'
# This operation is called indexing bevause you provide the index of the element inside square brackets 
# If you make a mistake a mistake and try to access an element which doesnt exist youll see an error index error list index out of range

# You can also use negative indices 
top_cities[-1] #Gives you the last element in the list 'Pheonix'
top_cities[-2] #Gives you the second element from the end 'Houston'

# Python also makes it possible to access a few elements at the same time 
# For this we use something called slicing
top_cities[0:2} # To get the first 2 elements in the list
# Here we use a colon : to introduce two indicies
# The first index is the first element to include, & the second index is the first elemnt NOT to include
# So when we make a slice from 0:2 this means we take the first element with zero(0), we take the second element with one (1), and then we stop at the third element with index two (2)
# In other words the first index is inclusive the second is exclusive
# As a result, both the first and the second index can be omitted
top_cities[:4] # If you omit the first index it means 'start from the beginning of the list'
top_cities[2:] # If you omit the second index it means' take all elements from index 2 until the end of the list
top_cities[:3] # This means take all the elements from the beginning of the list until the 3rd indexexclusive
top_cities[10:15] # For trying to slice elements that do not exist you will not recieve an error you will just get back an empty list
# Note that when you access a single element you get a string value
top_cities[0] -> 'New York City'
# but if you use slicing you get a list even if only slicing for one element
top_cities[0:1] -> ['New York City']
