class CheckingAccount:
    def __init__(self, name, address, phoneNo, accountNo, balance, transactionHistory):
        self._name = name
        self._address = address
        self._phoneNo = phoneNo
        self._accountNo = accountNo
        self._balance = float(balance)
        self._transactionHistory = []

    def debit(self, amount):
        if amount > 0:
            self._balance -= amount
            self._transactionHistory.append('Debit of ${}'.format(amount))
            print('Debit of ${}. New balance: ${}'.format(amount, self._balance))
        else:
            print('Debit amount invalid.')

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactionHistory.append('Deposit of ${}'.format(amount))
            print('Deposit of ${} successful. New balance: ${}'.format(amount, self._balance))
        else:
            print('Deposit failed. Invalid amount.')

    def updateAddress(self, newAddress):
        self._address = newAddress
        print('Address has been updated to: {}'.format(newAddress))

    def updatePhoneNo(self, newNumber):
        self._phoneNo = newNumber
        print('Phone Number has been updated to: {}'.format(newNumber))

    def getBalance(self):
        return self._balance
    
    def transactions(self):
        for transaction in self._transactionHistory:
            print(transaction)
    
account = CheckingAccount('April Goodlin', '215 School Drive', '(336) 555-5555', '2214', '204', '')
account.deposit(400)
account.deposit(341)
account.debit(219)
account.debit(11)
account.deposit(32)
print()
account.updateAddress('214 School Drive')
account.updatePhoneNo('(336) 555-5511')
print()
account.deposit(2015)
account.debit(123)
print()
account.transactions
print()
account.getBalance