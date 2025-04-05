# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 08:26:01 2025

@author: sakuc
"""
#find the given no is a prime no or not
a=int(input("Enter the No: "))
def prime_number(a):
    for i in range(2,a):
        if a%i==0:
            print("Given no is not a Prime Number")
            break;
        else:
            print("given no is a Prime Number")
            break;
    


#find the no of vowels in a sentence
a=input("Enter the sentence: ")


def no_of_vowels(a):
    count=0
    for i in a:
        if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U':
            count+=1
        else: 
            continue
    print(f"There are {count} Number of Vowels In The given Sentence ")
no_of_vowels(a)

#Find the GCD of the nos
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

a,b=map(int,input("Enter the numbers: ").split())
p=gcd(a,b)
print(f"Gcd of {a,b} is {p}")

#program to print numbers from 1 to 10 with single row with one tab space
for i in range(0,10):
    print(i+1,end=" ")
    
#program to create dictionary where the keys arefrom 1 to 15 and values are from square of the numbers
dict1={}
for i in range(1,16):
    dict1[i]=i**2
print(dict1)























