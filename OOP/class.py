# Creating class and object in python

# class Student:
#     name="Karan"

# s1 = Student()

# print(s1.name)

class Employee:
    '''This is employee class for maintaining employee data.'''
    def __init__(self,sal,ag):
        
        self.salary = sal
        self.age = ag

    def display(self):
        print(f"salary is {self.salary} and age is {self.age}");


e1 = Employee(200000,23)
e2 = Employee(100000,24)

# built-in class function

print(getattr(e1,'age'))
setattr(e1,'salary',500000)

print(e1.salary)
print(e2.salary,e2.age)
e2.display()
delattr(e2,'age')

print(hasattr(e2,'age'))

# Built-in class attribute

print(Employee.__dict__);
print(Employee.__doc__);
print(Employee.__name__)
print(Employee.__module__);


