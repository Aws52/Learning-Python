from datetime import datetime

class BasicAccount:

    history = []

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + 
                            f" Account by the name ({name}) was created with initial deposit ($ {balance:.2f})")

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        self.history.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + 
                            (f" The amount of ($ {deposit_amount:.2f}) has been deposited."))

    def withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount
        self.history.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + 
                            (f" The amount of ($ {withdraw_amount:.2f}) has been withdrawn."))

    def show_transactions_history(self):
        print("\n".join(self.history))


class SavingsAccount(BasicAccount):

    def __init__(self, name, balance):
        super().__init__(name, balance)

    def apply_interest(self, rate):
        extra = rate * self.balance
        self.balance += extra 
        self.history.append(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            + (f" The amount of ($ {extra:.2f}) has been added as interest.")
        )

