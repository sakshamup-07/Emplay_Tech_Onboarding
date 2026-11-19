fruits = ()
for i in range(7):
    fruit = input("Enter a fruit name: ")
    fruits += (fruit,) 
print(fruits)  

marks = ()
for i in range(5):
    mark = int(input("Enter a mark: "))
    marks += (mark,)
    print(sorted(marks))  # sorted() function used here to sort the marks in ascending order
    