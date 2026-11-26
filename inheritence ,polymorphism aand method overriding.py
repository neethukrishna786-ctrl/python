#inheritence
#class animal:
#    def __init__(self,name):
#        self.name=name
#    def speak(self):
#        print(f"{self.name} make sound")

#class dog(animal):
#    pass
#d=dog("jake")
#d.speak()

#polymorphism and method overriding
class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} makes sound")

class dog(animal):
    def speak(self):
        print(f"{self.name} says woof")

class cat(animal):
    def speak(self):
        print(f"{self.name} says meow")

d=dog("jake")
c=cat("tobby")
d.speak()
c.speak()

        
    
