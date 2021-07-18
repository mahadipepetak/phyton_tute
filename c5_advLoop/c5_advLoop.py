# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 18:57:10 2021

@author: mahad

"""
MAX_WIDTH = 10

# _|_|_ (col:3)
def myFunc(rows, cols):
    if(rows > 10): # if exceed comfortable width
        return False
    for r in range(rows): 
        text = ""
        for c in range(cols):
            if(r < rows-1):
                text += "_"
            else:
                text += " " # no "_" for the last row
                
            if (c < cols-1): # no "|" for the last col
                text += "|"
        print(text)
    return True

print(myFunc(10,5))
            