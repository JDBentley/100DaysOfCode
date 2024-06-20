#Create a treasure island demo. Basically a choose your own adventure.
choice1 = input('Which direction would you like to go? (left, right): ').lower()
if choice1 == 'left':
    print('Game over nerd')
else:
    print('You turn right through a doorway.')

choice2 = input('You walk up to a dark hole with a log across it. Do you climb across or try to find another way? (climb, search)').lower()
if choice2 == 'climb':
    print('You ded')
else:
    print("Smooth move, you finder a teleporter.")