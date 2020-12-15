# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:07:54 2020

@author: Debarghya Mondal
"""

m=[]
r = int(input())
for i in range(0,r):
	l= list(map(int,input().split(' ')))
	m.append(l)
print(m)
c=len(m[0])


res=[]
for i in range(c):
	l=[]
	for j in range(r):
		l.append(0)
	res.append(l)

for i in range(0,r):
   # iterate through columns
   for j in range(c):
       res[j][i] = m[i][j]

print(res)