# Now that we have a general idea of dictionaries lets see what operations we can perform on a dictionary 
# first of all since dictionaries are mutable, we can start with an empty dictionary and then add new elements to it as shown below:
from code import banner
grades = {}
# To create an empty dictionary all you need is a pair of curly brackets 
# Now adding a new element can be done with square brackets in a very simple way
grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)
#Output:
['John' : 'A-', 'Anne' : 'B']
# Here you can see that we created an empty dictionary and then added two entries to it 
# note that if anne retakes an exam and we want to update the dictionaries entries we can do so by using the very same syntax as shown below:
grades ['Anne'] = 'A'
print(grades)
# Output:
['John' : 'A-', 'Anne' : 'A']
# another option is to use the update option:
grades.update({'John':'A'})
print(grades)
# Ouput:
['John' : 'A', 'Anne' : 'A']
# Update works the very same way as using square brackets, but the syntax is a bit more difficult and takes longer to write
# To check the number of key value pairs in a dictionary, you can use the Len function 
# If we use the len fucntion on the list we created previously we will get back a value of two as you see below because the dictionary contains two entries or two key value pairs making the length of the dictionary two 
len(grades)
# Output:
2

# To check if a given key is present in a dictionary, you can use the good old 'in' operator
# For example:
for 'John' in grades:
    print('John got:', grades['John'])
# Output:
John got : A

# You can also delete a given key alongside its value using the 'del' operator as shown below:
del grades['John']
print(grades)
#Output:
['Anne' : 'A']

# Next we will discuss how you can iterate a dictionary
# First thing you must know that prior to python 3.6 dictionaries were not ordered
# This means that you could add key value pairs to a dictionary a certain way, but python could then store them internally in another way
# This changed in python 3.6 and dictionaries have now become ordered collections by default
# There are a few ways to iterate a dictionary depending on the situation
# By default if you use a simple for loop the same way you would for lists you will get access to the keys in the dictionary as shown below:
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
for el in grades:
    print(el)
# Output
John
Anne 
 # Here you can see the keys are printed to the output 
 # You will also achieve the very same result when you use the keys method on the dictionary as shown below 
 for el in grades.keys():
     print(el)
# Output:
John
Anne 
# Now if you want to get access to the values instead and the values only, you can use another method named values as shown below:
for el in grade.values():
    print(el)
#Output:
A-
B 
# Finally if you would like to see both Key and vlaue you can use a third method:
for person, grade in grades.items():
    print(person, 'got', grade)
 #Output:
 John got A-
 Anne got B 
 
 # Note that here we used 2 control variables seperated by a comma 'person' and 'grade'
 
 # Naturally you can change these two variable names to anything else you want
 # The important thing is that now, inside the loop we have access to both the key and the value 





























































