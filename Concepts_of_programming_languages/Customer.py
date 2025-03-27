#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 22:12:14 2025

@author: dorinavagenhoffer
"""
from Cart import Cart
from Discount import Discount


class Customer:
    def __init__(self, surname: str, lastname: str, email:str, address:str):
        self.surname = surname
        self.lastname = lastname
        self._email = email # Protected email attribute
        self.address = address
        self.orders =[] #A list, that stores the customer's orders
        self.discounts = [] #A list, that stores the customer's discount codes
        
    registered ={} #Dictionary to store the registered customers(key= customer's email)
    
    #Registering a new user
    @classmethod
    def register(cls):
        surname = input("Surname: ").strip()
        lastname = input("Lastname: ").strip()
        email = input("Email: ").strip()
        address=input("Address: ").strip()
        #Check if the email is already registered
        if email in cls.registered:
            print("This email has already been registered! ")
            return None
        #If new user, create a new customer instance
        new_customer=cls(len(cls.registered)+1, surname,lastname,email,address)
        cls.registered[email]=new_customer
        new_customer.welcome_coupon()
        return new_customer
    
    #Log in based on email 
    @classmethod
    def login(cls, email):
        if email in cls.registered:
            customer = cls.registered[email]
            print(f"Welcome back {customer.surname}!")
            return customer
        else:
            print("No account found with this email")
            return None
    
    #Welcome coupon for new customers(10% discount)
    def welcome_coupon(self):
        welcome = Discount("WELCOME10",10)
        self.discounts.append(welcome)
        print(f'Welcome, {self.surname}! Here is a 10% welcome coupon for you: {welcome.discount_code}')
        
    #Applies the discount code entered by the user
    def apply_discount(self, discount_code):
        for discount in self.discounts:
            if discount.discount_code == discount_code:
                self.applied_discount = discount
                print(f"Discount {discount_code} applied!")
                return
        print("Invalid discount code!")
    
      #Creates new order, appends the customer's order list  
    @classmethod    
    def append_order(cls, customer, cart_items: Cart):
            orders = [cls(customer,cart)for cart in cart_items]
            customer.orders.extend(orders)
            return orders
    
    #Getter for email
    @property
    def email(self):
        return self._email
    
    #Getter for customer ID
    @property
    def customer_id(self):
        return self.__customer_id
        
    def __str__(self):
        return f"Customer: {self.surname} {self.lastname}, email: {self._email}, orders: {len(self.orders)}"

