# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:51:24 2019

@author: Abhiram_CH_V_N_S
"""


import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


countries_df = pd.read_csv('factbook.csv', skipinitialspace=True, delimiter=";")
countries_df = countries_df.drop(0)

hiv_deceased = countries_df[['Country','HIV/AIDS - deaths' ]]

hiv_deceased_non_null = hiv_deceased.loc[~pd.isna(hiv_deceased['HIV/AIDS - deaths'])]


#convert 'HIV/AIDS - deaths' to int32

hiv_deceased_non_null.astype({'HIV/AIDS - deaths':'int32'})

hiv_deceased_20 = hiv_deceased_non_null.sort_values(by='HIV/AIDS - deaths', ascending=False).head(20)

hiv_count = hiv_deceased_20['HIV/AIDS - deaths'].value_counts().head(20)




#plots
x = hiv_deceased_20['Country']
y = hiv_deceased_20['HIV/AIDS - deaths']

hiv_count.plot(kind='bar')

plt.scatter(x,y)
plt.xticks(rotation=90)

#South Africa has the highest mortality rate because of HIV


#Unemployment
countries_df['Unemployment rate(%)']

unemployment_rate = countries_df.loc[~pd.isna(countries_df['Unemployment rate(%)'])]    

unemployment_rate.astype({'Unemployment rate(%)':'float32'})

unemployment_rate_20 = unemployment_rate.sort_values(by='Unemployment rate(%)', ascending=False).head(20)

x = unemployment_rate_20['Country']
y = unemployment_rate_20['Unemployment rate(%)']

plt.scatter(x,y)
plt.xticks(rotation=90)

#Nauru has the highest unemploymnet rate.. It is also the least visited place in the world.

account_balance = countries_df.loc[~pd.isna(countries_df['Current account balance'])]   
account_balance.astype({'Current account balance':'float32'})


account_balance_20 = account_balance.sort_values(by='Current account balance', ascending=True).head(20)
account_balance_20[['Country','Current account balance']]


#account balance of India and USA

account_balance.loc[account_balance['Country'].str.startswith('Unite')]
countries_df.iloc[249]

# Unemployment rate vs Military expenditures - percent of GDP(%)

military_expenditure = countries_df.loc[~pd.isna(countries_df['Military expenditures - percent of GDP(%)'])]
military_expenditure.astype({'Military expenditures - percent of GDP(%)':'float32'})

military_expenditure_20 = military_expenditure.sort_values(
        by = 'Military expenditures - percent of GDP(%)', ascending=False).head(20)

unemploymnet_vs_military = military_expenditure_20[['Country', 'Military expenditures - percent of GDP(%)', 'Unemployment rate(%)']]


military_expenditure.loc[military_expenditure['Country'].str.startswith('United St')]['Military expenditures - percent of GDP(%)']


military_expenditure.set_index("Country", inplace=True)


ind_vs_pak = military_expenditure.loc[['India', 'Pakistan'], ['GDP', 'Military expenditures - dollar figure',
                         'Military expenditures - percent of GDP(%)',             
                         'Unemployment rate(%)','Life expectancy at birth(years)',
                         'GDP - real growth rate(%)', 'Area(sq km)',
                         'Investment (gross fixed)(% of GDP)', 'Debt - external', 
                         'Inflation rate (consumer prices)(%)',
                         'Infant mortality rate(deaths/1000 live births)']]




