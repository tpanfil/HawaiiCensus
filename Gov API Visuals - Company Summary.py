# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:30:34 2021

@author: JRO20
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly 
import plotly.express as px
import numpy as np
import seaborn as sns
import plotly
import matplotlib.pyplot as plt 


#%% - API KEY

key = 'd3b4c5ff2ca4a0a17f4440470a5390947b980d84'

#url = https://www.census.gov/data/developers/data-sets/abs.2019.html

#%% - Company summary

r1 = requests.request('GET', 'https://api.census.gov/data/2018/abscs?get=GEO_ID,NAME,STATE,NAICS2017,NAICS2017_LABEL,SEX,SEX_LABEL,ETH_GROUP,ETH_GROUP_LABEL,RACE_GROUP,RACE_GROUP_LABEL,VET_GROUP,VET_GROUP_LABEL,EMPSZFI,EMPSZFI_LABEL,YEAR,FIRMPDEMP,FIRMPDEMP_F,RCPPDEMP,RCPPDEMP_F,EMP,EMP_F,PAYANN,PAYANN_F,FIRMPDEMP_S,FIRMPDEMP_S_F,RCPPDEMP_S,RCPPDEMP_S_F,EMP_S,EMP_S_F,PAYANN_S,PAYANN_S_F&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*&key=' + key)

response1 = r1.json()

#%% - Characteristics of Business

#r2 = requests.request('GET', 'https://api.census.gov/data/2018/abscb?get=GEO_ID,NAME,NAICS2017,NAICS2017_LABEL,SEX,SEX_LABEL,ETH_GROUP,ETH_GROUP_LABEL,RACE_GROUP,RACE_GROUP_LABEL,VET_GROUP,VET_GROUP_LABEL,QDESC,QDESC_LABEL,BUSCHAR,BUSCHAR_LABEL,YEAR,FIRMPDEMP,FIRMPDEMP_F,FIRMPDEMP_PCT,FIRMPDEMP_PCT_F,RCPPDEMP,RCPPDEMP_F,RCPPDEMP_PCT,RCPPDEMP_PCT_F,EMP,EMP_F,EMP_PCT,EMP_PCT_F,PAYANN,PAYANN_F,PAYANN_PCT,PAYANN_PCT_F,FIRMPDEMP_S,FIRMPDEMP_S_F,FIRMPDEMP_PCT_S,FIRMPDEMP_PCT_S_F,RCPPDEMP_S,RCPPDEMP_S_F,RCPPDEMP_PCT_S,RCPPDEMP_PCT_S_F,EMP_S,EMP_S_F,EMP_PCT_S,EMP_PCT_S_F,PAYANN_S,PAYANN_S_F,PAYANN_PCT_S,PAYANN_PCT_S_F&for=us:*&key=' + key)

#response2 = r2.json()

#%% -- Business Owners

#r3 = requests.request('GET', 'https://api.census.gov/data/2018/abscbo?get=GEO_ID,NAME,NAICS2017,NAICS2017_LABEL,OWNER_SEX,OWNER_SEX_LABEL,OWNER_ETH,OWNER_ETH_LABEL,OWNER_RACE,OWNER_RACE_LABEL,OWNER_VET,OWNER_VET_LABEL,QDESC,QDESC_LABEL,OWNCHAR,OWNCHAR_LABEL,YEAR,OWNPDEMP,OWNPDEMP_F,OWNPDEMP_PCT,OWNPDEMP_PCT_F,OWNPDEMP_S,OWNPDEMP_S_F,OWNPDEMP_PCT_S,OWNPDEMP_PCT_S_F&for=us:*&key=' + key)

#response3 = r3.json()

#%% -- Technology Characteristics of Business

#r4 = requests.request('GET', 'https://api.census.gov/data/2018/abstcb?get=GEO_ID,NAME,NAICS2017,NAICS2017_LABEL,SEX,SEX_LABEL,ETH_GROUP,ETH_GROUP_LABEL,RACE_GROUP,RACE_GROUP_LABEL,VET_GROUP,VET_GROUP_LABEL,NSFSZFI,NSFSZFI_LABEL,FACTORS_P,FACTORS_P_LABEL,YEAR,FIRMPDEMP,FIRMPDEMP_F,FIRMPDEMP_PCT,FIRMPDEMP_PCT_F,RCPPDEMP,RCPPDEMP_F,RCPPDEMP_PCT,RCPPDEMP_PCT_F,EMP,EMP_F,EMP_PCT,EMP_PCT_F,PAYANN,PAYANN_F,PAYANN_PCT,PAYANN_PCT_F,FIRMPDEMP_S,FIRMPDEMP_S_F,FIRMPDEMP_PCT_S,FIRMPDEMP_PCT_S_F,RCPPDEMP_S,RCPPDEMP_S_F,RCPPDEMP_PCT_S,RCPPDEMP_PCT_S_F,EMP_S,EMP_S_F,EMP_PCT_S,EMP_PCT_S_F,PAYANN_S,PAYANN_S_F,PAYANN_PCT_S,PAYANN_PCT_S_F&for=us:*&key=' + key)

