#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 18:02:23 2017

@author: dragon
"""

import pandas as pd

dataframe = pd.read_csv('Deduplication Problem - Sample Dataset.csv')
def deduplication_records(df1):
    
    list1 = []
    list2 = []
    for i in range(df1.shape[0]):
        list1.append(df1.iloc[i,0].split())
    for j in range(df1.shape[0]):
        list2.append(df1.iloc[j,3].split())
    
    df2 = pd.DataFrame(list1, columns = ['ln1','ln2'])
    df3 = pd.DataFrame(list2, columns = ['fn1', 'fn2'])
    
    df1 = pd.concat([df1, df2, df3], axis = 1)
    
    df1['full_name_new'] = df1['fn1'] + ' ' + df1['ln1'] + ' ' + df1['dob']
    df4 = df1.copy()
    
    df4 = df4.drop_duplicates('full_name_new')
    
    df4.drop(['ln1', 'ln2', 'fn1', 'fn2', 
              'full_name_new',], axis = 1, inplace = True)
    
    a = df4.shape[0]
    deduplicated_records = df4.to_csv(path_or_buf= '/home/dragon/Downloads/deduplicated_records.csv', index = False)
    return(df4, a)
    
deduplication_records(dataframe)
        

