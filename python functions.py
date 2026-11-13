#def greet():
#    print("hello,world!")

#calling the function
#greet()

#def greet(name):
#    print(f"hello,{name}!")

#calling the function
#greet("Alice")

#positional arguments
#def greet(name,age,place):
#    print(f"my name is {name} and age is {age} and place is {place}")

#calling the function
#greet("Neethu","24","palakkad")

#keyword arguments
#def greet(name,msg="good morning"):
#    print(f"{msg},{name}")

#print("Alice","good morning")

#keyword arguments
#def greet(name,age):
#    print("name:",name)
#    print("age:",age)

#greet(name="nik",age=20)

#default arguments
#def greet(name,age=20):
#    print("name:",name)
#    print("age:",age)

#greet("nik")

#default arguments
#def greet(name,msg="good morning"):
#    print(f"{msg},{name}!")

#greet("alice")

#arbitarary arguments
#def numbers(*a):
#    print(a)

#numbers(1,2,3,4,5,6,7,8,9,10)

#def numbers(*a):
#    print(a)
#    total=0
#    for i in a:
#        total+=i
#    print(total)

#numbers(1,2,3,4,5,6,7,8,9,10)

#def details(**kwargs):
#    for key,value in kwargs.items():
#        print(f"{key}:{value}")

#details(name="alice",age=30,city="new york")

#def info(*args,**kwargs):
#    print("positional arguments:",args)
#    print("keyword arguments:",kwargs)

#info(1,2,3,name="alice",age=25)

#def full_function_example(param1, *args,**kwargs):
#    print("regular parameter:",param1)
#    print("positional parameter:",*args)
#    print("keyword parameter:",**kwargs)

#full_function_example(10,20,30,name="alice",age=30)    

#return statement
#def add(a,b):
#    print(a+b)
#    return a+b

#add(5,6)

#docstring functions
#def add(a,b):
#    """ this function adds two numbers."""
#    return a+b

#print(add.__doc__)

#def multiply(a,b):
#    return a*b

#result=multiply(3,4)
#print(result)






