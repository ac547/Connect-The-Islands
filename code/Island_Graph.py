# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:16:39 2020

@author: Castellano
"""

def Island_Graph(Island_List=list):
    
    import sys, os
    
    # For n islands in Island list, enumerate island on [0,3)
    
    output = []
    skip = []
    
    dums = dict(val for val in enumerate(Island_List))
    
    for i in dums.keys():
        #print(i)
        skip.append(i)
        
        for j in dums.keys():
            
                if i == j or j in skip:
                    next
                    #print("skipped")
                
                else:
                    
                    #sys.stdout = open(os.devnull, 'w')
                    
                    y0 = [i,j,Island_Distance(dums[i],dums[j])]
                
                    output.append(y0)
                
                    #sys.stdout = sys.__stdout__
                
                    #print(y0)
                
        
    #print(output)
    print("\nLenght of output list is {}, ".format(len(output)),
          "which makes sense for a list of size {}, ".format(len(Island_List)),
          "Since {} times {} divided by 2 is {}.".format(len(Island_List),
                                                         len(Island_List)-1,
                                                         int(len(Island_List)*(len(Island_List)-1))/2))
    
                                                                                                                    
    return output
    
    