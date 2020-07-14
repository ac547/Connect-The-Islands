# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 01:59:13 2020

@author: Castellano
"""

def Coordinates(file):
    
    
    ''' This function will return a list,
    where each element of the list is a list itself of coordinates for each test case in the file.
    In the case where the input file only contains 1 test case, the function will return a list of length 1.'''
    
    import re
    file.seek(0)
    coor = []
    
    num_cases = int(file.readlines(1)[0][0])
    print("Number of test cases is: {} \n".format(num_cases))
    
    
    for case in range(num_cases):
        print('For test case {} ... '.format(case+1))
        
        dims = re.findall('\d+', file.readlines(1)[0])
        i = int(dims[0])
        j = int(dims[1])
        case_coor = []
        
        print('Dimensions are {0} by {1} \n'.format(i,j))
        
        for ith in range(i):
            line = file.readlines(1)[0]
            for jth in range(j):
                if line[jth] == "x":
                    #print(ith+1,jth+1)
                    case_coor.append((ith+1,jth+1))
        #print(case_coor)
        coor.append(case_coor)
        
    return coor
                    