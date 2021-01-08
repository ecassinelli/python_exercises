# Name: Eduardo Cassinelli
# ID: 260876480

# Cash input by the user.
cash = float(input("Please input the amount: ")) * 100
# Price of the item input by the user 
price = float(input("PLease input the price of product: ")) * 100  

# Change that the machine will give to the user
change = cash - price  

if cash >= price and cash % 5 == 0 and price % 5 == 0:
    toonies = int(change / 200)
    loonie = int((change - toonies * 200) / 100)
    quarter = int((change - toonies * 200 - loonie * 100) / 25)
    dime = int((change - toonies * 200 - loonie * 100 - quarter * 25) / 10)
    nickel = int((change - toonies * 200 - loonie * 100 - quarter * 25 - dime * 10) / 5)

    print('Amount received:', cash)
    print('Cost of the item:', price)
    print('Required change:', change, '\n')

    print('Change:')
    print('    toonies x', toonies)
    print('    loonie x', loonie)
    print('    quarter x', quarter)
    print('    dime x', dime)
    print('    nickel x', nickel)
else:
    print('Please insert the amount of cash equal or greater to the price of the product.')
    print('No pennies accepted.')
    print('Please start again')