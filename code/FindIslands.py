# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:35:53 2020

@author: Castellano
"""

def FindIslands(LandCell_List=list):
    
    Island_List = []
    island = []
    checked = []
    
    for i in LandCell_List.keys():
        
        if i not in checked:
            
            print("Finding Islands Connected to Land {}".format(i))
        
            island = ExploreIsland(i,20,20,neighbors=[])
            [checked.append(x) for x in island]
            print("Explored island {}, consists of {}:".format(i, island))
        
            if len(island) < 1:
                Island_List.append([i])
        
            if island is not None:
                Island_List.append(island)
        else:
            next
                    
    return Island_List