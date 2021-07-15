# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 21:32:48 2021

@author: mahad
"""

"""
song name: Ragaman
singer: faizal tahir
 
writer: Faizal Tahir, Mike Chan, Romeo, Karim Karam, Jaare
company: Faithful Music, Warner Music Malaysia
date: 24/08/2018
year of released: 2018
genre: reggae
duration: 4min 10sec
"""

# import library
import datetime

# def variables
favSong = "Ragaman"
singer = "Faizal Tahir"
dateReleased = datetime.datetime(2018, 8, 24)

genre = ["reggae", "funk-pop"]
genreStr = ','.join([str(item) for item in genre])

company = ["Faithful Music", "Warner Music Malaysia"]
companyStr = ','.join([str(item) for item in genre])
                      
writer = ["Faizal Tahir", "Mike Chan", "Romeo", "Karim Karam", "Jaare"]
writerStr = ','.join([str(item) for item in writer])

duration = "00:04:10" 

# def function
def singer(song = None):    
    return "Faizal Tahir" if song == favSong or not song else "unknown"

def dateReleased(song = None):
    return datetime.datetime(2018, 8, 24) if song == favSong or not song else "unknown"

def genreStr(song = None):
    genre = ["reggae", "funk-pop"] if song == favSong or not song else "unknown"
    return ','.join([str(item) for item in genre])

"""
def company(song = None):
    company = ["Faithful Music", "Warner Music Malaysia"] if song == favSong or not song else "unknown"
    return ','.join([str(item) for item in company])

def writer(song = None):
    writer = ["Faizal Tahir", "Mike Chan", "Romeo", "Karim Karam", "Jaare"] if song == favSong or not song else "unknown"
    return ','.join([str(item) for item in writer])

def duration(song = None):
    return "00:04:10" if song==favSong or not song else "unknown"
"""

# print output
print("Favorite Song: " + favSong)
print("Singer: " + singer())
print("Date of released: " + dateReleased().strftime("%x"))
print("Type of genre(s): " + genreStr())
# print("Company(ies): " + company())
# print("Writer(s): " + writer())
# print("Song duration: " + duration())

print("Company(ies): " + companyStr)
print("Writer(s): " + writerStr)
print("Song duration: " + duration)








