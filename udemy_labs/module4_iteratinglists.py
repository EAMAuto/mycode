# When talking about the for loop, we mentioned the term sequences
# Recall that sequences in python are special data structures that can store more than one value and can be browsed sequentially, meaning element by element
# We also said that strings are a good example of sequences, because you can browse the characters in a string one by one 
# It turns out that you can also iterate lists in the same way as lists are also sequences
# Example:
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Pheonix']
for city in top_cities:
    print('Current city:', city)
#The output of the following instruction will be :
#Current city: New York City
#Current city: Los Angeles
#Current city: Chicago
#Current city: Houston
#Current city: Pheonix

# What we did here was use the fr loop to access the list elements one by one 
# We then defined a control variable named city ( This controlled variable can be anything of your choosing)
# Note: the for loop gets the list elements in the exact order they were provided
# First we begin with index 0 then move to 1 and so on and so forth

#The syntax is very convinient when you want to do something with each element in a list 
#Note however that insides the loops body you have no access to the index of the current element
#For example in the second iteration you get 'Los Angeles' as the value of the variable city here but you have no way of checking that Los Angeles has the index of one 

# There is another way that you can iterate lists so that you can access both the element and the its index

# Lets review an example of this below:
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Pheonix']
for city_index in range(len(top_cities)):
    print('Current index:', city_index, '| Current City:', top_cities[city_index], )

# Here we reintroduce the len function, for string the len function will tell you the amount of character in a string
# When len is used with list it will return the number of elements instead

# So in our case the len function will return 5 as we have 5 cities in the list 
# Now it turns out that range(len(top_cities)) means 5 

# remember that there are a few versions of the range function and for this version we provided the end number of 5 so the default incrementation number of 1 will be used and the default starting number of 1 will also be used

# This means that range(5) will generate the following numbers for us [0, 1, 2, 3, 4] and it just so happens that these are the exact possible indices in our list 
# Inside the loop we now have two options, if we need the index of the given element, we just use the control variable city_index but if we need the element of the given index, we can use the lists name with square brackets to access it top_cities[city_index]

# Another example of iterating over lists
#This time we will write a simple program that sums up someones expenditures
# We have the intitial list where someone wrote down all the expenditures
spendings = [32.45, 18.65, 23.45, 78.32, 5.23]

# The author of the list want us to sum up all these numbers and print the total amount of money they sent
sum = 0.0 # first we need a variable for the sum and at first the sum equals 0.0
# next we will iterate over the spendings 
for spending in spendings:
    sum += spending
    print('Money spent:', sum)
# The output of this will be 'Moneyspent: 158.1' which is the sum of all the elements in our list 
