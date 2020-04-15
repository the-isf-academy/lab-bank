# Unit 2 Lab: Don't break the bank
This lab introduces students to object-oriented programming through buggy banking software. Students work to understanding the way each class works together to create a banking system in order to fix the bugs in the software.

## Getting started

Clone this repo and find the lab walk through here: [cs.fablearn.org](https://cs.fablearn.org/labs/2-0-bank%20lab.html)

## Testing

Files for testing purposes:

- `test_lab.py`
- `test_output.txt`

Along the way, you can test your code by running `python test_lab.py`. Include the `-k part2`, `-k transfer`, or `-k bug` to run tests only for one section of the lab.

Feel free to look into any of the test files, but don't edit them.

## Submission

Commit and push to Github to submit this lab. 

Along the way, make sure you are documenting your progress by making regular commits.

## Lab Sections

This lab has 4 parts:

1. Learn about using OOP in Python
2. Understand the Bank and Account class BISF has developed as part of their accounting system
3. Add a new function to BISF's system
4. Break into the bank -- and propose security fixes for the vulnerabilities

## Notes

- Floats are a terrible way to keep track of currency. You may see artifacts 
  like 100.00000000001. This could be an opportunity for a conversation
  about lower levels of abstraction, and possible aternatives (like Decimal).
