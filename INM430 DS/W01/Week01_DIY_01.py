# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 13:44:51 2025

@author: deepak.joshi@city.ac.uk
"""

import csv
import sys

f=open(r"D:\City Lectures\INM430 DS\W01\TB_burden_countries_2014-09-29.csv")


#Part1: Q1
c=0
for k in csv.reader(f):
    if bool(k)==True:
        c=c+1
print(f"Number of rows in this dataset is {c-1}.")
f.close()


#Part1: Q2

with open(r"D:\City Lectures\INM430 DS\W01\TB_burden_countries_2014-09-29.csv") as f:


    idx=next(csv.reader(f)).index("e_prev_num_lo") 
        
    sum_0=0
    count=0
    for i in csv.reader(f):
        
        if i[idx] !="":
            sum_0=sum_0+float(i[idx])
        
        count=count+1

    print("Sum is ",sum_0)
    print("Row count is ",count)
    print("Avg is ",sum_0/count)
    
#Part1: Q3 e_prev_nu,_lo & year 1990 & 2011

with open(r"D:\City Lectures\INM430 DS\W01\TB_burden_countries_2014-09-29.csv") as f:
    
    head = next(csv.reader(f))
    idx_e=head.index("e_prev_num_lo")
    idx_yr=head.index("year")
    count_1990=0
    count_2011=0
    sum_1990= 0
    sum_2011=0
    
    for i in csv.reader(f):
        if i[idx_e] !="":
            if i[idx_yr]=="1990":
                sum_1990=sum_1990+ float(i[idx_e])
                count_1990=count_1990+1
                
                
            elif i[idx_yr]=="2011":
                sum_2011=sum_2011+ float(i[idx_e])
                count_2011=count_2011+1
                avg_2011=sum_2011/count_2011
            
        avg_1990=sum_1990/count_1990
        avg_1990=sum_1990/count_1990
    print("Avg of 'e_prev_num_lo' for yr 1990: ",avg_1990)
    print("Avg of 'e_prev_num_lo' for yr 2011: ",avg_2011)