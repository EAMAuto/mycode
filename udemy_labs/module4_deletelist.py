# We already now how to create a list and access its elements now we will learn how to delete elements from a list
top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Pheonix']
# you can see in this list we have a city that does not reside in the United States in the 3rd element or index # 2
#In order to delete this element we will introduce a new keyword named del which is short for delete
del top_cities[2] # Deletes Singapore from the list
top_cities[2] -> ['Chicago']
# upon the execution of this code the string singapore will be deleted and all elements to the right of it will be shifted to the left to fill in the space meaning the new 3rd element or index numer 2 will be chicago 
# We can also delete multiple elements at once by using the del intruction alongside slicing
# For example:
del top_cities[3;] -> ['New York City', 'Los Angeles', 'Singapore']
# This instruction is saying 'Starting at index 3 delete all elements in the list until the end of the list'
# This instruction leaves the first 3 elements in tact
#indices with numbers 0,1, & 2 will still be apart of the list 
# You can also delete all elements from a list without deleting the entire list itself by using the del isntuction with slicing and not including any indices 
del top_cities[:] -> []
# You can also delete the entire list by providing the list name along with the del instruction 
del top_cities # Deletes the list 
print(top_cities) -> NameError: name 'top_cities' is not defined 

# # # # NOTE # # # #
# del is not a function it is na instruction 
# We know that it isnt a function call because each function call requires a function name followed by a pair of parenthesis 
