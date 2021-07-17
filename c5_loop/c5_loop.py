# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 20:39:11 2021

@author: mahad
"""

# define function
def isPrime(num):
    if (num == 2): # 2 is prime number
        return True    
    elif (num%2 == 0): # check for even number
        return False
    else: # check odd number until the val
        ptr = 3
        while(ptr<num):
            if ((num/ptr).is_integer()):
                return False                
            ptr += 2
        return True

  
# test/operations
limit = 100
for ptr in range(limit):
    ptr += 1
    text = ""
        
    if(isPrime(ptr)): # if prime
        text += "prime"
    else: 
        if(ptr%3 == 0): # dev by 3
            text += "fizz"
            
        if(ptr%5 == 0): # dev by 5
            text += "buzz"
    
    # if not prime/dev by 3/ dev by 5, print the number
    if(len(text) == 0):
        text = str(ptr)
    
    print(text)
