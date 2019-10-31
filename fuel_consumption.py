# -*- coding: utf-8 -*-
"""Fuel Consumption.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16G62uPpK6mLb-2Vf18m9oUZQlBFOCM59
"""

import pandas as pd
import numpy as np

cons_data14=pd.read_csv('Original MY2000-2014 Fuel Consumption Ratings (2-cycle).csv',encoding='latin1')
cons_data15=pd.read_csv('MY2015 Fuel Consumption Ratings (5-cycle).csv',encoding='latin1')
cons_data16=pd.read_csv('MY2016 Fuel Consumption Ratings.csv',encoding='latin1')
cons_data17=pd.read_csv('MY2017 Fuel Consumption Ratings.csv',encoding='latin1')
cons_data18=pd.read_csv('MY2018 Fuel Consumption Ratings.csv',encoding='latin1')
cons_data19=pd.read_csv('MY2019 Fuel Consumption Ratings.csv',encoding='latin1')

from IPython.display import display
data=[cons_data14,cons_data15,cons_data16,cons_data17,cons_data18,cons_data19]
cons_data14.head()
for i in data:
    display(i.head())

for i in data:
    display(i.isnull().values.any())

for i in data:
    display(i.shape)

data_c=list()
for i in data:
    for column in i:
        if ((i[column].isna().sum())==i.shape[0]):
            i= i.drop(column, axis=1)
    data_c.append(i)
    display(i.head(5),i.shape)

for x in data_c:
    display(x.shape)

for i in range(2,6):
    display(data_c[i].head(5))

new_data=list()
new_data.append(data_c[0])
new_data.append(data_c[1])
new_data.append(data_c[2].drop('CO2', axis=1))
for i in range(3,6):
    new_data.append(data_c[i].drop('CO2', axis=1).drop('SMOG', axis=1))
for x in new_data:
    display(x.head(5),x.shape)

print(len(np.unique(new_data[0]['MODEL.1'].values.tolist())))
new_data[0] = new_data[0].astype({"MODEL.1": str})
new_data[1]=new_data[1].rename(index=str,columns={"FUEL CONSUMPTION*":"FUEL CONSUMPTION"})
display(new_data[1].head(5))

for x in new_data:
    display(x.head(5))

data_new=list()
for x in new_data:
    data_new.append(x.drop(x.index[0]))
for x in data_new:
    display(x.head(5))

df=pd.DataFrame()
for x in data_new:
    df=df.append(x,ignore_index=True)

display(df.head(5),df.shape)

df.to_csv("Fuel Consumption",index=False)

Fuel=pd.read_csv('Fuel Consumption')

display(Fuel.head(5))

Fuel.describe()

null_columns=Fuel.columns[Fuel.isnull().any()]
Fuel[null_columns].isnull().sum()

for x in range(14343,Fuel.shape[0]):
    display(Fuel.loc[x:,])

p=0
for x in range(14344,Fuel.shape[0]):
    if(Fuel.loc[x].isnull().sum()>=7):
        Fuel=(Fuel.drop(Fuel.index[x]))
Fuel.shape

null_columns=Fuel.columns[Fuel.isnull().any()]
Fuel[null_columns].isnull().sum()

