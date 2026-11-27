class Employee :
    company = "Emplay"
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(self.salary , self.name)
class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)  
    def __init__(self, name , salary , language):
        self.language = language
        self.salary=salary
        self.name=name
    def showlanguage(self):
        print(self.language)
dev = Developer("Saksham", 57000, "Python")
dev.display()
dev.showlanguage()

def avg(*args):
    total=0
    num=0
    for i in args:
        total +=i
        num+=1
    return total/num