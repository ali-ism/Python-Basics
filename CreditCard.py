class CreditCard:
    def __init__(self,customer,bank,acnt,limit,balance = 0):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = balance
        
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_acnt(self):
        return self._acnt
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self,price):
        try:
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True
        except TypeError:
            print("Invalid data type for input Price!")

    def make_payment(self,amount):
        if amount <= 0:
            raise ValueError("Enter an amount greater than zero!")
        try:
            self._balance -= amount
        except TypeError:
            print("Invalid data type for input Amount!")