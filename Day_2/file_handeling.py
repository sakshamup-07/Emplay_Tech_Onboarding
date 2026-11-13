with open("Day_2/employee.txt" , "r+") as file:
    content = file.read()
    print(content)
    file.write("\naryan")
    print(content)