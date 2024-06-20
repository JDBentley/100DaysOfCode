#Take two names and determine the love rating.
#Getting inputs
name_one = input('What is the first name? ').lower()
name_two = input('What is the second name? ').lower()

#Logic
counter_one = 0
counter_two = 0
for i in name_one:
    if i == 't' or i == 'r' or i == 'u' or i =='e' or i == 'l' or i == 'o' or i == 'v':
        counter_one += 1

for i in name_two:
    if i == 't' or i == 'r' or i == 'u' or i =='e' or i == 'l' or i == 'o' or i == 'v':
        counter_one += 1
    
true = str(counter_one)
love = str(counter_two)
score = true + love

#Returning results
print(f'Your love score is {score}')