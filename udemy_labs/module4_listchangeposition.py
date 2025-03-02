# Imagine the following problem:
# Our user provides two numbers that we save in two variables named first and second
first = input('Enter first number: ')
second = input('Enter second number: ')

# We then need to swap the values we want the first variable to have the value of the second variable and vice versa

first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first = second
second = first 
print('After Swapping: ', first, second)
#^ if we do the above we will end up with both variables having the same value because this is an assignment operator which is assigning the first variables value to the second then assigning that same value back to the first

# if we would like to swap values we would need to introduce a third temporary variable to act as a holding space 

# You would save the vlaue of the first variable to the temporary third variable so that you dont lose it as shown below:
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
temporary = first
first = second
second = temporary
print('After Swapping: ', first, second)

#Python also has a nice shortcut to do this :
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first, second = second, first
print('After Swapping: ', first, second)

# ^ For the example seen above you can see it is much simpler, all you need to do is provide them with commas in proper order and reverse order with the assignment operator in between
# It turns out that you can use the very same logic with list elements

#Example:
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Pheonix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

#Here we are swapping the places of the 1 and the last element
# The new list will be the following:
top_cities = ['Pheonix', 'Los Angeles', 'Chicago', 'Houston', 'New York City']

# We also typically change element positions when we sort list elements
# Pyhton has dedicated list methods to sort lists alphabetically 

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Pheonix']
top_cities.sort()
print(top_cities)

# The output of the above script will result in the list being reorganized ot be in alphabetical order
#This sort method also works with numbers sorting them in order of the least to greatest 

random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()
print(random_numbers)
 # The output of the above will reorganize the list in in this order -3, 0, 2, 4, 5

# If you would like to reverse the order from Z - A or from greatest number to lowest number you can use a keyword argument 

random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse = True)
print(random_numbers)

# after inputing these instructions we will be able to observe the reverse ordering of letters or numbers

#remember that once you use a method like sort the change is permanent, sometimes you want to change the list temporarily and for this you can use a general list function instead of a list method 
# Example
print(sorted(top_cities))
print(top_cities)

#upon excution fo the above the output we observe will look like the following:
['Chicago', 'Houston', 'Los Angeles', 'New York City', 'Pheonix'] <- Alphabetical order
['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Pheonix']<- original list

# Here you can see hat the sort command printed the list in alphabetical order while the original list remains untouched


# # # # # # # # # # Rememeber # # # # # # # # # #
# list_name.sort() : sorts the original list
# sorted(list_name) : gives back a new, sorted list, keeps the original unchanged

#naturally this all works with numbers as well
