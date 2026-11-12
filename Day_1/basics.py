
name = "Saksham"
age = 22
height = 5.10
is_employed = True

print(name)
print(age)
print(type(name))
print(type(height))

print("My name is", name, "and I am", age, "years old")

a = 20
b = 7

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** 2)

age = 22

if age >= 18:
    print("Adult")
else:
    print("Minor")

marks = 78

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Needs improvement")

for i in range(1, 10):
    print(i)

count = 5

while count > 0:
    print(count)
    count -= 1

languages = ["Python", "Java", "C++", "JavaScript"]

print(languages)
print(languages[0])
print(languages[-1])

languages.append("SQL")
languages.remove("Java")

print(languages)

employee = {
    "name": "Saksham",
    "age": 22,
    "department": "Engineering"
}

print(employee["name"])
print(employee["department"])

employee["role"] = "Software Engineer"
print(employee)

numbers = [10, 20, 30, 40, 50]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

for num in numbers:
    if num % 2 == 0:
        print(num, "is even")

username = input("Enter your name: ")
print("Welcome", username)

user_age = int(input("Enter your age: "))
print("Next year you will be", user_age + 1)
