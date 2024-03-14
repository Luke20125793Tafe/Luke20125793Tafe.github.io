try:
        hours = float(input('enter your hours worked:\n'))
        pay = float(input('enter your p/h rate:\n'))
except:
        print('please only use numbers')

def computepay(h, p):
        payOT = p*1.5
        if h > 40:
            ot =  (h - 40)*(payOT)
            subTotal = 40*pay
            totalPay = subTotal+ot
            return totalPay
        else:
            totalPay = hours*pay
            return totalPay


Totalpay = computepay(hours, pay)
print('Pay', Totalpay)
