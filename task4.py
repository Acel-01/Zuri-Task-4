# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:52:10 2021

@author: Emeka Aladimma
"""

class Budget:
    def __init__(self,noun):
        self.database = {}
        self.noun = noun
        self.balance = 0
        self.database[self.noun] = self.balance
        symbol_processed = lambda value: chr(int(value, 16))
        self.naira_symbol = symbol_processed("20A6")
    
    def deposit(self,depositAmount):
        self.balance += depositAmount
        self.database[self.noun] = self.balance
        print(f"Your deposit of {self.naira_symbol}{depositAmount} is successful")
    
    def withdraw(self,withdrawAmount):
        if withdrawAmount > self.balance:
            print("You don't have up to the amount you wish to withdraw")
        else:
            self.balance -= withdrawAmount
            self.database[self.noun] = self.balance
            print(f"Your withdrawal of {self.naira_symbol}{withdrawAmount} is successful")
     
    def balanceFunc(self):
        print(f"{self.naira_symbol}{self.balance}")
    
    def transfer(self,transferAmount,moveTo):
        if self.balance > transferAmount:
            self.balance -= transferAmount
            moveTo.balance += transferAmount
            print(f"Your transfer of {self.naira_symbol}{transferAmount} to {moveTo.noun} is successful") 
        else:
            print("You don't have up to the amount you wish to transfer")
