#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json


# # Part 1

# In[60]:


df = pd.read_csv("data.csv")
df_copy = df #making a copy 

print(len(df_copy))


# In[61]:


df_copy["Profit (in millions)"].tolist() #did a quick check found that non-numeric was NA
numeric_filter = df_copy["Profit (in millions)"] != "N.A." 
df_copy = df_copy[numeric_filter]

print(len(df_copy))


# In[4]:


df_copy.head()


# # Part 2

# In[19]:


for num in df_copy["Profit (in millions)"]:
    df_copy["Profit (in millions)"].replace(to_replace = num, value = float(num))


# In[45]:


#making JSON
# data2 = df_copy.to_json()
df_copy.to_json(r'C:\Users\woods\Documents\GCP Challenge\data2.json')


# In[59]:


df_copy.sort_values(by=["Profit (in millions)"], inplace=True, ascending = False)

for i in range(0,20):
    print(df_copy.iloc[i,:])

