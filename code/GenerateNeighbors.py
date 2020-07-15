# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:32:10 2020

@author: Castellano
"""

def GenerateNeighbors(t1=int,m=int,n=int):
    
    coordinates = T[t1]
    row_neighboors = []
    candidates = []
    
    row_candidates = [(coordinates[0],coordinates[1]-1),(coordinates[0],coordinates[1]+1)]
    [candidates.append(x) for x in row_candidates]
    
    
    col_candidates = [(coordinates[0]-1,coordinates[1]),(coordinates[0]+1,coordinates[1])]
    [candidates.append(x) for x in col_candidates]
    
    #return [x in T.values() for x in candidates]
    return sum([x in T.values() for x in candidates])
    