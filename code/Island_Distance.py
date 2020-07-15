# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:14:43 2020

@author: Castellano
"""

def Island_Distance(isl1=list,isl2=list):
    
    x0 = 'nothing'
    
    for i in isl1:
        
        if GenerateNeighbors(i,m=int,n=int) > 3: #Landlocked Land
            next
        else:
            
            print("    Checking land {}".format(i))
            for j in isl2:
                
                if GenerateNeighbors(j,m=int,n=int) >3: 
                    next
                else:
                    
                    #print("Measuring land {} to land {}".format(i,j))
                    
                    x1 = Distance(i,j)
                    
                    if x0 == 'nothing':
                        x0 = x1
                        
                    if x1 < x0:
                        x0 = x1
                        print("\nNew Shortest Lenght is {}".format(x0))
    print("\nShortest lenght is {}\n".format(x0))
    return x0
                      