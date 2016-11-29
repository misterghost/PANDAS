#merging data sets examples
#Begin by importing pandas:
from pandas import Series, DataFrame
import pandas as pd

df1 = DataFrame({'key':['vicky', 
                        'javier', 
                        'miguel', 
                        'vero', 
                        'daniela', 
                        'lupe'], 
                'data1': [1,2,3,4,5,6]})


df2 = DataFrame({'key':['javier', 
                        'vicky', 
                        'daniela', 
                        'lupe', 
                        'vero', 
                        'miguel'], 
                'data2': [2,5,1,6,8,2]})

#pd.merge(df1, df2, on='key')

df3 = DataFrame({'lkey':['lupe',
                         'vicky',
                         'vero',
                         'daniela',
                         'miguel'
                         ],
                'data3': [1,2,3,4,5]})

df4 = DataFrame({'rkey':['javier',
                         'vicky',
                         'vero',
                         'daniela',
                         'lupe',
                         'miguel'],
                'data4':[2,5,1,6,8,2]})
