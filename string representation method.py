#class Book:
#    def __init__(self,title,author):
#        self.title =title
#        self.author =author
#    def __str__(self):
#        return f"'{self.title}'by {self.author}"
#book=Book("1984","george orwell")
#print(book)    

#class variables vs instance variables
#class Employee:
#    company = "ABC Corp" #class variable

#    def __init__(self,name,position):
#        self.name=name #instance variable
#        self.position=position #instance variable
#emp1=Employee("john","manager")
#emp2=Employee("alice","developer")

# accessing class variable
#print(emp1.company) #abc corp
#print(emp2.company) #abc corp

#accessing instance variable
#print(emp1.name) #john
#print(emp2.name) # alice              

#encapsulation
class Employee:
    def __init__(self,name,salary):
        self.name=name #public attribute
        self.__salary=salary #private attribute

    def display_employee(self):
        print(f"name:{self.name},salary:{self.__salary}")
    def update_salary(self,new_salary):
        self.__salary += new_salary
emp=Employee("John",50000)
emp.display_employee()

emp.update_salary(20000)
emp.display_employee()
#trying to access private attribute directly (will raise an error)
#print(emp.__salary)

emp.name="jake"
emp.display_employee()

emp.__salary=1000000
emp.display_employee()