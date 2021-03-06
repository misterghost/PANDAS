#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:41:28 2016

@author: ArqSantos
"""
#Begin by importing pandas:
from pandas import Series, DataFrame
import pandas as pd
#SELECTION

#Starting with a dict of equal length lists:
data = {
        'State':['ohio', 'nevada', 'oklahoma', 'texas', 'louisiana'], 
        'Year':[2000, 2001, 1999, 2003, 2005],
        'Population': [1.5, 1.3, 1.6, 1.2, 2.0]
        }
        
#slightly different:
#create an index first:
old_index = ['1st State', '2nd state', '3rd State', '4th State', '5th State']

#Convert to dataframe, without specifying the indexes, those will be autogenerated:      
dataframe_example = DataFrame(data)
print('First dataframe from the dictionary of equal-length lists.')
#Indexes go from 0 to 4
print(dataframe_example)

#Assign specific set of indexes to dataframe:
dataframe_example.index = old_index
print('Changed indexes to a list of indexes.')
print(dataframe_example)

#Getting a slice of the dataframe rows:
x = dataframe_example['1st State':'3rd State']
print('This is a slice of rows.')
print(x)

#Replacing values:
dataframe_example['1st State':'3rd State'] = 'Unknown'
print('This replaced existing values with a specific one.')
print(dataframe_example)


#This is a slice of the dataframe columns:
z = dataframe_example[['Population', 'Year']]
print('this is a slice of columns.')
print(z)






print('###################################################')
#ARITHMETICS ON SERIES AND DATAFRAMES

#Starting with a pair of dicts of equal length lists:
data1 = {
        'State':['ohio', 'nevada', 'oklahoma', 'texas', 'louisiana'], 
        'Year':[2000, 2001, 1999, 2003, 2005],
        'Population': [1.5, 1.3, 1.6, 1.2, 2.0]
        }

data2 = {
        'State':['clemente', 'nevada', 'juana', 'junior', 'louisiana'], 
        'Year':[2000, 2001, 1999, 2003, 2005],
        'Population': [1.8, 1.2, 1.1, 1.9, 2.9]
        }
        
#Create an index first:
index3 = ['1st state', '2nd state', '3rd state', '4th state', '5th state']

#Convert to dataframe, without specifying the indexes, those will be autogenerated:      
adding_dataframe_example1 = DataFrame(data1)
print('First dataframe from the dictionary of equal-length lists.')
#Indexes go from 0 to 4
print(adding_dataframe_example1)

#Assign specific set of indexes to dataframe:
adding_dataframe_example1.index = index3
print('Changed indexes to a list of indexes on the first DF.')
print(adding_dataframe_example1)

#Again for the next DF:
#Convert to dataframe, without specifying the indexes, those will be autogenerated:      
adding_dataframe_example2 = DataFrame(data2)
print('Second dataframe from the dictionary of equal-length lists.')
#Indexes go from 0 to 4
print(adding_dataframe_example2)

#Assign specific set of indexes to dataframe:
adding_dataframe_example2.index = index3
print('Changed indexes to a list of indexes on the second DF.')
print(adding_dataframe_example2)





xs = adding_dataframe_example1 + adding_dataframe_example2
print('This is the sum of both DF:')
print(xs)




































