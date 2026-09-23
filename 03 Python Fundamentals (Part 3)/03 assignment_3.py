'''
Q1. Ask the user for a string and check whether it is a palindrome or not.
A palindrome is a string which is same when we read it forward & backward. Eg - "madam", "racecar" etc.
[Hint - A palindrome string is equal to the reversed version of the string. We can use a loop to reverse the string manually. ]
'''
# print('-----TO CHECK THE GIVEN STRING IS A PALINDROME OR NOT------')
# user_input = input('Enter a string to check for the palindrome: ')
# reversed_string = user_input[::-1]

# if(user_input == reversed_string):
#     print(f'{user_input} string is a palindrome.')
# else:
#     print(f'{user_input} string is not a palindrome.')
# print('-')*50



'''
Q2. Given a list of integers compute the average of all numbers in the list.
'''
# print("-----Calculate the average of all numbers in the list-----")
# list1 = [1, 2, 7, 4, 5]
# sum = 0
# for val in list1:
#     sum += val

# avg = (float)(sum/len(list1))
# print(f"The average value of the list is: {avg:.2f}")
# print('-'*50)


'''
Q3. Input two lists of integers from the user. Merge them into one list and sort the result.
Eg - list1 = [1, 2, 7] , list2 = [2, 4, 5]
result = [1, 2, 3, 4, 5, 7]
'''
# print("-----MERGE TWO LISTS OF INTEGERS INTO ONE LIST AND SORT THE RESULT-----")
# print("Enter the number of list in list1")
# n1 = int(input("Enter your desire number elements for list 1: "))
# list1 = []

# for i in range(n1):
#     num = int(input("Enter the elements for the list 1: "))
#     list1.append(num)

# n2 = int(input("Enter your desire number for the list 2: "))
# list2 = []

# for i in range(n2):
#     num = int(input("Enter the elements for the list 2: "))
#     list2.append(num)

# list3 = list(set(list1).union(set(list2)))
# print("The merged list with sorted elements is:")
# for val in list3:
#     print(val, end=" ")
# print()
# print('-'*50)


'''
Q4. Given a tuple of integers, create:
A tuple of all even numbers
A tuple of all odd numbers
'''
# print('-----EVEN NUMBERS TUPLE AND ODD NUMBERS TUPLE-----')
# tuples = (1,2,3,4,5,6,7,8,9,10)
# even_tuple = ()
# odd_tuple = ()

# for ele in tuples:
#     if (ele % 2 ==0):
#         even_tuple = even_tuple + (ele,)
#     else:
#         odd_tuple = odd_tuple + (ele,)
# print("Even Tuple:")
# for val in even_tuple:
#     print(val, end=" ")
# print()
# print(type(even_tuple))
# print("Odd Tuple:")
# for val in odd_tuple:
#     print(val, end=" ")
# print()
# print(type(odd_tuple))
# print('-'*50)


'''
Q5. Create a dictionary where:
Keys = student names
Values = marks (integer)
Write a menu-based program where user presses a key ('A', 'B', 'C', 'D') depending on the operation they want to perform on the dictionary:

A - Add a student
B - Update marks
C - Search for a student
D - Display all students and marks
'''
print("----------")



'''
Q6. Given a list of words:
words = ["apple", "banana", "kiwi", "cherry", "mango"]
Create a dictionary that maps each word to its length.

Example:
{"apple": 5, "banana": 6, "kiwi": 4, ...}
'''

'''
Q7. Write a program that takes a string from the user and prints the number of spaces in the string.
'''

'''
Q8. Write a program to check whether two lists share no common elements.
# share no common elements list1 = [1, 2, 3, 4]  list2 = [5, 6, 7, 8]
# share common elements    list1 = [1, 2, 3]     list2 = [3, 4]
[Hint - use sets]
'''

'''
Q9. Given a list, print all elements that appear more than once in the list.
[Hint - use sets]
'''


'''
Q10. Ask the user for a string and print:
All unique characters
The count of unique characters
'''