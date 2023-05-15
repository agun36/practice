# file = open("file_handling.txt", "r")
# do something with the file
# content = file.readline()
# print(content)
# file.close()

file = open("file_handling.txt", "w")
file.write("This is the written to the file")
file.close()
file = open("file_handling.txt", "r")
content = file.read()
print(content)
file.close()

file = open("file_handling.txt", "w")
file.write("This is the new line")
file.close()
