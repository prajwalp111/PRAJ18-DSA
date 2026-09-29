from abc import ABC, abstractmethod

class Paymnent(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Paymnent):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class UPI(Paymnent):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")       

class NetBanking(Paymnent):
    def pay(self, amount):
        print(f"Paid {amount} using Net Banking.")

def process_payment(payment_method, amount):
    payment_method.pay(amount)

if __name__ == "__main__":
    credit_card = CreditCard()
    upi = UPI()
    net_banking = NetBanking()

    process_payment(credit_card, 100)
    process_payment(upi, 200)
    process_payment(net_banking, 300)