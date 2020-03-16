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
import sys, io

from bank import Bank
from part2 import part2

class TestBankLab(unittest.TestCase):

    def test_part2(self):
        """
        Test to make sure students code matches described state
        """
        print("\n\nTESTING PART2 FUNCTION:")
        f = open("test_output.txt", "r")
        expected_output = f.read()
        f.close()
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        part2()
        output = sys.stdout.getvalue()
        sys.stdout = stdout
        print(output)
        print("TEST COMPLETE. TEST RESULT:")
        self.assertEqual(output, expected_output)

    def test_transfer0(self):
        """
        Test simple transfer that should be successful
        """
        # stdout = sys.stdout
        # sys.stdout = io.StringIO()
        print("\n\nTESTING TRANSFER SCENARIO 0:")
        hsbc = Bank("HSBC")
        hsbc.add_account("Han")
        hsbc.deposit("Han", 200)
        hsbc.add_account("Proctor")
        test0 = hsbc.transfer("Han", "Proctor", 100)
        test1 = hsbc.check_balance("Han")
        test2 = hsbc.check_balance("Proctor")
        print("TRANSFER SCENARIO 0 COMPLETE. TEST RESULT:")
        self.assertTrue(test0)
        self.assertEqual(test1, 100)
        self.assertEqual(test2, 100)
        # output = sys.stdout.getvalue()
        # sys.stdout = stdout

    def test_transfer1(self):
        """
        Test transfer that should be unsuccessful due to insufficient funds
        """
        # stdout = sys.stdout
        # sys.stdout = io.StringIO()
        print("\n\nTESTING TRANSFER SCENARIO 1:")
        hsbc = Bank("HSBC")
        hsbc.add_account("Han")
        hsbc.deposit("Han", 200)
        hsbc.add_account("Proctor")
        test0 = hsbc.transfer("Han", "Proctor", 100)
        test1 = hsbc.check_balance("Han")
        test2 = hsbc.check_balance("Proctor")
        test3 = hsbc.transfer("Han", "Proctor", 150)
        test4 = hsbc.check_balance("Han")
        test5 = hsbc.check_balance("Proctor")
        print("TRANSFER SCENARIO 1 COMPLETE. TEST RESULT:")
        self.assertTrue(test0)
        self.assertEqual(test1, 100)
        self.assertEqual(test2, 100)
        self.assertFalse(test3)
        self.assertEqual(test4, 100)
        self.assertEqual(test5, 100)
        # output = sys.stdout.getvalue()
        # sys.stdout = stdout

    def test_transfer2(self):
        """
        Test transfer that should be unsuccessful due to non-existent transfer_from_acct
        """
        # stdout = sys.stdout
        # sys.stdout = io.StringIO()
        print("\n\nTESTING TRANSFER SCENARIO 2:")
        hsbc = Bank("HSBC")
        hsbc.add_account("Han")
        hsbc.deposit("Han", 200)
        hsbc.add_account("Proctor")
        test0 = hsbc.transfer("Han", "Proctor", 100)
        test1 = hsbc.check_balance("Han")
        test2 = hsbc.check_balance("Proctor")
        test3 = hsbc.transfer("nope", "Proctor", 100)
        test4 = hsbc.check_balance("Han")
        test5 = hsbc.check_balance("Proctor")
        print("TRANSFER SCENARIO 2 COMPLETE. TEST RESULT:")
        self.assertTrue(test0)
        self.assertEqual(test1, 100)
        self.assertEqual(test2, 100)
        self.assertFalse(test3)
        self.assertEqual(test4, 100)
        self.assertEqual(test5, 100)
        # output = sys.stdout.getvalue()
        # sys.stdout = stdout

    def test_transfer3(self):
        """
        Test transfer that should be unsuccessful due to non-existent transfer_to_acct
        """
        # stdout = sys.stdout
        # sys.stdout = io.StringIO()
        print("\n\nTESTING TRANSFER SCENARIO 3:")
        hsbc = Bank("HSBC")
        hsbc.add_account("Han")
        hsbc.deposit("Han", 200)
        hsbc.add_account("Proctor")
        test0 = hsbc.transfer("Han", "Proctor", 100)
        test1 = hsbc.check_balance("Han")
        test2 = hsbc.check_balance("Proctor")
        test3 = hsbc.transfer("Han", "nope", 100)
        test4 = hsbc.check_balance("Han")
        test5 = hsbc.check_balance("Proctor")
        print("TRANSFER SCENARIO 3 COMPLETE. TEST RESULT:")
        self.assertTrue(test0)
        self.assertEqual(test1, 100)
        self.assertEqual(test2, 100)
        self.assertFalse(test3)
        self.assertEqual(test4, 100)
        self.assertEqual(test5, 100)
        # output = sys.stdout.getvalue()
        # sys.stdout = stdout

    def test_transfer4(self):
        """
        Edge cases: transfer to same account (either return true or false but should not increment account)
        """
        # stdout = sys.stdout
        # sys.stdout = io.StringIO()
        print("\n\nTESTING TRANSFER SCENARIO 4:")
        hsbc = Bank("HSBC")
        hsbc.add_account("Han")
        hsbc.deposit("Han", 200)
        hsbc.add_account("Proctor")
        test0 = hsbc.transfer("Han", "Proctor", 100)
        test1 = hsbc.check_balance("Han")
        test2 = hsbc.check_balance("Proctor")
        hsbc.transfer("Han", "Han", 100)
        test3 = hsbc.check_balance("Han")
        print("TRANSFER SCENARIO 4 COMPLETE. TEST RESULT:")
        self.assertTrue(test0)
        self.assertEqual(test1, 100)
        self.assertEqual(test2, 100)
        self.assertEqual(test3, 100)
        # output = sys.stdout.getvalue()
        # sys.stdout = stdout

    def test_bug_fix(self):
        """
        Testing to see if student has addressed security flaw.
        """
        # stdout = sys.stdout
        # sys.stdout = io.StringIO()
        print("\n\nTESTING SECURITY BUG SCENARIO:")
        hsbc = Bank("HSBC")
        hsbc.add_account("Han")
        hsbc.deposit("Han", 200)
        hsbc.withdraw("Han", 100)
        test0 = hsbc.withdraw("Han", -1000)
        test1 = hsbc.check_balance("Han")
        print("SECURITY BUG SCENARIO COMPLETE. TEST RESULT:")
        self.assertFalse(test0)
        self.assertEqual(test1, 100)
        # output = sys.stdout.getvalue()
        # sys.stdout = stdout

if __name__ == '__main__':
    unittest.main()
