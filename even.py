# -*- coding: utf-8 -*-
"""even

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a483yn69wmU8RnbdP9AlqTEk1G13ixA7
"""

#Asking user to input a number, int() is used to ensure the variable is an integer
number = int(input("Enter a number: "))

#Setting the starting point i as -1 because the task asked to include 1
#In order for the numbers to be even underneath the loop, the code will instruct the
#algorithm to add 2 to each input number in order to be even, since it starts -1
i=-1

#while loop repeats printing even numbers that are smaller or include the input number
#the reason there i isnt == to input number it's because there 
while i < number:
    i+=2
    print(i) #prints all the even numbers from 1 up to the input number