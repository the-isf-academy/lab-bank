# Testing file for bank lab
# By: Chris Proctor and Jacob Wolf

# =============================================================================
# ☕️ More-Than-You-Need-To-Know Lounge ☕️
# =============================================================================
# Welcome to the More-Than-You-Need-To-Know Lounge, a chill place for code that
# you don't need to understand.

# Thanks for stopping by, we hope you find something that catches your eye.
# But don't worry if this stuff doesn't make sense yet -- as long as we know
# how to use code, we don't have to understand everything about it.

# Of course, if you really like this place, stay a while. You can ask a
# teacher about it if you're interested.
#
# =============================================================================

import unittest

from bank import Bank

class TestBankLab(unittest.TestCase):

    def test_transfer0(self):
        """
        Test simple transfer that should be successful
        """
        hsbc = Bank("HSBC")
        hsbc.add_account("Han")
        hsbc.deposit("Han", 200)
        hsbc.add_account("Proctor")
        self.assertTrue(hsbc.transfer("Han", "Proctor", 100))
        self.assertEqual(hsbc.check_balance("Han"), 100)
        self.assertEqual(hsbc.check_balance("Proctor"), 100)

    def test_transfer1(self):
        """
        Test transfer that should be unsuccessful due to insufficient funds
        """
        hsbc = Bank("HSBC")
        hsbc.add_account("Han")
        hsbc.deposit("Han", 200)
        hsbc.add_account("Proctor")
        self.assertFalse(hsbc.transfer("Han", "Proctor", 300))
        self.assertEqual(hsbc.check_balance("Han"), 200)
        self.assertEqual(hsbc.check_balance("Proctor"), 0)

    def test_transfer2(self):
        """
        Test transfer that should be unsuccessful due to non-existent transfer_from_acct
        """
        hsbc = Bank("HSBC")
        hsbc.add_account("Han")
        hsbc.deposit("Han", 200)
        hsbc.add_account("Proctor")
        self.assertFalse(hsbc.transfer("nope", "Proctor", 100))
        self.assertEqual(hsbc.check_balance("Han"), 200)
        self.assertEqual(hsbc.check_balance("Proctor"), 0)

    def test_transfer3(self):
        """
        Test transfer that should be unsuccessful due to non-existent transfer_to_acct
        """
        hsbc = Bank("HSBC")
        hsbc.add_account("Han")
        hsbc.deposit("Han", 200)
        hsbc.add_account("Proctor")
        self.assertFalse(hsbc.transfer("Han", "nope", 100))
        self.assertEqual(hsbc.check_balance("Han"), 200)
        self.assertEqual(hsbc.check_balance("Proctor"), 0)

    def test_transfer4(self):
        """
        Edge cases:
            negative value transfer (should fail)
            transfer to same account (either return true or false but should not increment account)
        """
        hsbc = Bank("HSBC")
        hsbc.add_account("Han")
        hsbc.deposit("Han", 200)
        hsbc.transfer("Han", "Han", 100)
        self.assertEqual(hsbc.check_balance("Han"), 200)

unittest.main()
