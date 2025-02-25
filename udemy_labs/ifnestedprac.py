answer_a = input('Have you used them at all? y/n ')
answer_b = input('Has the item broken down on its own? y/n ')
answer_c = int(input('How many days ago did you purchase the item? '))
if answer_a == 'n' and answer_c < 10:
    print('you can get a refund')
elif answer_b == 'y':
    print('you can get a refund')
else:
    print('you cannot get a refund.')
