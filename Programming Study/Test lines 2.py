import sys

enjoy = [1,2,3,4,5,6,7,8,9,10]
#scale of enjoyment from 1 - 10
a = int(input('On a scale of 1 - 10, how much do you enjoy cakes:\n'))
if a in enjoy [:3]:
        sys.stdout.write('thats unfortunate')
if a in enjoy [3:6]:
        sys.stdout.write('an enjoyer of cakes')
if a in enjoy [6:]:
         sys.stdout.write('a huge fan of cakes I see')
