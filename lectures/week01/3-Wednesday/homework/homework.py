#### 1. Tip Calculator
total = input('The total bill amount: ')
service = input('''
                1. good
                2. average
                3. bad ''')
if service == 1:
    tip = bill * 0.20
else:
    tip = bill * 0.15
