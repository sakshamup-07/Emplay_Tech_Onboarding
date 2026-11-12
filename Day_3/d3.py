#exception handeling
# try:
#     a = 10
#     b = 0

#     print(a / b)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# try:
#     age = int(input("Enter your age: "))
#     result = 100 / age

# except ValueError:
#     print("Please enter a valid number")

# except ZeroDivisionError:
#     print("Age cannot be zero")
# try:
#     number = int(input("Enter a number: "))
#     print(number * 2)

# except ValueError:
#     print("Invalid input")
#     if number == 2:
#      raise ValueError("cant be 2")

#     else:
#       print("Operation successful")
# finally:
#     print("exe complete")

import random

print(random.randint(1, 10))
print(random.choice(["Python", "Java", "C++"]))
from datetime import datetime, date

today = date.today()
current_time = datetime.now()

print(today)
print(current_time)