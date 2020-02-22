#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Calculator:
    
    def __init__(self):
        self.a = self.b = 0
    def get_a_b(self): 
        return self.a , self.b
    
    def set_a (self, a):
        self.a = a
    
    def set_b (self, b):
        self.b = b
        
    def Addition(self, tup):
        self.a = tup[0]
        self.b = tup[1]
        return self.a + self.b
    
    def Subtraction(self, tup):
        self.a = tup[0]
        self.b = tup[1]
        return self.a-self.b
    
    def Multiplication(self, tup):
        self.a = tup[0]
        self.b = tup[1]
        return self.a * self.b
    
    def Division(self, tup):
        self.a = tup[0]
        self.b = tup[1]
        return self.a / self.b
    
    def Power(self, tup):
        self.a = tup[0]
        self.b = tup[1]
        return self.a**self.b

