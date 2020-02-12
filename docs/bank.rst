Bank
====

.. automodule:: bank
   :members:

.. py:method:: transfer(source_account_name, destination_account_name, amount)

   NOTE: THIS METHOD IS NOT YET IMPLEMENTED!

   Moves the amount from a source account to a destination account name if 
   there are accounts with both names in this :py:class:`Bank` and if there are 
   sufficient funds in the source account. Reports to the user what happened.

   :param str source_account_name: Name of the source account.
   :param str destination_account_name: Name of the destination account.
   :param float amount: How much money to transfer.
   :return: Whether the transfer succeeded.
   :rtype: bool
