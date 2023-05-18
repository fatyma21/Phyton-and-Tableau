# -*- coding: utf-8 -*-
"""
Created on Thu May 11 08:56:04 2023

@author: toksy
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#read json file
#method 1 
json_file= open('loan_data_json.json')
data= json.load(json_file)

#run all scripts

#method 2
with open('loan_data_json.json') as json_file:
    data= json.load(json_file)
    #print(data)

# transform to dataframe
loandata= pd.DataFrame(data)

# finding unique values for the purpose column
loandata['purpose'].unique()

# describing the data
loandata.describe()

# describe the data for a specific column
loandata['int.rate'].describe()

loandata['fico'].describe()

loandata['dti'].describe()

# Usinf Exp to get real annual income
income= np.exp(loandata['log.annual.inc'])

#creating an annual income column in the loandata using the income created above
loandata['Annual Income']= income


#Working with If Startements
a= 14
b= 500
if b>a:
    print('b is greater than a')
    
#adding more conditions

a= 14
b= 500
c= 1000
if b>a and b<c:
    print('b is greater than a but less than c')  
    
# What if a condition is not met ie there is no else
a= 14
b= 500
c= 20
if b> a and b <c :
    print('b is greater than a but less than c')   #add and else for print out
else:
    print('No conditions met')
    
#Adding an elseif statement to add a 2nd or more contdition

a= 40
b= 500
c= 30
if b> a and b <c :
    print('b is greater than a but less than c')   #add and else for print out
elif b>a and b>c:
    print('b is greater than a and c')
else:
    print('No conditions met')    


#Using Or
a= 40
b= 500
c= 1000
if b> a or b <c :
    print('b is greater than a or less than c')   
else:
    print('No conditions met')            
    
a= 40
b= 0
c= 1000
if b> a and b <c :
    print('b is greater than a or less than c')   
else:
    print('No conditions met')    



#FICO SCORE
# fico >= 300 and < 400:
# 'Very Poor'
# fico >= 400 and ficoscore < 600:
# 'Poor'
# fico >= 601 and ficoscore < 660:
# 'Fair'
# fico >= 660 and ficoscore < 780:
# 'Good'
# fico >=780:
# 'Excellent'

fico = 700 # we used 250 and 350 as well to print differnt ficocat
if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 600 and fico < 660:
    ficocat ='Fair'
elif fico >= 660 and fico < 700:
    ficocat ='Good'
elif fico >=700:
    ficocat ='Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)
    
#Applying the above to the whole column
#Using for loops
fruits= ['apple','pear','banana','cherry']
for x in fruits:
    print(x)
    y = x +' fruit'
    print(y)

#loops based on position
for x in range(0,3):
    y= fruits[x] + ' for sale'
    print(y)
    
#applying Fpor Loops to Loan Data
#using 1st 10 ficocat data
ficocat = []
for x in range(0,10):
    category= loandata['fico'] [x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category < 600:
        cat = 'Poor'
    elif category >= 600 and category < 660:
        cat ='Fair'
    elif category >= 660 and category < 700:
        cat ='Good'
    elif category >=700:
        cat ='Excellent'
    else:
        cat = 'Unknown' 
    ficocat.append(cat)
        
        
# applying to loandata all rows
length= len(loandata)        
ficocat = []
for x in range(0,length):
    category= loandata['fico'] [x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category < 600:
        cat = 'Poor'
    elif category >= 600 and category < 660:
        cat ='Fair'
    elif category >= 660 and category < 700:
        cat ='Good'
    elif category >=700:
        cat ='Excellent'
    else:
        cat = 'Unknown' 
    ficocat.append(cat)
ficocat= pd.Series(ficocat)  
loandata['fico.category']= ficocat     

#WHILE LOOP
i=1
while i< 10:
    print(i)
    i= i+1


#try and accept
length= len(loandata)        
ficocat = []
for x in range(0,length):
    category= loandata['fico'] [x]
    
    try:
        
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 600 and category < 660:
            cat ='Fair'
        elif category >= 660 and category < 700:
            cat ='Good'
        elif category >=700:
            cat ='Excellent'
        else:
            cat = 'Unknown' 
    except:  
        cat = 'Unknown'
    ficocat.append(cat)


# #Testing Erro
# length= len(loandata)        
# ficocat = []
# for x in range(0,length):
#     category= 'red'
#     try:
        
#         if category >= 300 and category < 400:
#             cat = 'Very Poor'
#         elif category >= 400 and category < 600:
#             cat = 'Poor'
#         elif category >= 600 and category < 660:
#             cat ='Fair'
#         elif category >= 660 and category < 700:
#             cat ='Good'
#         elif category >=700:
#             cat ='Excellent'
#         else:
#             cat = 'Unknown' 
#     except:
#         cat = 'Error- Unknown' 
   
#     ficocat.append(cat)


#df.loc as conditional statement
# for of df.loc
#df.loc[df[columnName]condition, newColumnName] = 'valueif condition is met'

loandata.loc[loandata['int.rate'] >0.12, 'int.rateType'] = 'High'
loandata.loc[loandata['int.rate'] <=0.12, 'int.rateType'] = 'Low'

#Plots
#install and import matplotlib.pyplot as plt
#number of rows or loans by fico.category

catplot= loandata.groupby(['fico.category']).size()
catplot.plot.bar()
plt.show()

#Adding color and widthsize

catplot= loandata.groupby(['fico.category']).size()
catplot.plot.bar(color= 'green', width= 0.1)
plt.show()

purposecount= loandata.groupby(['purpose']).size()
purposecount.plot.bar(color= 'red', width= 0.2)
plt.show()

#Scatterplots Define your y and x points
ypoint = loandata['Annual Income']
xpoint = loandata['dti']
plt.scatter(xpoint,ypoint)
plt.show()

#changing color to red
ypoint = loandata['Annual Income']
xpoint = loandata['dti']
plt.scatter(xpoint,ypoint, color='red')
plt.show()

#changing color to a specific green

ypoint = loandata['Annual Income']
xpoint = loandata['dti']
plt.scatter(xpoint,ypoint, color='#4caf50')
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)













































































