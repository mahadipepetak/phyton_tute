# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 23:22:16 2021

@author: mahad
"""

class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    def call(self, phone_num):
        print(f"{self.brand} phone is calling {phone_num}")
    
    def __str__(self) -> str:
        return f"Brand {self.brand}, price {self.price}"
    
  
    
iPhone = Phone("IPhone 7+", 500)
iPhone.call("012-25252523")
print(iPhone)