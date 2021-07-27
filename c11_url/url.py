# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 22:34:05 2021

@author: mahad
"""

from urllib import request
import json
from Joke import Joke

url_json = "https://official-joke-api.appspot.com/random_joke"
r = request.urlopen(url_json)
#print(r.getcode())

joke_data = r.read()
json_data = json.loads(joke_data)
#print(json_data)
'''
for key in json_data:
    print(f"{key} - {json_data[key]}")
'''
jokeObj = Joke(json_data["setup"], json_data["punchline"])
print(jokeObj)

#print(json_data["setup"])