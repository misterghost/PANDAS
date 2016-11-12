#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:48:04 2016

@author: ArqSantos
"""
#Begin by importing pandas:
from pandas import Series, DataFrame
import pandas as pd
#reading a regular csv:
df = pd.read_csv('forCSV.csv')
print(df)

print('#######################################')
print('#######################################')

#reading a regular csv with missing fields:
dfm = pd.read_csv('forCSV_missing.csv')
print(dfm)
#in console:     pd.isnull(dfm)

print('#######################################')
print('#######################################')

#replace selected fields with a default value:
#2 options:
#1st option: specify a sentinel word list:
sentinels = {'nombre':['pedro', 'polo']}
dfm2 = pd.read_csv('forCSV_missing.csv', na_values=sentinels)
print('Deleted pedro and polo via a blacklist.')
print(dfm2)
#2nd option: pass the value directly:
dfm3 = pd.read_csv('forCSV_missing.csv', na_values=['silvia'])
print('Deleted silvia directly.')
print(dfm3)



    
    

