# -*- coding: utf-8 -*-
"""logic

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OwTx2IzF9EVXaZzo-_wsk_6sx-Wyd-vo
"""

#Asks user for their details
name = input("Enter your full name: ")
age = int(input("Enter your age: "))

if age == 21: #Wrong boolean expression. The program asks if user is aged exactly 21, not 21 and over. 
#If older than 21, no message will be displayed.
	print("You're {age} years old. You're old enough to buy tickets for this event!") 
 #It prints the word age in brackets instead displaying the input number for age
 
else age >= 21: #Wrong boolean expression. The program asks if user is aged 21 or over. Not under.

	print("You're {age} years old. You're not old enough to buy tickets for this event.")
  #It prints the word age in brackets instead displaying the input number for age
  #The printed message doesn't match the else condition