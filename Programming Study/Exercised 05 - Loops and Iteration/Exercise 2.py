numbers = []
sumNum = 0
countNum = 0
keepNumbering = 0
largestNum = 0
smallestNum = None

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
    if num > largestNum:
        largestNum = num
    elif smallestNum == None or num < smallestNum :
        smallestNum = num
    
print(sumNum, " ", countNum, " ", smallestNum, ":", largestNum)
    