file = open("something.txt", "r")
data = file.read()
print(data)
file.close()

file = open("somefile.txt", "w")
file.write("Hello, World!")
file.close()