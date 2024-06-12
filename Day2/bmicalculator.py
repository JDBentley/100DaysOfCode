#Create a BMI Calculator for Kilograms
print('Welcome to the 100 days of code BMI Calc. version 1 ')

#Getting inputs
height = input('What is your height in meters? ')
weight = input('How much do you weigh in kilograms? ')

#Performing calculations
bmi = weight / (height * height)

#Returning result
print(bmi)