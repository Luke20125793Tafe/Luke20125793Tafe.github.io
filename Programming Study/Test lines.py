marks = [] #list
marks2 = {} #dictionary
marks3 = () #tuple

keepreading = True

while keepreading:
        mark = int(input("enter score: "))
        if mark == -99 :
            keepreading = False
        else:
            marks.append(mark)

#math time. get totals and averages
Totalmarks = 0
nrmarks = len(marks)
for mark in marks:
    Totalmarks = Totalmarks + mark
average = Totalmarks / nrmarks

for mark in marks:
    if mark >= average :
        print(mark," *")
    else:
        print(mark)
