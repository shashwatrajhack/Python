class Computer(object):
    def __init__(self):
        self.ram = '8gb'
        self.storage = '512gb'
        print("Computer class called..")


class Mobile(Computer):
    def __init__(self):
        super().__init__()

        self.phone = "X-phone"
        print("Mobile class called and access the constructor of parent class computer through super function")

m1 = Mobile()
print(m1.__dict__)
