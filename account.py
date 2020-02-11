
class Account:
    """An account is 
    """

    def __init__(self, name):
        """The Account constructor creates a new Account instance.

        Args:
            name: A string for the account name.
        """
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        """Deposits funds into the account, checking that amount is not negative.

        Returns:
            Whether the deposit succeeded.
        """
        self.balance += amount
        note = "Deposited {}. New balance is {}"
        self.report(note.format(amount, self.balance))
        return True

    def withdraw(self, amount):
        """Withdraws funds from the account. Amount must not be negative.

        Returns:
            Whether the withdrawal succeeded.
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

    def report(self, activity):
        """Prints out a report of activity.
        """
        print("{:<30}| {}.".format("Account " + self.name, activity))

