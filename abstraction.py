from abc import ABC , abstractmethod

class shape(ABC): #abstract class 
    @abstractmethod
    def area(self):
        pass
class Rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width * self.height
#shape = shape() #TypeError: can't instantiate abstract class shape
rectangle = Rectangle(10,20)
print(rectangle.area())