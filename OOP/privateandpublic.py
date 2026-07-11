class Account:
    def __init__(self,acc_no,acc_pass):
        self.accountNumber = acc_no
        self.__accountPassword = acc_pass

        
    def reset_pass(self):
        return self.__accountPassword

acc1 = Account("12345","abcde")

print(acc1.accountNumber)
print(acc1.reset_pass())

