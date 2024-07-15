class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initialAmount,accName):
        self.balance=initialAmount
        self.name=accName
        print(f"\nAccount '{self.name}' created.\nBalance=${self.balance:.2f}")

    
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")


    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"\nDeposite Completed.")
        self.getBalance()

    def viableTransaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, amount '{self.name}' only has a balance of ${self.balance:.2f}"
            )
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance=self.balance-amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw intereupted: {error}")

    def transfer(self,amount,account):
        try:
            print('\n*****************************\n\nBeginning Transfer.. ')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Transfer Complete\n**************************")
        except BalanceException as error:
            print(f"Transfer Interrupted.")            



class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance=self.balance+(amount * 1.05)
        print("\nDeposit Completed.")
        self.getBalance()

class SavingAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount,accName)
        self.fee=5

    def withdraw(self, amount):
        return super().withdraw(amount)