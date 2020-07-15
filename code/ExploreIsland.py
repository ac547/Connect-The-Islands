# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:35:30 2020

@author: Castellano
"""

def ExploreIsland(t1=int,m=int,n=int, neighbors=[]):
    
    coordinates = T[t1]
    candidates = []
    if neighbors == []:
        neighbors.append(t1)
    
    row_candidates = [(coordinates[0],coordinates[1]-1),(coordinates[0],coordinates[1]+1)]
    [candidates.append(x) for x in row_candidates]
    
    
    col_candidates = [(coordinates[0]-1,coordinates[1]),(coordinates[0]+1,coordinates[1])]
    [candidates.append(x) for x in col_candidates]
    
    print("\nFor Land {0} with coordinates {1}, Candidates are {2} ".format(t1, coordinates, candidates))

    for x in candidates:
        print("  ...Checking coordinates {} for land {}".format(x,t1))
        if x in T.values():
            for key, value in T.items():
                if value == x and key in neighbors:
                    print("            Land {} already on Island with land {}!            ".format(key,t1))
                if value == x and key not in neighbors:
                    print("      ...Adding land {} with coordinates {} to land {} ".format(key,x,t1))
                    neighbors.append(key)
                    print("\nExploring land {}____________\n".format(key))
                    ExploreIsland(key,m,n,neighbors)
    
    #print("Island consists of Lands {}".format(neighbors))                
    return neighbors 
    #neighbors.append()