"""Let p be a bank’s interest rate in percent per year. An initial amount
A has then grown to

    A(1 + p / 100) ** n
        
after n years. Make a program for computing how much money 1000
euros have grown to after three years with 5% interest rate. Name of
program file: interest_rate.py ."""

x = 1; initial_amount = 1000

result = initial_amount * (1 + (5 / 100)) * 3
print('Money will grown after three years %.2f' % result)
