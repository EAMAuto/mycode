# In this lab we will explain how to copy a list into a new variable 
# It may seem easy but there is a catch we need to go over
# When you work with a basic data type such as an integer or a string, you can see that the name of the variable is the name of its content
# If we want to copy te content of this variable, all we have to do is create a new variable and use the assignment operator (=)
# for example 
name_original = 'Jon snow'
name_new = name-original
# Here the second line takes the string value stored under the name of the first variable and copies it into 'name_new'
# The important thing here is that 'name_original' and 'name_new' have the same value but are independent of eachother meaning if you change one it will not affect the other
#for example
name_original = 'Jon snow'
name_new = name-original
name_original = 'danaerys targeryan'<- here we are reassigning a new value to name-original but name_new will remain 'jon snow'

# These same rule applies to other basic data types such as integers, floats, booleans

#However the same rule is not true for data collections like lists
# Lets explore:
list_original = [1,2,3]
list_new = list_original
list_original[0] = -5
print(list_original, list_new)

#the output you will recieve from the following code  will be:
[-5,2,3]
[-5,2,3]
# Here we tried to copy the contents of the original list into the new list and display both the original list and new list but we were only able to print out to new list twice
# This occurs because with complex data types like lists, the name of the list does not point to the actual list in the computer memeory. INstead the name of the lsit is the name of the memory location where the list is stored 

# In computer programming we often call these refernces because they refernce other places in the memeory 

# When we assign the value of the original value to the new variable, all we do is we copy the reference to the original list
# behind the scenes both variables now point to the very same place in the memory with the very same list. 
# As a result, wen you try to modify some of the elements in one of the variables, you also modify the elements of the other variable at the same time because both of these variables share the same list
# The question then becomes, hwo do you actually make a copy of a list so that two variables have two seperate lists that you can modify independently 
# All you have to do is use slicing
# Below is an example of hwo to accomplish this:
list_original = [1,2,3]
list_new = list_original[:] <- slicing
list_original[0] = -5
print(list_original, list_new)

#This output will read as follows:
[-5,2,3]
[1,2,3]

# nAturally you can also copy a selected fragment of the original list using slicing 
# If you want to copy the first two elements into a list:
list_original = [1,2,3]
list_new = list_original[:2] <- indicates the first two elements
list_original[0] = -5
print(list_original, list_new)
