# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:55:39 2021

@author: mahad
"""

"""
Create a function that accepts 3 parameters and checks for equality between any two of them.

Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.
"""
def checkConvStrInt(num):
    if isinstance(num, str):
        return int(num)
    else:
        return num


def checkEqual(num1, num2, num3):
    
    #check & convert str -> int if necessary
    num1 = checkConvStrInt(num1)        
    num2 = checkConvStrInt(num2)        
    num3 = checkConvStrInt(num3)
        
    #compare each possiblity
    num12 = (num1 == num2)
    num23 = (num2 == num3)
    num13 = (num1 == num3)
    
    #return compared result
    print("has equal") if num12 or num23 or num13 else print("has no equal") 
    return True if num12 or num23 or num13 else False
        
print(checkEqual("1", 2, 3))