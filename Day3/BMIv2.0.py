#Take BMI Exercise and output classification
#Taking inputs
height = float(input('Inser your height here in meters: '))
weight = int(input('Input your weight here in kg: '))

#Calculating BMI
bmi = weight/(height * height)

#Outputting classification
print(f'Your BMI is {bmi}')
if bmi <= 18.5:
    print('You are undeweight')
elif bmi > 18.5 | bmi < 25:
    print('You are a normal weight')
elif bmi >= 25 and bmi < 30:
    print('You are slightly overweight.')
elif bmi >= 30 and bmi < 35:
    print('You are obese')
else:
    print('You are clinically obese')