#!/usr/bin/env python


while True :
    print("input a number")
    number = input()
    if type(number) == int:
        break
    print("error!input an integer!!") 
    
number_int = number
sum_number = 0
while number_int > 0 :
    sum_number += number_int%10
    number_int /= 10 
print(sum_number)
