# data = ["saksham" , "ravi" , "srthak" , 24 , 56 , 24]
# data.append("hello")
# data.extend([100 , "sahlu" , 200])
# # print(data)
# # print(data[-1])
# # print(data[2])
# data.insert(2 , "shyaam")
# print(data)
# print(len(data))
# print(data[2 : 10 : 1]) #start then end then step

# tupple = ("saksham" , 22 , "ritik")
# print(type(tupple))  #tupples are immutable unlike list
# tupple = (100,) + tupple[1:] # , is to distnguish single tupple from expression
# print(tupple)
# print(tupple.count("ritik")) #only these 2 builtin func
# print(tupple.index("ritik"))

# employee =("saksham " , "rajesh" , "saurav" , " krishna")
# name1  , name2 , name3 , name4 = employee
# print(name1)  //NOTE - PARTIAL UNPACKING
# print(name2)
# print(name3) #these are tupple unpacking

#  #sets 

# # numbers = {1 , 2 , 2,2,3 , "shahstri"}
# # print(numbers)
# # empty_set = set() #this will create empty set 
# # numbers.update(["shahstri" ,"ravi"])
# # print(numbers)
# # numbers.discard("ravi")
# # numbers.remove(2) #throws error if element do not exists unlike discard
# frontend ={"saksham" , "ritesh" , "jarvis"}
# backend = {"saksham" , "ritesh" ,"hari"}
# print(frontend.union(backend))
# print(frontend.intersection(backend)) //NOTE ---type cast to tupple and iterate
# print(frontend.difference(backend))
# print(frontend ^ backend)
# unique_data = set(data)
# print(unique_data)


# =====Dictionaries
arsonal ={
    "name" : "saksham",
    "age" : 22,
    "role" : "swe"
}
print(arsonal)
print(arsonal["age"])
print(arsonal.get("city" , "not avl")) # the second statement execute if the key does not exist
arsonal["city"] = "haridwar"
arsonal["age"] = 50
print(arsonal)
arsonal.update({
    "name" : "friday",
    "age":20
})
for i in arsonal.keys():
    print(i)
    employees = {
    "emp101": {
        "name": "Rahul",
        "age": 25,
        "salary": 50000
    },
    "emp102": {
        "name": "Priya",
        "age": 24,
        "salary": 60000
    }
}

print(employees["emp101"]["name"])
print(employees["emp102"]["salary"])

#python comprehension

square = [i**2 for i in range(1,6)]
print(square)

def greet(name, message="Welcome"):
    print(message, name)

greet("Saksham")
greet("Saksham", "Good morning")
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication

x, y, z = calculate(10, 5) #multiple values returned with tupple unpacking

print(x)
print(y)
print(z)

def test(*args):
    print(args)

test("Saksham", "Python", 22)
def test2(**kwargs):
    print(kwargs)

test2(name="Saksham", skill="Python", age=22)
