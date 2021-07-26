# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 08:51:16 2021

@author: mahad

NOTE: - ABANDON
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
          
def getNewCoordinate(MATRIC, colChoose):
    
    rowReg = None 
    global player           
    #print("GET COOR", MATRIC, colChoose, player)       
    
    for col in range(len(MATRIC[colChoose])-1, -1, -1):
        #print(MATRIC[colChoose][col])
        if(not MATRIC[colChoose][col]): #if none
            rowReg = "player" + str(player)            
            break
                
    if rowReg:
        MATRIC[colChoose][col] = rowReg
        #print("\nRETURN GET COOR", MATRIC, colChoose, col)
        return [colChoose, col] # if has changes
    
    return None #if no changes to MATRIC
    

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
            
            '''
            rowReg = None            
           
            for col in range(len(MATRIC[colChoose])-1, -1, -1):
                #print(MATRIC[colChoose][col])
                if(not MATRIC[colChoose][col]): #if none
                    rowReg = "player" + str(player)
                    player = int(not player)
                    break
                
            if rowReg:
                MATRIC[colChoose][col] = rowReg
            '''  
            newCoordinate = getNewCoordinate(MATRIC, colChoose)
            print("GET COOR", newCoordinate)
            if newCoordinate: 
                #check winner
                getWinner(newCoordinate)
                
                player = int(not player) # if has new coor -> change player
                
                
def getBgStCol(colChoose):
    diff = (COL_ROW_NUM-1)-(colChoose+3)
    pt = 0
    if(diff>)
    
    return pt
            
            
def getWinner(coordinate):
    global MATRIC
    global player
    # 0row = coor[n,0] 
    # 0col = coor[0,n]
    col = coordinate[0]
    row = coordinate[1]
    smCol = (coordinate[0]-3) if ((coordinate[0]-3) >= 0) else 0 #if >0, sm = val, else = 0
    smRow = (coordinate[1]-3) if ((coordinate[1]-3) >= 0) else 0 #if >0, sm = val, else = 0
    bgStCol = (coordinate[0]+3) if ((coordinate[0]+3) >= 0) else 0 #if >0, sm = val, else = 0
    
    print(col, smCol, row, smRow)
    
    textWin = None
    
    #check horizontal
    hor1= (MATRIC[col][smRow] == MATRIC[col][smRow+1] and MATRIC[col][smRow+1] == MATRIC[col][smRow+2] and MATRIC[col][smRow+2] == MATRIC[col][smRow+3])
    hor2= (MATRIC[col][smRow+1] == MATRIC[col][smRow+2] and MATRIC[col][smRow+2] == MATRIC[col][smRow+3] and MATRIC[col][smRow+3] == MATRIC[col][smRow+4])
    hor3= (MATRIC[col][smRow+2] == MATRIC[col][smRow+3] and MATRIC[col][smRow+3] == MATRIC[col][smRow+4] and MATRIC[col][smRow+4] == MATRIC[col][smRow+5])
    hor4= (MATRIC[col][smRow+3] == MATRIC[col][smRow+4] and MATRIC[col][smRow+4] == MATRIC[col][smRow+5] and MATRIC[col][smRow+5] == MATRIC[col][smRow+6])
    
    if hor1 or hor2 or hor3 or hor4:
        textWin = "player: ", player, "win"
    #check vertical
    #check decline
    #check incline
    
    if(not textWin):
        textWin = "continue... "
    
    print(textWin)
    
    

# TEST/SYSTEM
board(COL_ROW_NUM)
fillMatric(COL_ROW_NUM)
inGame()

#testMat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(testMat[0][1])

