# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 15:30:25 2022

@author: Navya
"""

import pandas as pd
h=['age','workclass','fnlwgt','education','education-num','martial-status','occupation','relationship','race','sex','capgain','caploss','hrsperweek','native-coun','class']
d=pd.read_csv(r'C:\Users\Navya\Downloads\income.csv',names=h)
d.head()
print(d.shape)#--->total rows and col 

d['workclass']=d['workclass'].replace(to_replace=' ?',value='Private')
d['native-coun']=d['native-coun'].replace(to_replace=' ?',value='Private')
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
d['workclass']=le.fit_transform(d['workclass'])
d['education']=le.fit_transform(d['education'])
d['martial-status']=le.fit_transform(d['martial-status'])
d['occupation']=le.fit_transform(d['occupation'])
d['relationship']=le.fit_transform(d['relationship'])
d['race']=le.fit_transform(d['race'])
d['sex']=le.fit_transform(d['sex'])
d['native-coun']=le.fit_transform(d['native-coun'])




d=d.fillna(0)#--->empty spaces filled with 0 with help of pandas
"""
spliting of xtest,ytest,xtrain,ytrain"""
x=d.iloc[:,:14].values
y=d.iloc[:,14].values
print(x.shape)
print(y.shape)
print(type(d))
print(type(x))
print(type(y))


from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=9)
print(xtrain.shape)
print(xtest.shape)
print(ytrain.shape)
print(ytest.shape)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(xtrain,ytrain)



ypred=model.predict(xtest)
print(ypred.shape)
#-->accuracy check ytest with ypred
from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred)*100)