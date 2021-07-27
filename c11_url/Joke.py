# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 23:19:53 2021

@author: mahad
"""

class Joke:
    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline
    
    def __str__(self):
        return f"Setup: {self.setup}, \nPunchline: {self.punchline}"