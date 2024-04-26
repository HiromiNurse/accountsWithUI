class Account:

    def __init__(self, name, balance=0, MINIMUM=0, atype='checking'):
        self.__name = name
        self.__balance = balance
        self.MINIMUM = MINIMUM
        self.set_balance(balance)
        self.atype = atype

    def withdraw(self, amount):
        """
        Function withdraw amount from account total
        :param amount: Int Amount to withdraw
        :return: boolean
        """
        if (amount > 0) and ((self.__balance - amount) >= self.MINIMUM):  # Make sure it works
            self.__balance -= amount
            return True
        else:
            raise ChildProcessError

    def get_balance(self):
        """
        :return: Int account balance
        """
        return self.__balance

    def get_name(self):
        """
        :return: Str account name
        """
        return self.__name

    def set_balance(self, value):
        """
        Function Set's the account's balance
        :param value: Int to set account balance to
        """
        if value > self.MINIMUM:
            self.__balance = value
        else:
            self.__balance = self.MINIMUM

    def set_name(self, value):
        """
        Function Change account name to value
        :param value: String to set name to
        """
        self.__name = value

    def deposit(self, amount):
        """
        Function Adds the amount to the account balance
        :param amount: Int to add to account balance
        :return: boolean
        """
        if amount > 0:
            x = self.get_balance() + amount
            self.set_balance(x)
        else:
            raise ChildProcessError

    def __str__(self):
        return f"Account name = {self.get_name()}, Account balance = {self.get_balance():.2f}"


class SavingAccount(Account):
    MINIMUM = 100
    RATE = 0.02

    def __init__(self, name, deposit_count=0):
        super().__init__(name, SavingAccount.MINIMUM, SavingAccount.MINIMUM, atype='saving')
        self.__deposit_count = deposit_count

    def apply_interest(self):
        """
        Function Adds interest to the account balance
        """
        if ((self.__deposit_count % 5) == 0) and (self.__deposit_count != 0):
            x = self.get_balance() * (1 + SavingAccount.RATE)
            self.set_balance(x)

    def deposit(self, amount):
        """
        Function Adds the amount to the account balance
        :param amount: Int to add to account balance
        """
        if amount > 0:
            super().deposit(amount)
            self.__deposit_count += 1
            self.apply_interest()
        else:
            raise ChildProcessError

    def get_deposit_count(self):
        return self.__deposit_count

    def __str__(self):
        line = super().__str__().split(", ")
        return f"SAVING ACCOUNT: {line[0]}, {line[1]}"
        # return f"SAVING ACCOUNT name: {self.get_name()}, SAVING ACCOUNT balance: {self.get_balance():.2f}"
