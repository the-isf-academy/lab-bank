from bank import Bank

hsbc = Bank("HSBC")
sc = Bank("Standard Chartered")

hsbc.add_account("Wolf")
hsbc.add_account("Han")
hsbc.deposit("Wolf", 110)
hsbc.check_balance("Han")
hsbc.deposit("Han", 240)
hsbc.withdraw("Han", 100)
hsbc.withdraw("Han", 100)
hsbc.withdraw("Han", 100)
hsbc.check_balance("Han")