#response4 = r4.json()

#%% -- Into DFs

CompanySummaryDF = pd.DataFrame(response1[1:], columns = response1[0])
#CompanySummaryDF.EMP = CompanySummaryDF.EMP.astype(str).astype(float)

#CharBusinessDF = pd.DataFrame(response2[1:], columns = response2[0])

#BusinessOwnersDF = pd.DataFrame(response3[1:], columns = response3[0])

#TechDF = pd.DataFrame(response4[1:], columns = response4[0])

#%% -- Whittle down to Honolulu 

Index = []
for index, i in enumerate(CompanySummaryDF.NAME):
    if 'Urban Honolulu, HI Metro Area' in i:
        Index.append(index)
        
FinalDF = CompanySummaryDF.iloc[Index]

#%% -- Reduce unwanted columns

print(FinalDF.columns)

cols = ['NAME', 'NAICS2017_LABEL',
       'SEX_LABEL', 'ETH_GROUP_LABEL',
       'RACE_GROUP_LABEL', 'VET_GROUP_LABEL',
       'EMPSZFI_LABEL', 'FIRMPDEMP',
       'EMP', 'PAYANN', 'FIRMPDEMP_S', 
       'EMP_S',
       'PAYANN_S']

FinalDF = FinalDF[cols]


#%%  - DF Info and type assignment

print('DF Info:\n')
print(FinalDF.info())

FinalDF.FIRMPDEMP = FinalDF.FIRMPDEMP.astype(str).astype(float)
FinalDF.FIRMPDEMP_S = FinalDF.FIRMPDEMP_S = FinalDF.FIRMPDEMP_S.astype(str).astype(float)
FinalDF.EMP = FinalDF.EMP.astype(str).astype(float)
FinalDF.EMP_S = FinalDF.EMP_S.astype(str).astype(float)
FinalDF.PAYANN = FinalDF.PAYANN.astype(str).astype(float)
FinalDF.PAYANN_S = FinalDF.PAYANN_S.astype(str).astype(float)

#%% - DF Basic Info

print('DF Info:\n')
print(FinalDF.info())
print('DF Description:\n')
print(FinalDF.describe())


#%% -- Correlation Matrix

CorDF = FinalDF[['FIRMPDEMP', 'EMP', 'PAYANN']]
CorDF.columns = ['Number_of_Employer_Firms', 'Number_of_Employers', 'Annual_Payroll(ten-millions)']

plt.figure(figsize = (16, 12))
sns.heatmap(CorDF.corr(), cmap='YlGnBu', annot=True, fmt='.2f').set(title = 'Correlation Matrix');


#%% - Boxplots -- SUX

EMP = FinalDF.EMP
FIRMPDEMP = FinalDF.FIRMPDEMP
PAYANN = FinalDF.PAYANN

BoxData = [EMP, FIRMPDEMP, PAYANN]

fig = plt.figure(figsize =(10, 7))

ax = fig.add_axes([0, 0, 1, 1])

bp = ax.boxplot(BoxData, patch_artist=True)

colors = ['#463F1A', '#FFA400', '#F9EBE0']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.set_xticklabels(['EMP', 'FIRMPDEMP', 'PAYANN'])
ax.set_ylabel('Value')
ax.set_xlabel('Variable')
plt.title('EMP, FIRMPDEMP and PAYANN Boxplots')
plt.show()


#%% -- Hist of each variable and scatter of relationships

NoTotalDF = FinalDF[FinalDF['SEX_LABEL'] != 'Total']
NoTotalDF = NoTotalDF[NoTotalDF['SEX_LABEL'] != 'Classifiable']
cols = ['NAME', 'NAICS2017_LABEL', 'Sex', 'ETH_GROUP_LABEL',
       'RACE_GROUP_LABEL', 'VET_GROUP_LABEL', 'EMPSZFI_LABEL', 'Number_of_Employer_Firms',
       'Number_of_Employees', 'Annual_Payroll(ten-millions)', 'FIRMPDEMP_S', 'EMP_S', 'PAYANN_S']

NoTotalDF.columns = cols 

g = sns.PairGrid(data=NoTotalDF, vars=['Number_of_Employees', 'Number_of_Employer_Firms', 'Annual_Payroll(ten-millions)'],
                 hue = 'Sex', height=3, palette='Set1')
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
g.add_legend();


#%% - Bar plot 

plot_data = NoTotalDF.groupby(['Sex'])['Number_of_Employees'].mean().reset_index()


sns.barplot(x = 'Number_of_Employees', y = 'Sex', data = plot_data).set(title = 'Mean Employees by Sex')
plt.ylabel('Sex')
plt.xlabel('Mean Number of Employees')


































