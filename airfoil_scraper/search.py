import pandas as pd
import numpy as np

def FileSearch(N_value, Re_desired, max_thickness, max_camber, CLCD_tolerance, desired_CLCD, **kwargs):
    
    filename = 'airfoils.csv'
    df = pd.read_csv(filename)
    
    column_name= 'Cl/Cd_Re'+str(Re_desired)+'_N'+str(N_value)
    print('Column name: ', column_name)
    print('Max thickness percentage: ', str(max_thickness), '%')
    print('Max camber percentage: ', str(max_camber), '%')
    print('CL/CD: ', str(desired_CLCD))
    print('Tolerance' , str(CLCD_tolerance), '%')

    ## Filter for max camber percentage
    if max_camber:
        max_camber=float(max_camber)
        df['max_camber'] = df['max_camber'].str.rstrip('%').astype('float')
        camber_filter = df['max_camber']<=max_camber
    else:  #don't filter
        camber_filter = True 
        
    ## Filter for max thickness percentage
    if max_thickness:
        max_thickness=float(max_thickness)
        df['max_thickness'] = df['max_thickness'].str.rstrip('%').astype('float')
        thickness_filter = df['max_thickness']<=max_thickness
    else:   #don't filter
        thickness_filter=True
        
    ## Filter for the CL/CD ratio being between the upper and lower bounds. 
    if not CLCD_tolerance:#If tolerance was not specified it sets a default tolerance of 5%
        CLCD_tolerance = 5 #% 
       
    CLCD_tolerance=float(CLCD_tolerance)
     
    upperbound_clcd = (1+CLCD_tolerance/100)*desired_CLCD
    lowerbound_clcd = (1-CLCD_tolerance/100)*desired_CLCD
    
    

    clcd_lower_filter = df[column_name]>=lowerbound_clcd
    clcd_upper_filter = df[column_name] <= upperbound_clcd
    
    ## Combining all the filter for a final filter
    clcd_filters = clcd_lower_filter & clcd_upper_filter & camber_filter & thickness_filter
    
    ## Filtering list 
    filtered_lst = df[clcd_filters]
    
    print(filtered_lst.loc[:,['title', column_name]], end='\n')
    
    ## Changing format of the filtered csv to a list
    filtered_lst_lstformat = filtered_lst.values.tolist()
    lst_column_names = list(filtered_lst.columns)
    
    return lst_column_names, filtered_lst_lstformat
