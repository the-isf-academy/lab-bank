
class Account:
    """An account is one fund in a bank.

    In reality, banks don't keep everyone's money separate, they just put all
    the money together and keep track of how much belongs to each account.
    Banks don't even keep enough money around to pay out everyone's accounts.
    They loan out your money to others for a profit and just keep enough for
    the amount they expect people to withdraw. In the past, there have been
    times when something scary happened and everybody wanted to take their
    money out at once and there wasn't enough. This is called a
    "run on the bank."

        Args:
            name: A string for the account name.

        Example::

            >>> from account import Account
            >>> my_money = Account("Piggy bank")
            Account Piggy bank            | Account opened.
            >>> my_money.deposit(100)
            Account Piggy bank            | Deposited 100. New balance is 100.
            >>> my_money.withdraw(50)
            Account Piggy bank            | Withdrew 50. New balance is 50.
            >>> my_money.withdraw(200)
            Account Piggy bank            | Can't withdraw 200. Insufficient balance.
    """

    def __init__(self, name):
        """The Account constructor creates a new Account instance.
        """
        self.name = name
        self.balance = 0
        self.report("Account opened")

    def deposit(self, amount):
        """Deposits funds into the account, checking that amount is not negative.

        Args:
            amount (float): How much to deposit.

        Returns:
            bool: Whether the deposit succeeded.
        """
        self.balance += amount
        note = "Deposited {}. New balance is {}"
        self.report(note.format(amount, self.balance))
        return True

    def withdraw(self, amount):
        """Withdraws funds from the account if possible.

        Args:
            amount (float): How much to withdraw.

        Returns:
            bool: Whether the withdrawal succeeded.
        """
        if amount > self.balance:
            note = "Can't withdraw {}. Insufficient balance"
            self.report(note.format(amount, self.name))
            return False
        else:
            self.balance -= amount
            note = "Withdrew {}. New balance is {}"
            self.report(note.format(amount, self.balance))
            return True

    def check_balance(self):
        """Reports the balance of the account

        Args:
            account_name (str): The account name.

        Returns:
            The account balance.
        """
        note = "Current balance is {}"
        self.report(note.format(self.balance))
        return self.balance

    def report(self, activity):
        """Prints out a report of activity.

        Args:
            activity (str): A description of what happened.
        """
        print("{:<30}| {}.".format("Account " + self.name, activity))
