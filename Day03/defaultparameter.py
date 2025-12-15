def greet(name,msg="Hello"):
    print(msg,name)

greet("Alice")
greet("Bob","Good Morning")

def name(name,surname="Darure"):
    print(name,surname)
name("Pranita")

def student(name,age,course):
    print(name,age,course)

student(age=20, name="Pranita", course="Python")

def add(a,b):
    return a+b

def operator(func,x,y):
    return func(x,y)

print(operator(add,7,8))