class Account:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    @property

    def balance(self):
        return self.__balance

    def deposit(self,amount):
        self.__balance+=amount
        print("The balance is",self.__balance)
        return self.__balance

    def withdraw(self,amount):
        if amount>self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance-=amount
            print("The balance is",self.__balance)
        return self.__balance

class SavingsAccount(Account):

    def __init__(self,name,balance,interest_rate):

        super().__init__(name,balance)
        self.interest_rate=interest_rate


    def add_interest(self):
        interest=self.balance * self.interest_rate

        print(f"Adding interest: Rs{interest:.2f}")

        self.deposit(interest)

sa=SavingsAccount("Ram", 50000,0.02)
sa.add_interest()
sa.withdraw(5000)
sa.add_interest()


