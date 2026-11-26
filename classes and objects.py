#class car:
#    def __init__(self,make,model,year):
#        self.make=make
#        self.model=model
#        self.year=year
#    def display_info(self):
#        print(f"car:{self.year}{self.make}{self.model}")

#car1=car("toyota","corolla",2021)
#car2=car("ford","mustang",2023)
#car1.display_info()
#car2.display_info()

#class person:
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    def greet(self):
#        print(f"hello,my name is{self.name} and i am {self.age}yearsold.")
#person1=person("alice",30)
#person1.greet()

class Dog:
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
    def bark(self):
        print(f"{self.name} says woof!")
    dog1= Dog("labrador","buddy")
    print(dog1.breed)
    dog1.bark()

               
