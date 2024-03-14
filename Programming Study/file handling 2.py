file2 = open('sample02.txt','a')

import datetime as time

currentTime = time.datetime.now()
timeStamp = currentTime.strftime('%d-%m-%Y %H:%M:%S')


file2.write('\n' + timeStamp)
file2.close()