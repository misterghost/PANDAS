#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 12:58:11 2016

@author: ArqSantos
"""
#Begin by importing pandas:
from pandas import Series, DataFrame
import pandas as pd


#Starting with an array:
data = ['ohio', 'nevada', 'oklahoma', 'texas', 'louisiana']
        
#Convert array called data to a Series.
#Series is a fixed length, ordered dictionary.
object = Series(data)
print(object)  
#Specify index.
object_with_index = Series(data, index=['first state', 'second state', 
                                        'third state', 'fourth state', 
                                        'fifth state'])
print(object_with_index)       

#Index OBJECTS
#Holds labels or metadata like axis name.
#Any array or sequence can be converted to an Index.

#Starting with an array:
data2 = ['ohio', 'nevada', 'oklahoma', 'texas', 'louisiana']

#Convert to series and add indexes.
object_with_index2 = Series(data2, index = ['1st State', '2nd state',
                                            '3rd State', '4th State',
                                            '5th State'])
print(object_with_index2)

#Make those indexes, indexes objects:
index = object_with_index2.index

#Get one of those indexes:
print('Index number one is: ', index[:1])

#Index Objects are inmutable:
print('Inmutable Index Objects:')
print(index[:1])
#Change it (uncomment next line):
#index[1] = '2rd State'
#Error.


#Indexes are being array-like. You can search among them.
print("Let's search for an index in all the indexes:")
if '1st State' in object_with_index2:
    print('List of indexes contains "1st State". ')
else:
    print("No it doesn't.")






























