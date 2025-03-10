# user enters two numbers

# script calculates the result of diving those number
try:
    num1= int(input("Enter a number:\n"))
    num2= int(input("Enter another number:\n"))
    print(f"{num1} / {num2} = {num1/num2}")
except Exception as somevariable :
    print("You screwed up, by the way! This was the error:", somevariable)

# ValueError
# ZeroDivisionError
