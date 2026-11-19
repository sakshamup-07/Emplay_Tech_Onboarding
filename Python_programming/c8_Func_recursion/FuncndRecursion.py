def greet(name , ending = "Good Morning"):
    print(f"Hello {name} {ending}")
greet("Saksham")  # default argument used here
greet("Alice", "Good Evening")  # custom argument used here

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))  # recursion used here

def sumer(x):
    if x == 0:
        return 0
    else:
        return x + sumer(x-1)
print(sumer(5))  # recursion used here