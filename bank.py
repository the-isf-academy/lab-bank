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

    def check_balance(self, account_name):
        """ Checks the balance of an account if one exists

        Returns:
            The balance of the account or None if the account doesn't exist.
        """
        if self.account_exists(account_name):
            acct_balance = self.accounts[account_name].check_balance()
            note = "Checking balance of {}"
            self.report(note.format(account_name))
            return acct_balance
        else:
            note = "No account named {}"
            self.report(note.format(account_name))
            return None

    def report(self, activity):
        """Prints out a successful activity.
        """
        print("{:30}| {}.".format("Bank " + self.name, activity))


    def transfer(self, transfer_from_acct, transfer_to_acct, amount):
        """ Transfers money between two accounts if the transfer_from_acct has sufficient funds to complete the transfer

        Returns:
            Whether the transfer was successful
        """
        # ➡️======== 💻 DELETE THIS LINE AND WRITE YOUR TRANSFER() CODE HERE 💻 ========⬅️
        pass
