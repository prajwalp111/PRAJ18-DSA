class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        """"
        Create a new credit card instance.
        The initial balance is zero.
        customer → the name of the customer (e.g., John Bowman)
        bank     → the name of the bank (e.g., California Savings)
        acnt     → the account identifier (e.g., 5391037593875309)
        limit    → credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._acnt

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; 
        False if charge was denied."""

        if price + self._balance > self._limit:
            return False
        else: 
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

if __name__ == "__main__":

    wallet = []
    wallet.append(CreditCard("Bishma Raja", "SBI", "1234 5267 8122 2222", 10000))
    wallet.append(CreditCard("Bishma Raja", "HDFC", "1324 2356 5455 2265", 12000))
    wallet.append(CreditCard("Bishma Raja", "ICICI", "1234 5267 8122 2222", 15000))

    for val in range(1, 17):
        wallet[0].charge(val * 100)
        wallet[1].charge(val * 200)
        wallet[2].charge(val * 300)


    for c in range(3):
        print(f"Customer = {wallet[c].get_customer()}")
        print(f"Bank = {wallet[c].get_bank()}")
        print(f"Account = {wallet[c].get_account()}")
        print(f"Limit = {wallet[c].get_limit()}")
        print(f"Balance = {wallet[c].get_balance()}")

        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(1000)
            print(f"New balance = {wallet[c].get_balance()}")

        print("----------------------------------------")
