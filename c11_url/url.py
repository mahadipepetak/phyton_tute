# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 22:34:05 2021

@author: mahad
"""

from urllib import request
import json

url_json = "https://official-joke-api.appspot.com/random_joke"
r = request.urlopen(url_json)
#print(r.getcode())

joke = r.read()
json_data = json.loads(joke)
#print(json_data)
for key in json_data:
    print(f"{key} - {json_data[key]}")