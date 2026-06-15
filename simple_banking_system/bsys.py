from datetime import datetime

class BasicAccount:

    def __init__(self, name, balance):
        self.history = []
        self.name = name
        self.balance = balance
        self.history.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + 
                            f" Account by the name ({name}) was created with initial deposit ($ {balance:.2f})")

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        self.history.append(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            + (
                f" The amount of ($ {deposit_amount:.2f}) has been deposited.  current balance is ($ {self.balance:.2f})"
            )
        )

    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            self.history.append(
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                + (
                    f" The amount of ($ {withdraw_amount:.2f}) has been withdrawn.  current balance is ($ {self.balance:.2f})"
                )
            )
        else:
            print("You do not have sufficient funds")

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
            + (
                f" The amount of ($ {extra:.2f}) has been added as interest.  current balance is ($ {self.balance:.2f})"
            )
        )
