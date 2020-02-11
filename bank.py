from account import Account

class Bank:
    """A Bank has many accounts.
    """

    def __init__(self, name):
        """The Bank constructor creates a new Bank instance.

        Args: 
            name: A string for the bank name.
            verbose: If True, will report on all activity.
        """
        self.name = name
        self.accounts = {}
        self.report("Open for business")

    def add_account(self, account_name):
        """Adds a new account to the bank if allowed.

        Returns:
            Whether the request succeeded.
        """
        if self.account_exists(account_name):
            note = "Add account rejected. An account named {} already exists"
            self.report(note.format(account_name))
            return False
        else:
            self.accounts[account_name] = Account(account_name)
            note = "added an account named {}"
            self.report(note.format(account_name))
            return True

    def account_exists(self, account_name):
        """Checks whether an account exists.
        """
        return account_name in self.accounts.keys()

    def deposit(self, account_name, amount):
        """Accepts a deposit into an account.

        Returns:
            Whether the deposit succeeded.
        """
        if self.account_exists(account_name):
            self.accounts[account_name].deposit(amount)
            note = "Deposit of {} to {} accepted"
            self.report(note.format(amount, account_name))
            return True
        else:
            note = "Deposit of {} rejected. No account named {}"
            self.report(note.format(amount, account_name))
            return False

    def withdraw(self, account_name, amount):
        """Withdraws money from an account.

        Returns:
            Whether the withdrawal succeeded.
        """
        if self.account_exists(account_name):
            success = self.accounts[account_name].withdraw(amount)
            if success:
                note = "Withdrawal of {} from {} accepted"
                self.report(note.format(amount, account_name))
                return True
            else:
                note = "Withdrawal of {} from {} rejected"
                self.report(note.format(amount, account_name))
                return False
        else:
            note = "Withdrawal of {} rejected. No account named {}"
            self.report(note.format(amount, account_name))
            return False

    def report(self, activity):
        """Prints out a successful activity.
        """
        print("{:30}| {}.".format("Bank " + self.name, activity))
