# Unit 2, Lesson 0

## Use classes

- Run `central.py`
- In Python shell, have students instantiate, interact with classes
- Write another script that plays with classes using loops
    
## Anatomy of a class
 
- declaration line
    - base class
    - docstring
- indentaition
    - attributes
    - methods
        - self argument
        - docstrings
- constructor
    - no return value
- Exceptions
- reading documentation

## Extending classes

New method: 

    Bank.transfer(from_account, to_account, amount)

New attributes:

    Account.password

Implement password-checking on accounts. Should the bank check passwords, or
should the account check them? Are passwords required for transfers?

## Hacking the bank

- Find security issues. 
- Can you fix them? 

## Notes

- Floats are a terrible way to keep track of currency. You may see artifacts 
  like 100.00000000001. This could be an opportunity for a conversation
  about lower levels of abstraction, and possible aternatives (like Decimal).
