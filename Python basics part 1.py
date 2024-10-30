# Lesson 1: variables
# no special charactors when starting ex: !@#$%^&*() | only _ is allow as the first char
# the next char can be anything: lower and upper case letters, numbers, and char

#
# a = 100
# b = 12
# c = a*b
#
# print(c)
# print('hello world!')
#
# if a < 12:
#     c= b+a
#     print(c)
#
# else:
#     print('a is not less 12')
#
#
# #10/24/2024
# #keywords: are variables which are reserved by the programing language
# # ex: elif, else, for, if and so on there are 35 in total
#
# #finding type
# a = 100
# b = 12.0
# c = 'welcome'
#
# print(type(a))
# print(type(b))
# print(type(c))
#

"""
# Data types:
numeric: int, float, and complex
text - string ex "test"
boolean - true and false
map - dictionary
set - set and frozenset
binary - bytes, bytearray, memoryview
"""
from tkinter.font import names

#10/25/2024

#what is your age? using formating:

# Age = 24
# Name = 'Franc'
# Location = 'PA'
#
# print(f'Hello, my name is {Name}, I am {Age}, and I am located in {Location}')
#
# print(Name.upper())
# print(Name.lower())
# print(len(Location))

#10/26/24
# Arithmetic and relational

# a = 2
# b = 5
#
# print(a+b) #addition
# print(a-b)  #subtraction
# print(a/b) #divition
# print(a*b) #multiplication
# print(a%b) #modulus
# print(a//b) #floor division
# print(a**b) #exponential

#comparison values
# a = 2
# b = 5
#
# print(a>b)
# print(a>=b)
# print(a<b)
# print(a<=b)

#equal to operator
# a = 2
# b = 5
#
# print(a==b)
# print(a!=b)

#Logical statement
# a = 2
# b = 9
#
# if a == b and b==a:
#     print('hello')
# elif a>b or b>a:
#     print('hi')
# else:
#     print('try again')
#
# name = input("enter your first name: ")
# last_name = input("enter your last name: ")
# age = int(input('how old are you: '))
# print(f'your first name is {name}, and your last name is {last_name}')
#
# if age <9:
#     print('you are a baby')
# elif age >=10 and age <=19:
#     print('you are in your teens')
# elif age >=20 and age <=49:
#     print('you are an adult and ready for the world')
# elif age >= 50 and age <=70:
#     print('you are an adult with a family, and making big impact to the youth')
# else:
#     print("you're old!")

#10/28/24
#flow control
#
# for loop

# sequence = "Test"
# r = 0
# for a in sequence:
#     print(a, r)
#     r=r+1

# for x in range(1,10,2):
#     print(x)

# x=0
# test=5
# for i in range (test):
#     print(test,x)
#     x=x+1

#input example

# n= int(input('enter a number: '))
# x = 0
# for i in range(1,n):
#     x = x + 1
#     print(f'you entered {n} and {n} * {x} =', i*n)

#printing even number

for i in range(10):
    if i%2 != 0:
        print('these are odd numbers: ',i)
        if i == 5:
            break

