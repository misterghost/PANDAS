#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 12:58:11 2016

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
        
obj = Series(range(3), index=['a', 'b', 'c'])
        
index = obj.index
