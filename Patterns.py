# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 13:40:05 2025

@author: sakuc
"""
'''pattern printing
1
1 2
1 2 3 
1 2 3 4 
1 2 3 4 5 '''

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")
    
'''
A
B B
C C C
D D D D
'''
for i in range(0,5):
    print((chr(64+i)+' ')*i)
 #Mario pyramids
''' * * * * 
    * * *
    * *
    *'''
for i in range(6):
    for i in range(6-i):
        print("*",end=" ")
    print()

''' #
    # #
    # # # 
    # # # #'''
   
for i in range(4):
    for i in range(i+1):
        print("#",end=" ")
    print()
    
'''# # # #
   # # #
   # #
   #'''
   
for i in range(4):
    for j in range(4-i):
        print("#",end=" ")
    print()
 
    
 
