file = open("file1.txt", "w")
file.write("Hello")
file.close()




file = open("file2.txt", "w")
file.write("Python is easy")
file.close()




file = open("file3.txt", "w")
file.write("Line 1\n")
file.write("Line 2\n")
file.close()




file = open("numbers.txt", "w")
file.write(str(100))
file.close()




text = input("Enter text: ")
file = open("user.txt", "w")
file.write(text)
file.close()




file = open("words.txt", "w")
file.write("Apple ")
file.write("Banana ")
file.write("Orange")
file.close()




file = open("count.txt", "w")
for i in range(5):
    file.write(str(i) + "\n")
file.close()




file = open("date.txt", "w")
file.write("2026")
file.close()




file = open("name.txt", "w")
file.write("Ali")
file.close()




file = open("city.txt", "w")
file.write("Almaty")
file.close()