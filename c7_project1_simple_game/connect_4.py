# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 08:51:16 2021

@author: mahad
"""
# VARIABLES/CONSTANT
COL_ROW_NUM = 4  
MATRIC=[]
INSTRUCTION_PER_TURN = "Instruction?"
INSTRUCTION_PER_TURN += "\nChooce column number:(between 4 and 10)."
INSTRUCTION_PER_TURN += "\nor 'q' to exit."
INSTRUCTION_PER_TURN += "\nYour move? ... "

player = 1
isDone = 0

# the board is symmetrical n*n size
def board(colRow):
    for r in range(colRow):
        activeRw = ""
        dividerRw = ""
        
        #draw active values
        for c in range(colRow+1):  
            activeRw+=" "             
            if (c<colRow-1):
                activeRw+="|"
        
        #draw row divider
        for c in range(colRow+1):    
            #stop draw for the last row
            if r<colRow-1:  
                if c<colRow-2:
                    dividerRw+="--"
                else:
                    dividerRw+="-" 
        
        print(activeRw)
        print(dividerRw)
        
def fillMatric(colRow):
    MATRIC_Col = [None]*colRow
    for r in range(colRow):
        MATRIC.append(list(MATRIC_Col))
    print(MATRIC)
          

"""
[ r1     r2     r3
 [None, None, None], col 1
 [None, None, None], col 2
 [None, None, None]  col 3
]
"""
def inGame():
    global MATRIC
    #testMat = [[None, None, 3], [None, None, None], [None, 8, 9]]
    
    
    while(True):        
        global player
        
        print(MATRIC)
        #print(MATRIC)
        print("\nTURN: PLAYER", player)
        
        userInput = input(INSTRUCTION_PER_TURN)   
        if((userInput).upper() == "Q"):
            print("exit:", userInput)
            break
        elif(int(userInput)):            
            print(player, "userInput:", userInput)
            colChoose = int(userInput)-1
            print(colChoose)
            #check for the last row of that column
            # if has no val -> assign
            # if has -> repeat player
            
            rowReg = None            
           
            for col in range(len(MATRIC[colChoose])-1, -1, -1):
                #print(MATRIC[colChoose][col])
                if(not MATRIC[colChoose][col]): #if none
                    rowReg = "player" + str(player)
                    player = int(not player)
                    break
                
            if rowReg:
                MATRIC[colChoose][col] = rowReg
            
            #check winner
            

# TEST/SYSTEM
board(COL_ROW_NUM)
fillMatric(COL_ROW_NUM)
inGame()

#testMat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(testMat[0][1])

