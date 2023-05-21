# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:55:27 2023

@author: toksy
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel/ xlxs files
data= pd.read_excel('articles.xlsx') 

# getting the summary of the data
data.describe()

#Summary of the columns
data.info()

# Counting the number of aricles per source
#formart df.groupby(['column_to_group'])['column_to_count'].count()

data.groupby(['source_id'])['article_id'].count()

#Total number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#Dropping a column
data= data.drop('engagement_comment_plugin_count' , axis = 1)
data.info()

#functions inphyton
#This is a function
def thisfunction():
    print('This is my first function') #does not do anthing because we did not call it
#now call it using the return function

def thisfunction():
    print('This is my first function')
    return()

#Functions can be used to create variables
#This is a function with Variables

def aboutMe(name):
    print('This is ' +name)
    return(name)
a = aboutMe('Fatima')  
    
def aboutMe(name, surname, location):
    print('This is ' +name, 'My surname is '+surname, 'I am from '+location)
    return(name, surname, location)
a = aboutMe('Fatima','Louis','Ikeja') 

#Using for loops in functions
def favFood(food):
    for x in food:
        print('Top food is '+ x)
fastfood= ('burger','pizza ','pie')
favFood(fastfood)
    

#Creating a function with for loop
def keywordflag(keyword):
    length= len(data)
    keyword_flag =[]
    for x in range(0,length):
        heading= data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
keywordflag= keywordflag('murder')
    
# Creating a new column in dataframe
data['keyword_flag'] = pd.Series(keywordflag)


# SentimentIntensityAnalyzer
sent_int = SentimentIntensityAnalyzer()
text = data['title'][15]
sent= sent_int.polarity_scores(text)

text = data['title'][16]
sent= sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

# Adding a for loop to extract a sentiment per title
title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
length= len(data)
for x in range (0,length):
    try:
        text= data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent= sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0      
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)  
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

#writing/ saving cleaned data to excel
data.to_excel('blogme_clean.xlsx', sheet_name = 'blogmedata', index= False)



























    