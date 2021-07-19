# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 16:26:28 2021

@author: mahad
"""
# note:
#myList = [1, 2, 3, 4]
#myList[1:2] = []
#print(myList)
#print(myList[0])

# var list 
myUniqueList = []
myLeftovers = []

# def a function
def addValToList(val):
    if val not in myUniqueList:
        myUniqueList.append(val)
        return True 
    
    myLeftovers.append(val)
    return False

# test
addValToList(1)
addValToList(2)
addValToList(1)
addValToList(3)
addValToList("hello")
addValToList("hello")

print(myUniqueList)
print(myLeftovers)