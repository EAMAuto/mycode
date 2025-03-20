# Recursion is a special technique for writing functions in most programming languages, including python.
# Recursion takes place when a function calls itself
# we will use the following problem as an example:
# we want to write a function to provide the factorial for a given number
# What is a factorial
# it is usually expressed as an exclamation mark after a number
# Its is the multiplication from one up to the number
# For example the factorial of 3 is 1 *1 + 1*2 + 1*3 which equals 6
# now we shall write a function to calculate this:
# We will start with a version that doesnt involve recursion
def get_factorial(number):
    factorial = 1
    for x in range(1, number + 1):
        factorial += x
    return factorial

# Now if we input the following;
print(get_factorial(6))
# We will get back:
720

#This approach to writing functions is often called iterative, because inside the function we use a for loop to iterate a sequence of numbers
# Lets see how we can write the same function using recursion:
# first let us explore factorial's:
# NOte one thing we can say that the factorial for a given number such as three is always equals to this number multiplied by the factorial for the previous number
#In other words:
# factorials can be expressed in two way 
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4
# 5! = 1 * 2 * 3 * 4 * 5

# OR

# 1! = 1
# 2! = 2 * 1!
# 3! = 3 * 2!
# 4! = 4 * 3!
# 5! = 5 * 4!

# We will use this to create our recursive version of the factorial function
def get_factorial_recursive(number):
    return number * get_factorial_recursive(number - 1)
# This is the first important piece of our recursive function ( The part where the function calls itself
# This code also accounts for the rule we just learned about related to factorial's
# However if we leave this function as is it will throw an error saying maximum recursion depth exceeded this is because the functions should also contain a so called stop condition, something that tells the function when to stop, at the moment as the function currently is recursion never ends for any number, meaning we will infinitely try to get a factorial for a lower number, this means the functions doesn't stop at 1 as it should it just keeps trying to go lower and deeper attempting to find a factorial using 0 and -1 and -2 etc etc
# So if this program was allowed to run it would continue to try to find a factorial until -infinity and would eventually take up too much memory and crash 
# We need to provide python with a stop condition  basically telling python to stop 
# It should stop when we reach number 1 as we can only calculate factorial's based on natural numbers meaning integers not less than one and for number one we know that the answer is just one
# So lets add a stop condition to our code:
def get_factorial_recursive(number):
    if number <= 1
        return 1
    return number * get_factorial_recursive(number - 1)
# Now if you input the following :
get_factorial_recursive(6)
#Output:
720 
# Our code now works as it should because we included the stop condition





























