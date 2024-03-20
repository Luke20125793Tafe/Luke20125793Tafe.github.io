numbers = []
sumNum = 0
countNum = 0
keepNumbering = 0

while keepNumbering < 20 :
    addNum = input("Enter a number: ")
    
    if addNum == "done" or addNum == "Done" :
        break
    else :
        try :
            addNum = int(addNum)
            numbers.append(addNum)
        except :
            print("invalid input")   
            
    keepNumbering = keepNumbering + 1

for num in numbers:
    sumNum = sumNum + num
    countNum = countNum + 1
    avgNum = sumNum / countNum
    
print(sumNum, " ", countNum, " ", avgNum)
    