# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:01:01 2020

@author: Castellano
"""

def Distance(t1=int,t2=int):
    '''Returns a scalar representing the manhattan distance between two coordinates representing input identifiers t1 and t2. 
    T is a global dictionary'''
    t1 = T[t1]
    t2 = T[t2]
    
    distance = abs(t2[1]-t1[1]) + abs(t2[0]-t1[0])
    
    return distance