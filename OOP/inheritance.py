class Car:
    @staticmethod
    def start():
        print("Start")

    @staticmethod
    def stop():
        print("Stop")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
        

car1 = ToyotaCar("Fortuner");

print(car1.name)
print(car1.start())

class Employee:
    bonus = 2000
    def show(self):
        print("This is an employee class")

class Manager(Employee):
    bonus1 = 5000
    def display(self):
        print("This is manager class")


e1 = Employee();
e1.show()
m1 = Manager()

m1.display()

print(m1.bonus)