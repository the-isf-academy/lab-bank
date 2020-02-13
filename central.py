"""An example of how banks and accounts can work together to create an ecomony.

In this example, we only need to import Bank, because the Bank will take care of
its own accounts. (If you have ever had a bank account, you know that you can't
interact with the account directly. Transactions go through the bank.)
"""

from bank import Bank

hsbc = Bank("HSBC")
sc = Bank("Standard Chartered")

hsbc.add_account("Wolf")
hsbc.add_account("Han")
hsbc.deposit("Wolf", 110)
hsbc.check_balance("Han")
hsbc.deposit("Han", 240)

for amount in range(10):
    if (hsbc.withdraw("Han", amount*10)):
        hsbc.deposit("Wolf", amount*10)
