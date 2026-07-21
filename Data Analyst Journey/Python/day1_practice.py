#Problem 1

#Print:

#Hello Vinay

#Solution
print('Hello Vinay')


# Problem 2

# Take name and age from the user.

# Print:

# My name is Vinay and I am 22 years old.

#Solution
# user_name = input("Enter your Name :- ")
# user_age = int(input("Enter your Age :- "))
# print(f'My name is {user_name} and I am {user_age} years old.')



# Problem 3

# Check whether a number is even or odd.

#Solution
# num = 12
# if num%2==0:
#     print('number is even')
# else:
#     print('number is odd')



# Problem 4

# Print numbers from 1 to 100.

#Solution
# for i in range(1,101,1):
#     print(i)




# Problem 5

# Print only even numbers from 1 to 100.

#Solution
# for i in range(2,101,2):
#     print(i)



# Problem 6

# Find the sum of numbers from 1 to 100.

#Solution
# sum = 0
# for i in range(1,101):
#     sum+=i
# print(sum)




# Problem 7

# Create a list of 10 numbers.

# Print:

# Largest
# Smallest
# Sum
# Average

#Solution

# li = [1,2,3,4,5,6,7,8,9,10]
# largest = li[0]
# smallest = li[0]
# sum = 0
# for i in li:
#     if i>largest:
#         largest=i
#     if i<smallest:
#         smallest=i
#     sum+=i
# print(f'Largest value is : {largest}')
# print(f'Smallest value is : {smallest}')
# print(f'Sum of values is : {sum}')
# print(f'Average of values is : {sum / len(li)}')




# Problem 8

# Count vowels in a string.

# Example:

# Python Programming

# Output:

# 4


#Solution
# vowels = 'aeiouAeiou'
# count = 0
# user_string = input("Enter any string to count vowels :- ")
# for i in user_string:
#     if i in vowels:
#         count+=1
# print(count)



# Problem 9

# Reverse a string.

# Input

# Vinay

# Output

# yaniV

#Solution
# user_str = input("Enter any string :- ")
# str = ""
# for i in range(len(user_str)-1,-1,-1):
#     str+=user_str[i]
# print(str)





# Problem 10

# Create a dictionary.

# Store:

# Name
# Age
# College

# Print every key and value.

# di = {
#     'Name' : 'Vinay',
#     'Age' : 21,
#     'College' : 'MITS'
# }
# for i in di:
#     print(f'{i} : {di[i]}')
