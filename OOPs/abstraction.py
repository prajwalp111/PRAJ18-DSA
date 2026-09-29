class ATM:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    atm = ATM(1000)
    print(f"Initial Balance: {atm.get_balance()}")
    
    atm.deposit(500)
    atm.withdraw(200)
    atm.withdraw(1500)  # Attempt to withdraw more than the balance
    print(f"Final Balance: {atm.get_balance()}")