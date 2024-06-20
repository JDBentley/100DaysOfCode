#Create a simple Pizza Delivery calculator
#Get inputs
pizza_size = input('What size pizza would you like? (S,M,L)').lower()
pizza_pepperoni = input('Would you like pepperoni? (Y,N)').lower()
pizza_cheese = input('Would you like extra cheese? (Y,N)').lower()

#Prices
small = 15
medium = 20
large = 25

pepper_small = 2
pepper_medlarge = 3

extra_cheese = 1

#Creating logic
price = 0
if pizza_size == 's':
    price = small
    if pizza_cheese == 'y':
        price += pepper_small
    else:
        price = price
    if pizza_cheese == 'y':
        price += extra_cheese
    else:
        price = price
if pizza_size == 'm':
    price = medium
    if pizza_cheese == 'y':
        price += pepper_medlarge
    else:
        price = price
    if pizza_cheese == 'y':
        price += extra_cheese
    else:
        price = price
elif pizza_size == 'l':
    price = large
    if pizza_cheese == 'y':
        price += pepper_medlarge
    else:
        price = price
    if pizza_cheese == 'y':
        price += extra_cheese
    else:
        price = price


#Returning price
print(f'Your total is price {price}')