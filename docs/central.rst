Central (Usage example)
=======================

An example of how banks and accounts can work together to create an ecomony.

In this example, we only need to import Bank, because the Bank will take care of
its own accounts. (If you have ever had a bank account, you know that you can't 
interact with the account directly. Transactions go through the bank.)
::

    from bank import Bank

    hsbc = Bank("HSBC")
    sc = Bank("Standard Chartered")
    
    hsbc.add_account("Wolf")
    hsbc.add_account("Han")
    hsbc.deposit("Wolf", 110)
    hsbc.deposit("Han", 240)
    
    for amount in range(10):
        if hsbc.withdraw("Han", 10 * amount):
            hsbc.deposit("Wolf", 10 * amount)

Here is the resulting transaction log:

.. code-block:: none

    Bank HSBC                     | Open for business.
    Bank Standard Chartered       | Open for business.
    Account Wolf                  | Account opened.
    Bank HSBC                     | added an account named Wolf.
    Account Han                   | Account opened.
    Bank HSBC                     | added an account named Han.
    Account Wolf                  | Deposited 110. New balance is 110.
    Bank HSBC                     | Deposit of 110 to Wolf accepted.
    Account Han                   | Deposited 240. New balance is 240.
    Bank HSBC                     | Deposit of 240 to Han accepted.
    Account Han                   | Withdrew 0. New balance is 240.
    Bank HSBC                     | Withdrawal of 0 from Han accepted.
    Account Wolf                  | Deposited 0. New balance is 110.
    Bank HSBC                     | Deposit of 0 to Wolf accepted.
    Account Han                   | Withdrew 10. New balance is 230.
    Bank HSBC                     | Withdrawal of 10 from Han accepted.
    Account Wolf                  | Deposited 10. New balance is 120.
    Bank HSBC                     | Deposit of 10 to Wolf accepted.
    Account Han                   | Withdrew 20. New balance is 210.
    Bank HSBC                     | Withdrawal of 20 from Han accepted.
    Account Wolf                  | Deposited 20. New balance is 140.
    Bank HSBC                     | Deposit of 20 to Wolf accepted.
    Account Han                   | Withdrew 30. New balance is 180.
    Bank HSBC                     | Withdrawal of 30 from Han accepted.
    Account Wolf                  | Deposited 30. New balance is 170.
    Bank HSBC                     | Deposit of 30 to Wolf accepted.
    Account Han                   | Withdrew 40. New balance is 140.
    Bank HSBC                     | Withdrawal of 40 from Han accepted.
    Account Wolf                  | Deposited 40. New balance is 210.
    Bank HSBC                     | Deposit of 40 to Wolf accepted.
    Account Han                   | Withdrew 50. New balance is 90.
    Bank HSBC                     | Withdrawal of 50 from Han accepted.
    Account Wolf                  | Deposited 50. New balance is 260.
    Bank HSBC                     | Deposit of 50 to Wolf accepted.
    Account Han                   | Withdrew 60. New balance is 30.
    Bank HSBC                     | Withdrawal of 60 from Han accepted.
    Account Wolf                  | Deposited 60. New balance is 320.
    Bank HSBC                     | Deposit of 60 to Wolf accepted.
    Account Han                   | Can't withdraw 70. Insufficient balance.
    Bank HSBC                     | Withdrawal of 70 from Han rejected.
    Account Han                   | Can't withdraw 80. Insufficient balance.
    Bank HSBC                     | Withdrawal of 80 from Han rejected.
    Account Han                   | Can't withdraw 90. Insufficient balance.
    Bank HSBC                     | Withdrawal of 90 from Han rejected.
