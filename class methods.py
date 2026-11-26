#class mathoperations:
#    @staticmethod
#    def add(a,b):
#        return a+b

#num1=mathoperations()
#print(num1.add(10,20))

class company:
    company_name="tech innovators"

    @classmethod
    def change_company_name(cls,new_name):
        cls.company_name=new_name
company.change_company_name("future solutions")
print(company.company_name)