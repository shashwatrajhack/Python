class BMW:
    def fuel_type(self):
        print("Diesel")

class Ferrari:
    def fuel_type(self):
        print("petrol")

def car_details(obj):
    obj.fuel_type()

bmw = BMW()
ferrari = Ferrari()

car_details(bmw);
car_details(ferrari);
