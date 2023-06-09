# -*- coding: utf-8 -*-
"""task1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/131tALDJoigYYqDwsr_G-8NhPbj0BjSdn
"""

#Assigning values to the below variables
num1=10
num2=20
num3=30

#Using conditional statements we compare the value stored in the num1 and num2 
#variables, stating which one is the larger
if num1 > num2:
    print("num1 is greater than num2.")
elif num1 < num2:
    print("num2 is greater than num1.")

#Using conditional statements and the modulus operator (%), we determine if num1
#is odd or even. Divides the value on the left of the operator by the value 
#on the right and returns the remainder. That's why the number 2 is used.
if (num1 %2) == 0:
    print("num1 is an even number.")
else:
    print("num1 is an odd number.")

#Using conditional statements we can sort the three integers in ascending order 
#help from: https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap03/sort.html
if num1>num2 and num1>num3:
    if num2>num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
if num2>num1 and num2>num3:
    if num1>num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
if num3>num2 and num3>num1:
    if num2>num1:
        print(num3, num2, num1)
    else:
        print(num3, num1, num2)