# -*- coding: utf-8 -*-
"""
Created on Mon May  8 12:59:17 2023

@author: toksy
"""

import pandas as pd
#file_name = pd.read_csv('file.csv')-----> format of read_csv
data= pd.read_csv('transaction.csv')
data= pd.read_csv('transaction.csv', sep=';')

#summary of the data
data.info()
#working with Calculations
#defining variables
CostPerItem= 11.73
SellingPricePerItem= 21.11
NumberofItemsPurchased=6
#Mathemathecal operations on Tableau
ProfitPerItem= 21.11 -11.73
ProfitPerItem= SellingPricePerItem- CostPerItem
ProfitPerTransaction= NumberofItemsPurchased * ProfitPerItem
SellingPricePerTransaction= SellingPricePerItem* NumberofItemsPurchased
CostPerTransaction= CostPerItem* NumberofItemsPurchased

#CostPerTransaction column calculation
#CostPerTransaction= CostPerItemPurchased* NumberOfItemPurchased
#variable= dataframe['columnn_name']

CostPerItem= data['CostPerItem']

NumberofItemsPurchased= data['NumberOfItemsPurchased']

data['CostPerTransaction']= data['CostPerItem'] * data['NumberOfItemsPurchased']

#salesPerTransaction
data['SalesPerTransaction'] = data['SellingPricePerItem']* data['NumberOfItemsPurchased']

#Profit = Sales- Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction']- data['CostPerTransaction']

#Markup= (sales-cost)/sales

data['Markup'] = (data['SalesPerTransaction']- data['CostPerTransaction'])/  data['CostPerTransaction']
#or
data['Markup']= data['ProfitPerTransaction']/ data['CostPerTransaction']

#rounding up markup
data['Markup']= round(data['Markup'],2)


# Combining data fields. always make sure the datatypes are the same'
#if not you can change the datatype ef from integer to string/object data type
#use day= data['Day'].astype(str)
# to change day and year from float to integer
data['Day'] = data['Day'].fillna(0).astype(int)

data['Year'] = data['Year'].fillna(0).astype(int)
#to change integer to string/object
day= data['Day'].astype(str)
Year= data['Year'].astype(str)
my_date= day+ '-' + data['Month'] + '-' + Year

data['Date']= my_date

#Using iloc to view specific rows and data
# first row with corresponding columns
data.iloc[0]

#1st 3 rows
data.iloc[0:3,2]

#1st 3 rows of the 2nd column
data.iloc[0:3,2]

#lsat 5 rows
data.iloc[-5:]

#first 5 rows
data.head()
#or
data.iloc[0:5]
# or
data.head(5)

#all rows on the 2nd column
data.iloc[:,2]

#4th row , 2nd column
data.iloc[4,2]

# Using Split to split client keywordsfield
#new_var= column.str.split('seperator', expand=True)

split_col= data['ClientKeywords,,'].str.split(',' , expand= True)

#Creating new columns for the new split_column

data['ClientAge']= split_col[0]
data['ClientType']= split_col[1]
data['LenghtofContract']= split_col[2]

# to get rid of square bracket and ' using the replace function
data['ClientAge']= data['ClientAge'].str.replace ('[','')

data['ClientAge']= data['ClientAge'].str.replace ("'", "")

data['ClientType']= data['ClientType'].str.replace ("'", "")

data['LenghtofContract']= data['LenghtofContract'].str.replace ("'", "")

data['LenghtofContract']= data['LenghtofContract'].str.replace ("]", "")

data['ItemDescription']= data['ItemDescription'].str.lower()

#bringing in a new dataset by merging
#same as the first time we brought in the dataset just make sure to name the
#file differntly
seasons= pd.read_csv('value_inc_seasons.csv', sep=';')

#to merge the two datafeame into 1 file we use the syntax
#merge_df= pd.merge(df_old,df_new, on='key')

data=pd.merge(data,seasons,on='Month')

#Dropping columns not needed month,day, year and clientkeyWord
#syntax is 
#df=df.drop(column_name, axis=1) axis =1 is to drop a column if =0 is to drop a row

data= data.drop('ClientKeywords,,' , axis=1)
#To drop multiple columns use a list (0ie using a {}and , to seperate them)

data= data.drop(['Year', 'Day', 'Month'] , axis=1)

#Exporting to csv
#The export will go into the working directory

data.to_csv('ValueInc_Cleaned.csv', index= False)


















