# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 23:03:35 2020

@author: Debarghya Mondal
"""
'''
Houseflies have an approximate life of four weeks. Given the number of days a housefly lived, design an algorithm and write the Python code to determine its approximate age in seconds. Check for boundary conditions and print ‘Invalid input’ if condition is not satisfied. For example, if a housefly lived for 21 days then its approximate age in seconds is 21*24*60*60 is 1814400.

Input Format

Number of days, n

Output Format

Number of seconds

Boundary Conditions

n>0 and n <28
'''

n= int(input()) #input no of days lived

if n<0 and n>28:
    print("Invalid")
else:
    m=n*24*60*60
    print(m)
    
    