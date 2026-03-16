file = open("data.txt", "r")
print(file.read())
file.close()



#read the first row
file = open("data.txt", "r")
print(file.readline())
file.close()



file = open("data.txt", "r")
print(file.readline())
print(file.readline())
file.close()



file = open("data.txt", "r")
print(file.read(5))
file.close()



file = open("data.txt", "r")
lines = file.readlines()
print(lines)
file.close()




file = open("data.txt", "r")
for line in file:
    print(line)
file.close()




file = open("data.txt", "r")
i = 1
for line in file:
    print(i, line)
    i += 1
file.close()



file = open("data.txt", "r")
text = file.read(10)
print(text)
file.close()




file = open("data.txt", "r")
text = file.read()
print(len(text))
file.close()




file = open("data.txt", "r")
text = file.read()
print(text.upper())
file.close()