# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:16:38 2021

@author: frank
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:16:38 2021

@author: frank
"""

import pandas as pd
import numpy as np

def FileSearch(N_value, Re_desired, max_thickness, max_camber, CLCD_tolerance, desired_CLCD, **kwargs):
    filename = 'airfoils.csv'#'airfoils.csv'

    if not CLCD_tolerance:#If tolerance was not specified it sets a default tolerance of 5%
        CLCD_tolerance = 5 #%
    # camber_filter_bool = bool(max_camber)
    # thicness_filter_bool = bool(max_thickness)
    
    
        
    CLCD_tolerance=float(CLCD_tolerance)/100
     
    upperbound_clcd = (1+CLCD_tolerance)*desired_CLCD
    lowerbound_clcd = (1-CLCD_tolerance)*desired_CLCD
    
    column_name= 'Cl/Cd_Re'+str(Re_desired)+'_'+str(N_value)
    print('Column name: ', column_name)
    print('Thick: ', str(max_thickness))
    print('Camber: ', str(max_camber))
    print('CL/CD: ', str(desired_CLCD))
    print('Tolerance' , str(CLCD_tolerance))
    
    df = pd.read_csv(filename)
    
    if max_camber:
        max_camber=float(max_camber)
        camber_filter = df['max_camber']<=max_camber
    else:
        #don't filter
        camber_filter = True #Need to add and verify this filter works
        #if setting to True doesn't work, then create a list of the same size, where all the values are True
    if max_thickness:
        max_thickness=float(max_thickness)
        thickness_filter = df['max_thickness']<=max_thickness
    else:
        #don't filter
        thickness_filter=True#Need to add and verify this filter works
    
    clcd_lower_filter = df[column_name]>=lowerbound_clcd
    clcd_upper_filter = df[column_name] <= upperbound_clcd
    
    clcd_filters = clcd_lower_filter & clcd_upper_filter & camber_filter & thickness_filter
    
    filtered_lst = df[clcd_filters]
    print(filtered_lst.loc[:,['title', column_name]])#, 'max_thickness', 'max_camber']])
    #print(type(filtered_lst.loc[:,['title', column_name]]))
    filtered_lst_lstformat = filtered_lst.values.tolist()
    lst_column_names = list(filtered_lst.columns)
    return lst_column_names, filtered_lst_lstformat#.loc[:,['title', column_name, 'max_thickness', 'max_camber']]

def InputFunction ():
    Re = input('Choose Reynolds Number [50K, 100K, 200K, 500K, 1000K]: ')
   
    Re_list = ['50K', '100K', '200K', '500K','1000K']
    Re_list_nums = ['50000', '100000', '500000', '1000000']
    N_list = ['N9', 'N5', '9', '5']#Should they input N9 or just 9??
    
    while True: #checks for valid input of Reynolds Number
        if (Re.upper() in Re_list )or (Re.upper() in Re_list_nums):
            if Re in Re_list_nums:
                Re=int(int(Re)/1000)
                Re=str(Re)+'K'
            break
        else:
            Re = input('Oops! Enter a valid Reynolds Number from [50k, 100k, 200k, 500k, 1000k]: ')
    
    N_val = input('Choose an N critical value [N5 or N9]: ')
    while True:#checks for valid input of N
        if N_val.upper() in N_list:
            if N_val in ['5', '9']:
                N_val = 'N'+ N_val
            break
        else:
            N_val = input('Oops! Enter a valid N value from [N5 or N9]: ')
            
    CLCD = float(input('Enter the desired CL/CD ratio: '))
    CLCD_tolerance = input('Enter the desired tolerance for the CL/CD ratio: [click Enter for default tolerance]: ') 
    ## will use an if statement so if they leave it empty it'll be false. if they enter something it'll be true
    max_camber = input('Enter the max camber percentage [click Enter to not filter]: ') #Restrict to verify only numbers are entered
    max_thickness = input('Enter the max thickness percentage [click Enter to not filter]: ')
     
    
    return N_val, Re, max_thickness, max_camber, CLCD_tolerance, CLCD

###Uncomment these to use the InputFunction instead of the GUI
# N_val, Re, max_thickness, max_camber, CLCD_tolerance, CLCD= InputFunction()    
# FileSearch(N_val, Re, max_thickness, max_camber, CLCD_tolerance, CLCD)
