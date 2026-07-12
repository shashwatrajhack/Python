# Creating class and object in python

# class Student:
#     name="Karan"

# s1 = Student()

# print(s1.name)

class Employee:
    def __init__(self,sal,ag):
        self.salary = sal
        self.age = ag

    def display(self):
        print(f"salary is {self.salary} and age is {self.age}");


e1 = Employee(200000,23)
e2 = Employee(100000,24)

print(e1.salary,e1.age)
print(e2.salary,e2.age)

e2.display()
