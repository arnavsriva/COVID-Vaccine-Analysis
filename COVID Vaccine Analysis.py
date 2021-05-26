#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("country_vaccinations.csv")


# In[2]:


data.head()


# In[3]:


data.tail()


# In[4]:


data.isna()


# In[5]:


data.describe()


# In[6]:


pd.to_datetime(data.date)


# In[7]:


data.country.value_counts()


# In[8]:


data = data[data.country.apply(lambda x:x not in ["England","Scotland","Wales", "Northern Ireland"])]
data.country.value_counts()            


# In[9]:


data.vaccines.value_counts()


# In[10]:


df = data[["vaccines","country" ]]
df.head()


# In[11]:


dict1 = {}
for i in df.vaccines.unique():
    dict1[i]=[df["country"][j] for j in df[df["vaccines"]==i].index]

vaccines = {}
for key, value in dict1.items():
    vaccines[key]= set(value)
for i,j in vaccines.items():
    print(f"{i}:>>{j}")


# In[12]:


pip install plotly


# In[13]:


#Visualization
import plotly.express as px
import plotly.offline as py

vaccine_map = px.choropleth(data, locations = 'iso_code', color ='vaccines')
vaccine_map.update_layout(height=400, margin={"r":0, "t":0, "l":0, "b":0})
vaccine_map.show()

