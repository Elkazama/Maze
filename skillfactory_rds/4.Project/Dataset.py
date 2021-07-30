#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[2]:


df_pribyl = pd.read_csv("C:\\Users\\elias\\Google Диск\\Общая папка\\Airplan\data_pribyl.csv", sep = ',')
df_anapa = pd.read_csv("C:\\Users\\elias\\Google Диск\\Общая папка\\Airplan\data_anapa.csv", sep = ',')


# In[3]:


df_pribyl


# In[4]:


a = df_pribyl['aircraft_code'].str[:]
df_pribyl['Расход ТС-1 в час'] = np.where(a == 'SU9', 1700, np.where(a == '733', 2600,2500)) 


# In[5]:


a = df_pribyl['arrival_airport'].str[:]
df_pribyl['Расход топлива за перелет'] = np.where(a == 'EGO', 1416.6, np.where(a == 'SVO', 4333.3, 13216.)) # Данные со слайда 6
df_pribyl['СОР'] = np.where(a == 'EGO', 14166 , np.where(a == 'SVO', 43333 , 132166)) # Данные со слайда 6


# In[6]:


df_pribyl['pribyl'] = df_pribyl['pribyl'].fillna(1461500)  #среднее число от прибыли полетов в Новокузнецк. Детали на 8 слайде 
df_pribyl['passngrs'] = df_pribyl['passngrs'].fillna(115)  #среднее число пассжиров


# In[10]:


df_pribyl['Процент расходов за перелет'] = df_pribyl['СОР']/df_pribyl['pribyl'] *100


# In[11]:


df_pribyl


# In[21]:


sns.boxplot(x="arrival_airport", y="pribyl",hue = 'Расход топлива за перелет',  data=df_pribyl)


# In[ ]:





# In[ ]:




