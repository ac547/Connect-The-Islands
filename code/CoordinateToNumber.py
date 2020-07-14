# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 06:58:57 2020

@author: Castellano
"""

def CoordinateToNumber(coordinate_list=list,m=int,n=int):
    '''Returns a list for a list of coordinates as input,
    returns a tuple for a coordinate as input'''
    global T
    if len(coordinate_list) > m*n:
        raise Exception('Stop, too many coordinates for mXn')
    if type(coordinate_list) is tuple:
        T = {0 : coordinate_list}
    else:
        for value in enumerate(coordinate_list):
            T = dict(val for val in enumerate(coordinate_list))
    return T