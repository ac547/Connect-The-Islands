# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 06:59:39 2020

@author: Castellano
"""

def NumberToCoordinate(L=list,m=int,n=int):
    
    
    '''Returns a list size n of tuples for a list of inputs of size n.
    T is a Global dictionary'''
    coordinate_list = []
    for key in L:
        coordinate_list.append(T.get(key))
    return coordinate_list