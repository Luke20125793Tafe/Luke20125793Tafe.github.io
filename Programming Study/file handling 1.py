
file = open("sample01.txt", "r")
content = file.read()
myList = []

for line in file:
    myList.append(line.strip())

print(myList)

file.close()

print(content)