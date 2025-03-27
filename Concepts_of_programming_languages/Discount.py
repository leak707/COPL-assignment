#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 22:11:17 2025

@author: dorinavagenhoffer
"""
from Cart import Cart


class Discount:
    def __init__(self, discount_code:str, discount_percentage:int):
        self.discount_code=discount_code
        self._discount_percentage = discount_percentage #Protected atttribute
        self.__times_used =0 #Private attribute
        
     #Calculate the discounted price  
    def calculate_discount(self,total_price:Cart):
        after_discount = total_price *(1-self._discount_percentage/100)
        self.__times_used +=1 
        return after_discount
    
    #Getter, how many times the coupon was used
    @property
    def coupon_used(self):
        return self.__times_used
      
    def __str__(self):
        return f"Discount Code: {self.discount_code}, value: {self._discount_percentage}%, used {self.__times_used} times."


 