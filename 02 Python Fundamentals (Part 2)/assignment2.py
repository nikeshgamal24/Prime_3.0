'''
Q1. Write a program that takes as input 'Salary'. Using conditional statements,
calculate the final tax rate based on these rules:
• If salary < 30,000  -> 5%
• If salary is 30,000- 70,000 -> 15%
• If salary > 70,000 ->25%
'''
print("-----Calculate the final tax rate based on the salary-----")
salary = int(input("Enter your salary: "))
if(salary < 30000):
    print(f'The final tax rate based on your salary ({salary}) is 5%')
elif (salary >= 30000 and salary < 70000):
    print(f'The final tax rate based on youru salary ({salary}) is 15%')
else:
    print(f'The final tax rate based on youru salary ({salary}) is 25%')
print('----'*50)

'''
Q2. Write a function that takes two integers and and prints all even
numbers between them (inclusive).
'''
print('----------Print all the even numbers between two integers-------')
print('Make sure your 2nd integer is greater than the first integer')
num1 = int(input('Enter your first integer: '))
num2 = int(input('Enter your second integer: '))
if(num1 > num2):
    print("Your 2nd integer is smaller than the 1st one.")
else:
    for i in range(num1,num2+1):
        if(i%2 ==0):
            print(i)
print('----'*50)


'''
Q3. Write a function that prints the digits of a number, n
For eg:  n=312, there are 3 digits in it 3, 1 and 2 & we need to print them
'''
print('----Print the digits of a number-----------')
def integerPrint(num):
    while num != 0:
        remainder = num % 10
        num = num // 10
        print(remainder)

num = int(input('Enter an integer number: '))
integerPrint(num)
print('-'*50)


'''
Q4. Write a function to return the count, the number of digits in a number n.
'''
print('----Print the count: the number of a digits-----------')
def countDigits(num):
    count = 0;
    while num != 0:
        remainder = num % 10
        num = num // 10
        count += 1
    return count

num = int(input('Enter an integer number: '))
count = countDigits(num)
print(f'The count of the digist is: {count}')
print('-'*50)


'''
Q5. Write a function to return the sum of digits of a number, n.
'''
print('WAF that returs the sum of the digits of a number.')
def sumOfDigits(num):
    sum = 0
    while num != 0:
        remainder  = num % 10
        sum += remainder
        num = num // 10
    return sum

num = int(input('Enter an integer digit: '))
sum = sumOfDigits(num)
print(f'The sum of the digits of the digit ({num}) is: {sum}')
print('-'*50)

'''
Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3
and 5.
'''
print('Print all nubers from 1 to 100 that are divisible by both 3 and 5')
for i in range(1,101):
    if( i % 3 ==0 and i % 5 ==0 ):
        print(i)
print('-'*50)

'''
Q7. Design a program to continuously input a number,n from user & print if it is
positive or negative until the user enters “Quit”.
'''
print("Continuously input a number,n from user & print if it is positive or negative until the user enters 'Quit'")
while True:
    user_input = input("Enter a integer number: ")

    if(user_input.lower() == 'quit'):
        break
    elif(int(user_input) >  0):
        print('The user input is a positive number')
    elif(int(user_input) < 0):
        print('The user input is a negative number')
    else:
        print('You entered either 0 or invald string')
print('-'*50)

'''
Q8. Letʼs create a Simple Calculator that performs arithmetic operations. Create
a function calculator(a,b,operation) that that performs addition, subtraction,
multiplication, or division based on the operation parameter.

[operation parameter can have values +, -, *& / ]
'''

print('Calculator that performs arithmetic operations')
def calculator(a,b,operation):
    match operation:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            return a/b
        case default:
            return "Invalid operation"


num1 = int(input("Enter an integer number: "))
num2 = int(input("Enter an integer number: "))
operation = input("Enter mode of operation(+,-,*,/): ")

result = calculator(num1,num2,operation)
print(f"The result of the operation {operation} between {num1} and {num2} is: {result}")
print('-'*50)

'''
Q9. Write a function is_print(n) that returns True if n is a prime number and
False otherwise, using a loop.
'''
def is_prime(num):
    count = 0;
    for i in range(2,num):
        print(i)
        if(num % i == 0):
            count += 1
            print(f'count: {count}')

    if(count == 0):
        return True
    else:
        return False

num = int(input('Enter an integer to check the prime: '))
result = is_prime(num)

print(f'Is {num} a prime? Ans: {result}')
print('-'*50)


'''
Q.10 Letʼs create a “ Number Guessing Game”. Given a secret number (already
decided by you), write a program that asks the user to guess it and prints:
i. "Too High", if the guess is above the number
ii. "Too low" , if the guess is below the number
iii. "Correct", if the guess matches
'''
print('--------Welcome to Number Guessing Game-------')

number_to_be_guessed = int(input('Enter a number that another player has to guess: '))

while True:
    your_guess = int(input("Enter your guess: "))
    if(number_to_be_guessed < your_guess):
          print("Too High")
    elif (number_to_be_guessed > your_guess):
          print("Too Low")
    elif(number_to_be_guessed == your_guess):
          print("Correct guess!!!")
          print(f"Number to be guessed: {number_to_be_guessed}, Your guess: {your_guess}")
          break
print('-'*50)
