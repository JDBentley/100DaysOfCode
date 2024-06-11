#Switch the value in two variables
a = input()
b = input()

#solution - use a third variable
c = a
a = b
b = c

#static code - don't change
print('a: ' + a)
print('b: ' + b)