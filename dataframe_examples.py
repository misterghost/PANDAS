#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:50:10 2016

@author: ArqSantos
"""
#Begin by importing pandas:
from pandas import Series, DataFrame
import pandas as pd


#Starting with a dict of equal length lists:
data = {
        'State':['ohio', 'nevada', 'oklahoma', 'texas', 'louisiana'], 
        'Year':[2000, 2001, 1999, 2003, 2005],
        'Population': [1.5, 1.3, 1.6, 1.2, 2.0]
        }
        
#Convert to dataframe, without specifying order of columns:      
a = dataframe_example = DataFrame(data)
print('First dataframe from the dictionary of equal-length lists.')
print(a)

#Convert to dataframe, stating the order of the columns:
b = dataframe_example2 = DataFrame(data, columns = ['Year', 'State', 'Population'])
print('Rearranged the order of the columns.')
print(b)

#Convert to dataframe, stating the order of the columns but adding an inexistent column,
#which adds NotaNumber (empty.)
c = dataframe_example3 = DataFrame(data, columns = ['Year', 'State', 'Population', 'Debt' ])
print('Added a column with no values; it added NaN')
print(c)

#Retrieve a column from a dataframe by dict-like notation:
x = dataframe_example3['State']
print("By Dict-Like Notation:(ie. dataframe_name['name_of_column']") 
print(x)

#Retrieve a column from a dataframe by attribute:
y = dataframe_example3.State
print('By Attribute: (ie: dataframe_name.name_of_column)') 
print(y)

#Add a new column with a value to an existing dataframe:
#using dict notation, we add a new column, and assign its values
#according to a design condition, in this case, if population > 1.4 : state is big. (true)
dataframe_example3['Big State?'] = dataframe_example3.Population > 1.4
print('Added a new column filled with values if condition met')
print(dataframe_example3)

#NESTES DICTIONARIES:
#If passed to a dataframe, OUTER dict keys will be COLUMNS, inner will be row indices:
#Notice that values missing are autofilled with NaN
#Try using "DF_From_Nested_Dict.T" to TRANSPOSE the result, swapping columns for rows.


population = {'Tijuana' : {2000:1.5, 2001:1.6, 2003:1.9},
              'Nuevo Leon': {2000: 2.5, 2001:2.9, 2002:3.1, 2004:3.8}
              }
DF_From_Nested_Dict = DataFrame(population)
print(DF_From_Nested_Dict)
#print(DF_From_Nested_Dict.T)

























