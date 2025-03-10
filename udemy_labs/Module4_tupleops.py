# We said that tuples and lists share many features, but they are also essentially different
# Lists are mutable and you can change them 
# tuples are immutable meaning once they are created you cannot change the elements of a tuple
# So what tuple operations are available in python
# the len function is available to count the number of elements in a tuple
user_data = ('John', "American", 1964)
print(len(user_data))
# output:
3 # The tuples has 3 elements

# you can also use the in and notin operators the same way as with lists
if 'American' in user_data:
    print('This person comes from the US!')
# output:
This person comes from the US!

# You can also iterate a tuple with a for loop
user_data = ('John', "American", 1964)
for element in user_data:
    print(element)
#output:
John
American
1964

# Tuples can also be added together or multiplied by an integer
user_data = ('John', "American", 1964) + ('Teacher', 'male')
print(user_data)
# Output:
('John', "American", 1964, 'Teacher', 'male')

# Note that behind the scenes we get a new tuple this is because as said before you cannot change existing tuples. So when you use the plus operator (+), all you do is you actually prouce a new tuple with all the elements that is assigned to our variable of user_data

# Similarly we can do something like multiplication as shown below
numbers = (0,1) * 10
print(numbers)
 # output:
 (0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1)
 
 # So you can see that tuples really share alot of features of lists and vice versa
 
 # # # # # # # # # # Now how do you know when you should use lists and when to use tuples?  # # # # # # # # # # 
 # this will of course come naturally to us as we become more experienced in programming 
 # This is the general rule 
 # Lists are typically used in situation when you want to have many values of the same data type
 # Lists are used when the values represent examples of the same class or the same phenomenon 
 # examples:
male_names = ['Adam', "Jerry", 'Mark'] # each element in this list is a different name but all the elements are strings and all of them represent male names
berlin_temps = [13.0, 17.5, 112.0] # Each element is a float that represents the temperature in berlin on a different day
# again all the elements are floats and all of them represent temperatures
# in cases such as the ones above its best to use lists


# Tuples in turn are often used when you want to group together values of different types that are somehow related, and together they form somer sort of structure or some sort of bigger data

# You have seen one such example already that we will revisit below:
user_data = ('John', 'American', 1964)

# Here you can see wew have 3 elements with different data types
# The name and nationality are strings while the year born is an integer but somehow all three data types are related because they all describe one user

# Sometimes it can make more sense to have the values in seperate variables but in another occasion it may make more sense to group them all together inside of on tuple

# tuples arent only used to group values that are somehow related together and form a bigger object they are also used to perform certain python operations quicker

# You have seen an example of this:
first = 5
second = 7
first, second = second, first # Now it turns out that first, second and second, first are now tuples
# This is the most powerful tuple properties
# they can appear on the left side of the assignment operator and on the right side as well
# You can also see that tuple elements can be variables, first and second for example are variables and not literals
# This way we are able to perform a swap operation in a single line 

























