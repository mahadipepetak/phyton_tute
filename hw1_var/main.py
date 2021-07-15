# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 12:53:13 2021

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

# print output
print("Favorite Song: " + songName)
print("Singer: " + singer)
print("Date of released: " + dateReleased.strftime("%x"))
print("Type of genre(s): " + genreStr)
print("Company(ies): " + companyStr)
print("Writer(s): " + writerStr)
print("Song duration: " + duration)