# -*- coding: utf-8 -*-
"""task4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q9GMNhfWK3tI5oh8nKJkVaQCmjRZ6AIh
"""

#Asks the user to store an integer in a variable
integer = int(input("Enter an integer:"))

#using conditional sttements, the algorithm determines wether or not the integer
#is divisible or not by 2 and/or 5
if (integer %2) == 0 and (integer %5) == 0:
    print("The integer is divisible by 2 and 5.")
if (integer %2) == 0 or (integer %5) == 0:
    print("The integer is divisible by 2 or 5.")
else:
    print("The integer is not divisible by 2 or 5.")