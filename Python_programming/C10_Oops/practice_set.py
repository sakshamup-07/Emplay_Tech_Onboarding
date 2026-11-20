class Programmer():
    company = 'Microsoft'
    def __init__(self, name, product):
        self.name = name
        self.product = product
p = Programmer('Saksham', 'GitHub')
print(p.name)
print(p.product)
print(p.company)

#Q2
@staticmethod
class calci:
    @staticmethod
    def __init__(self, x):
        self.x = x
    def square(self):
        print("The square of the number is: ", self.x*self.x)
a = calci(5)
a.square()