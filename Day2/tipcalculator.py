#Tip calculator
print('Welcome to the tip calculator. ')

#Getting inputs
bill = int(input('How much was the total bill? '))
party = int(input('How many members in your party? '))
tip_percent = int(input('What percentage would you like to tip? '))

#Calculating results
bill_share = round(bill / party, 2)
tip = (.1 * tip_percent) * bill_share
total = bill_share + tip

#Returning solution
print(f'Your total amount due is {total}')

