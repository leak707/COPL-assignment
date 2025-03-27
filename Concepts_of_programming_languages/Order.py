#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 22:12:02 2025

@author: dorinavagenhoffer
"""
# from Customer import Customer
from Cart import Cart 

class Order:
    num_orders = 1 #Class attribute to help to generate order IDs
    
    def __init__(self, cart:Cart):
        self.order_id = Order.num_orders
        self.cart= cart
        self.status = "Pending"
        self.applied_discount = None
        self.shipping_info = {}
        Order.num_orders +=1
        
    @staticmethod
    def cancel_order(order):
        order.status = "Cancelled"
        print(f"Order {order.order_id} has been cancelled")
        
    def __str__(self):
        return f"Order ID: {self.order_id}, status: {self.status}"