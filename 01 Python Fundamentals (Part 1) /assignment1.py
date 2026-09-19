# Q1. Write a program that asks the user for their name and age, then prints a sentence like: Hello Shradha, you are 21 years old!

name = input('Enter your name: ')
age = int(input('Enter your age: '))

print(f'Hello {name}, you are {age} years old')
print('--'*50)


# Q2. Take two numbers as input from the user and print their sum, difference, product, and quotient
print('Number 2 should not equal to 0')
num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1/num2

print(f'Sum: {sum}')
print(f'Difference: {difference}')
print(f'Product: {product}')
print(f'Quotient: {quotient:.2f}')
print('--'*50)

# Q3. Ask the user to enter two integers and one float. Convert them all to floats and print their average.
integer1 = float(input('Enter your first integer number: '))
integer2 = float(input('Enter your second integer number: '))
float1 = float(input('Enter your float number: '))

avg = (integer1 + integer2 + float1)/3

print(f'The average value for all three numbers is: {avg:.2f}')
print('--'*50)


''' 
The user enters a string containing a number (e.g., ). Convert it to:Q4 "45". 
• an integer
• a float
• a string again
Print all three values with their types. 
'''
str1 = "45"

str2 = int(str1)
str3 = float(str2)
str4 = str(int(str3))

print(f'The value for str2 is: {str2}, and the datat type is: {type(str2)}')
print(f'The value for str3 is: {str3}, and the datat type is: {type(str3)}')
print(f'The value for str4 is: {str4}, and the datat type is: {type(str4)}')
print('--'*50)


'''
Q.5 Evaluate and print the result of the following expression:
x = 10 + 3 * 2 ** 2
'''
x = 10 + 3 * 2 ** 2
print(f'The value for the expression (x = 10 + 3 * 2 ** 2) is: {x}')
print('--'*50)


#Q.6 Write a program to values of two numbers entered by the use
print('Swap the values of two numbers entered by the users')
num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

print('Before swappinng:')
print(f'Value for num1 is: {num1}, and num2 is: {num2}')
temp = num1
num1 = num2
num2 = temp
print('After swappinng:')
print(f'Value for num1 is: {num1}, and num2 is: {num2}')
print('--'*50)

'''
Q7 Ask the user for a temperature in Celsius (string input). Convert it to float,
then calculate and print temperature in Fahrenheit.

Conversion formula: FahrenheitTemp = (CelsiusT emp ∗ (9/5)) + 32
'''
CelsiusTemp = float(input('Enter the temperature in Celsius: '))
FahrenheitTemp = float(CelsiusTemp * (9/5)) + 32
print(f'The equivalent Fahrenheit Temperature of the {CelsiusTemp} Celsius temperature is {FahrenheitTemp:.2f}.')
print('--'*50)


'''
Q8. Take the radius (r) as user input and print the area.
Use the formula: π * r2 (value of π = 3.14)
'''

print('Print the area of the circle')
PI = 3.14
radius = float(input('Enter the radius of the circle: '))
area = PI * radius**2
print(f'The area of the circle of radius {radius} is: {area:.2f}')
print('--'*50)

'''
Q9. Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and
compute simple interest:
SI = (P ∗ R ∗ T )/100
'''
print('Calculate the simpe interest')
P = float(input('Enter the principle amount: '))
T = float(input('Enter the time interval: '))
R = float(input('Enter the rate of interest: '))
SI = float((P*T*R)/100)

print(f'The simple interest is: {SI:.2f}')
print('--'*50)

'''
Q.10 Take a decimal number as input (like 45.78) and output its:
'''
user_input = float(input("Enter a decimal number like 45.78: "))
num_str = str(user_input)
decimal_index = num_str.find('.')

integer_part = num_str[:decimal_index]
fractional_part = num_str[decimal_index:]

print(f'The integer part of the input({user_input}) is: {integer_part}')
print(f'The fractional part of the input({user_input}) is: {fractional_part}')
