# part2.py
# Author: [YOUR NAME HERE]
#
# This file should contain a Python program which generates a Bank and Account objects to match the state described in the lab spec sheet.

from bank import Bank

def promotion():
    """
    Function which creates the state of Banks and Accounts described in the lab spec webpage.
    """

    # 💻 YOUR CODE HERE

    hsbc = Bank("HSBC")

    for i in range(10):
        account_name = "Account{}".format(i)
        hsbc.add_account(account_name)
        hsbc.deposit(account_name,i*10)

    bisf = Bank("BISF")

    for i in range(10):
        account_name = "Account{}".format(i)
        bal = hsbc.check_balance(account_name)
        hsbc.withdraw(account_name,bal)

        bisf.add_account(account_name)
        bisf.deposit(account_name,bal)
        bisf.deposit(account_name,bal) 


if __name__ == "__main__":
    part2()
