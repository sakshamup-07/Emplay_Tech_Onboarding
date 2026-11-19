# Q1
def greatest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(greatest_of_three(10, 20, 15))

#Q2
print('a')
print('b' , end='')  # end parameter used here to avoid new line after each print
print('c' )

#Q3
def sofnnn(n):
    if n == 1:
        return 1
    else:
        return n + sofnnn(n-1)
print(sofnnn(5)) 

#Q4
def is_palindrome(s):
    return s == s[::-1]  # slicing used here to reverse the string
print(is_palindrome("racecar"))

def multitable(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
multitable(5)