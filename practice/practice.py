#strings
course="English for beginners"
print(course.replace('English','math')) #replaces the work, letter
print(len(course))  #length of a word
print('English' in course) #checks the existance
print(course.upper())
print(course.lower())
print(course.find('o')) #find the index

#arithmetic operations
#'/' return floting pont number
#''//' returns the integer of devision
#'%' returns the remainder
#'**' power

#Math functions
x=2.99
print(round(x)) #rounds the number
print(abs(-2,9)) #absolute value

import math
math.ceil(3.4), math.floar

#If statements
is_hot=True
is_cold=False
if is_hot:
    print("It is a hot day. Drink more water")
elif is_cold:
    print("It is cold outside, wear warm clothes")
else:
    print("It is a lovely day")        

#problem
house=int(input("Enter a price of a house"))
good_credit=True
if good_credit:
    downpayment=house*0.1
else:
    downpayment=house*0.2
print(f"Down payment: $ {downpayment}")    

#logical operators
high_income=True
good_credit=True
if high_income and good_credit: #and both true or one of the is true
    print("Eligible for loan")
else:
    print("Not eligible")

#problem
temperature=int(input("Enter a temperature: "))
if temperature>30:
    print("It is a hot day")
elif temperature==30:
    print("It a good day")
else:
    print("It is a cold day")           

#problem
name=string(input("Type your name"))
if len(name)<3:
    print("The name should be at least 3 characters long")
elif len(name)>50:
    print("Your name is too long, it should be max 50 characters") 
else:
    print("It looks good")  

#weight convert from punds to kg
weight=int(input("Enter yout weight: "))
unit=input("Choose 'L' for pound and 'K' for kilogram")  
if unit.upper=='L':
    mass=weight*0.45   
    
      


