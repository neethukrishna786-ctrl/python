class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display_grade(self):
        if self.marks >=90:
            grade ="A"
        elif self.marks >=75:
            grade="B"
        elif self.marks >=50:
            grade ="C"
        else:
            grade = "Fail"
        print(self.name + "'s grade:",grade)

student1 =student("Alice",85)
student2= student("John",95)

student1.display_grade()
student2.display_grade()