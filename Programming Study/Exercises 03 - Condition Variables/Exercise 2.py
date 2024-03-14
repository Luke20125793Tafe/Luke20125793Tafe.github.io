try:
    hoursWorked = float(input('enter your hours worked:\n'))
    payRate = float(input('enter your p/h rate:\n'))
    
    if hoursWorked > 40:
        totalPay = hoursWorked*(payRate*1.5)
        print ('your total pay comes to: $'+ str(totalPay))
    else:
        totalPay = hoursWorked*payRate
        print ('your total pay comes to: $'+ str(totalPay))
        
except:
    print('please enter a number (eg. 1, ,2 ,3)')



