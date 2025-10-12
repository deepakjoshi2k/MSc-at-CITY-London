# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 08:12:30 2025

@author: deepak.joshi@city.ac.uk
"""
import numpy as np
import sys
import matplotlib.pyplot as plt

# Q1:
print("Range printing")
print(np.arange(5,16))

# Q2
print("\nLinear spacing printing")
print(np.linspace(0, 23))
# print(np.linspace(0, 23)[1]-np.linspace(0, 23)[0])

# Q3
print("\nPrinting Uniform distribution arry")
arr=[]
for i in range(50):
    arr.append(np.random.uniform(-1,1))
arr=np.array(arr)
print(arr)

# Q4: Histogram for Uniform distribution
plt.hist(arr,bins=12)
plt.xlim(-1.5,1.5)
plt.show()

# Q5
arr_x1= np.random.randint(1,10,size=10)
arr_x2= np.random.randint(15,20,size=10)
print(arr_x1)
print(arr_x2)

diff=(arr_x2**2 - arr_x1**2)
print(diff)

e_dist=np.sqrt(diff)
print(e_dist)