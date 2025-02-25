answer_a = input('Do you like traveling? y/n: ')
if answer_a == 'y':
    answer_b = input('And do you like asia? y/n: ')
    if answer_b == 'y':
        print('Excellent! You can win a ticket to Thailand!')
    else:
        print('Sorry, to hear that!')
else:
    print('Sorry to hear that!')

# Note that this nested if program is meant to ask the user 2 things, if they like to travel and if so, do they like asia
# if the answer to both these questions is yes we show them a special message about a ticket lottery 
# if the answer to any of these questions is no then we apologize

# Note that proper indentation is very important here 
# The lines with IF and ELSE keywords in the nested if are indented with four spaces but the if and else blocks are indented even further with 8 spaces
#This way python can understand that this is an if statement on its own and that it should only be used when the first answer is yes 
# This multi-level indentation is very important so be mindful of it 
