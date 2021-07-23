# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 16:00:36 2021

@author: mahad
"""
#import modules
from os import path

#define functions
def optA(filePath):
    noteFile = open(filePath, "r")
    print(noteFile.read())
    noteFile.close()
    
def optB(filePath):
    noteFile = open(filePath, "w")
    noteText = input("Note text:... ")
    noteFile.write(noteText)
    noteFile.close()

def optC(filePath):
    noteFile = open(filePath, "a")
    noteText = input("Note text:... ")
    noteFile.write(noteText)
    noteFile.close()
    
def optD(filePath):
    # display all lines
    noteFile1 = open(filePath, "r")
    data = noteFile1.readlines()
    
    # print(data)
    count = 1
    for line in data:
        print(count, ")", line)
        count += 1
    
    # prompt user input
    lineNum = int(input("Line to be replaced:..."))
    lineText = input("Note text:...")
    data[lineNum-1] = lineText + "\n"
    
    # overwrite text
    noteFile1 = open(filePath, "w")
    noteFile1.writelines(data)
    
    noteFile1.close()
    
def createNote():
    noteFile = open(filePath, "w")
    print("Created a new note...")
    myNote = input("Write your note:")
    noteFile.write(myNote)
    noteFile.close()
    print("The note was saved.")


# variables/const
INSTRUCTION = "Please choose an option. "
INSTRUCTION += "\nA) Read the file"
INSTRUCTION += "\nB) Delete the file and start over"
INSTRUCTION += "\nC) Append the file"
INSTRUCTION += "\nD) Replace a single line"
INSTRUCTION += "\nYour choice:... "


#test/flow
print("****System start****")
filePath = input("File Name (eg: myNote.text): ")
print(filePath, "- EXIST:", path.exists(filePath))

if(not path.exists(filePath)): # file found
    createNote()
else: #file not found
            
    userOption = (input(INSTRUCTION)).upper()
    print("\nFILENAME:", filePath)
    
    if(userOption == "A"): 
        print("ACTION: A) Read the file")
        optA(filePath)
    elif(userOption == "B"):
        print("ACTION: B) Delete the file and start over")
        optB(filePath)
    elif(userOption == "C"):
        print("ACTION: C) Append the file")
        optC(filePath)
    elif(userOption == "D"):
        print("ACTION: D) Replace a single line")
        optD(filePath)
    else:
        print("choose:", userOption, "Action not recognized.")
    
print("\n****System end****")
  
    
    
    
    
    
    