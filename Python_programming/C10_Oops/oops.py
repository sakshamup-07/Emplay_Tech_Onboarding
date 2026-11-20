class Employee:
    name = "Saksham"
    salary = 9999999999
    age = 22
    def multi(self, x):
        print(self.age*x)

dep = Employee()
print(dep.name)
dep.multi(5)