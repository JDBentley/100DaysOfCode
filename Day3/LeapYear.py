#Determine if input year is a leap year
#Getting input year
year = int(input('Input your year here: '))

#Calculating year and returning it
if year % 4 == 0:
    if year % 100 != 0 and year % 400 == 0:
        print('Leap Year')
    else:
        print('Not a leap year')
else:
    print('Not a leap year')