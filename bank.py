from account import Account

class Bank:
    """A Bank has many accounts.

    Args:
        name (str): The bank's name.

    Example::

        >>> from bank import Bank
        >>> bank = Bank("Supersafe Ltd")
        Bank Supersafe Ltd            | Open for business.
        >>> bank.add_account("Heihei")
        Bank Supersafe Ltd            | added an account named Heihei.
        >>> bank.deposit("Heihei", 400)
        Account Heihei                | Deposited 400. New balance is 400.
        Bank Supersafe Ltd            | Deposit of 400 to Heihei accepted.
    """

    def __init__(self, name):
        """The Bank constructor creates a new Bank instance.
        """
        self.name = name
        self.accounts = {}
        self.report("Open for business")

    def add_account(self, account_name):
        """Adds a new account to the bank if allowed.

        Returns:
            bool: Whether the request succeeded.
        """
        if self.account_exists(account_name):
            note = "Add account rejected. An account named {} already exists"
            self.report(note.format(account_name))
            return False
        else:
            self.accounts[account_name] = Account(account_name)
            note = "Added an account named {}"
            self.report(note.format(account_name))
            return True

    def account_exists(self, account_name):
        """Checks whether an account exists.

        Args:
            account_name (str): The account name.

        Returns:
            bool: Whether the account exists.
        """
        return account_name in self.accounts.keys()

    def deposit(self, account_name, amount):
        """Accepts a deposit into an account.

        Args:
            account_name (str): The account name.
            amount (float): The amount to deposit.

        Returns:
            bool: Whether the deposit succeeded.
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
        """Withdraws money from an account if possible.

        Args:
            account_name (str): The account name.
            amount (float): The amount to withdraw.

        Returns:
            bool: Whether the withdrawal succeeded.
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

        Args:
            account_name (str): The account name.

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

        Args:
            activity (str): A description of what happened.
        """
        print("{:30}| {}.".format("Bank " + self.name, activity))



# ➡️ ======== 💻 DELETE THIS LINE AND WRITE YOUR TRANSFER() CODE HERE 💻 ========⬅️
