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