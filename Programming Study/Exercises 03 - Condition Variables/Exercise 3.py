try:
    score = float(input('please enter a score between 0.0 & 1.0:\n'))
    if score > 1.0 or score < 0.0:
        print('bad score')
    elif score >= 0.9:
        print('Your grade is an A!')
    elif score >= 0.8:
        print('Your grade is a B!')
    elif score >= 0.7:
        print('Your grade is a C!')
    elif score >= 0.6:
        print('Your grade is a D!')
    elif score < 0.6:
         print('Your grade is an F!')
    else:
        print('bad score')

except:
    print('bad score')
