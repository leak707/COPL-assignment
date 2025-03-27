#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 22:30:17 2025

@author: dorinavagenhoffer
"""
from Customer import Customer
from Discount import Discount
from Cart import Cart

#Derived class from Customer
class LoyalCustomer(Customer):
    def __init__(self, customer_id, surname, lastname, email, address, loyalty_points=0):
        super().__init__(customer_id, surname, lastname, email, address)
        self.loyalty_points = loyalty_points #Additional attribute     
    
    #Overridden method      
    def welcome_coupon(self):
        welcome = Discount("LOYAL20", 20)  #Loyal customers get a 20% discount
        self.discounts.append(welcome)
        print(f'Welcome, {self.surname}! As a loyal customer, you get a 20% welcome coupon: {welcome.discount_code}')

    #Overridden method
    def apply_discount(self, total_price:Cart):
          new_price = total_price * 0.95  #5% base discount for loyal customers
          print("Loyal customer discount applied")
          return super().apply_discount(new_price)
        
    def __str__(self):
        return f"LoyalCustomer: {self.surname} {self.lastname}, email: {self._email}, orders: {len(self.orders)}, loyalty points: {self.loyalty_points}"
      