# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 23:51:26 2021

@author: mahad
"""

# import library
import datetime

"""
# PREVIOUS INFO
songName = "Ragaman"
singer = "Faizal Tahir"
dateReleased = datetime.datetime(2018, 8, 24)
genre = ["reggae", "funk-pop"]
genreStr = ','.join([str(item) for item in genre])

company = ["Faithful Music", "Warner Music Malaysia"]
companyStr = ','.join([str(item) for item in genre])
                      
writer = ["Faizal Tahir", "Mike Chan", "Romeo", "Karim Karam", "Jaare"]
writerStr = ','.join([str(item) for item in writer])

duration = "00:04:10" 

"""

# def dectionary
favSong = {
    "Name" :"Ragaman",
    "Singer" : "Faizal Tahir",
    "Date Released" : datetime.datetime(2018, 8, 24),
    "Genre" : ["reggae", "funk-pop"],
    "Company" : ["Faithful Music", "Warner Music Malaysia"],
    "Writer" : ["Faizal Tahir", "Mike Chan", "Romeo", "Karim Karam", "Jaare"],
    "Duration" : "00:04:10"
    }

# define functions
def printSongMeta(songDict):
    for key in songDict:
        text = key + " - " + str(songDict[key])
        print(text)

def guessKeyVal(key, val):
    if(key in favSong and favSong[key]==val):
        print("YESS")
    else:
        print("NOO")
        

# Output info
# print(favSong)
printSongMeta(favSong)
                
guessKeyVal("Name", "Ragaman") 
guessKeyVal("Name", "Igaman")   
guessKeyVal("Hello", "Igaman")   
        
        