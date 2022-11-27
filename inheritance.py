# its seimple cod for show object inheritance and super()function
'''
salam haji ino faghat zadam k super va ears bari ro nshon bedam
'''
#my code get 4 valiu and giv you a introduction

class Student: 
    def __init__(self, typ, name, age):
        self.name = name
        self.age = age
        self.typ = typ

    def show_introduction(self):        
        result = []
        result.append((f"My name is {self.name} and {self.age} years old im {typ} of University of tehran"))
        print(result)
        return result



class Master(Student):
    def __init__(self, typ, name, age, record):
        super().__init__(typ, name, age)
        self.record = record
    def show_introduction(self):
        super().show_introduction()


class Employee(Student):
    def __init__(self, typ, name, age, respons):
        super().__init__(typ, name, age, )
        self.respons = respons
    def show_introduction(self):
        super().show_introduction()
    

typ = input('Please enter your type (1.Master/2.Employee/3.Student)->>')
name = input('Please enter your name->>')
age = input('Please enter your age->>')

if typ =='1':
    typ = "Master"
    record = input('Please enter your record->>')
    Master(typ ,name, age, record).show_introduction()

if typ =='2':
    typ = 'Employee'
    respons = input('Please enter your respons->>')
    Employee(typ, name, age, respons).show_introduction()
    
elif typ =='3':
    typ = "Student"
    Student(typ, name, age).show_introduction()




    