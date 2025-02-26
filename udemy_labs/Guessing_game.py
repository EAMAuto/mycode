while True:
    answer = int(input('When waas python 1.0 released? '))
    if answer < 1994:
        print('It was later than that')
    elif answer > 1994:
        print('It was earlier than that')
    else:
        print('Correct')
        break
