#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[25]:


df = pd.read_csv(r'D:\New folder\Fitness_trackers (2).csv')
df.head()


# In[17]:


df['Brand Name'].groupby(df['Device Type']).count().sort_values(ascending=False)


# In[18]:


df.shape


# In[19]:


df.describe()


# In[20]:


# Device Type distribution
labels = 'Smart watches', 'Fitness bands'
sizes = [490,75]
fig1, ax1 = plt.subplots()
fig1.set_facecolor('black')
ax1.pie(sizes, labels=labels, colors=["blue",'orange'],autopct='%1.1f%%', startangle=90,textprops={'color':'w','weight':'bold','fontsize':12.5})
ax1.axis('equal')
plt.show()


# In[21]:


#count of brands
df['Brand Name'].nunique()


# In[22]:


#top 10 brands
df['Brand Name'].groupby(df['Brand Name']).count().sort_values(ascending=False).iloc[:10]


# In[23]:


#product counts
sns.set_style('white')
sns.countplot(y="Brand Name", hue="Device Type", data=df, palette=["yellow","red"],
              order=df["Brand Name"].value_counts().iloc[:10].index)


# In[24]:


# Brandwise Mean Selling prices
round(df.groupby('Brand Name')['Average Battery Life (in days)'].mean(),0).sort_values(ascending=False)


# In[11]:


df['Device Type'].groupby(df['Brand Name']).count().sort_values(ascending=False).iloc[:1]


# In[12]:


# Brandwise Mean Selling prices
round(df.groupby('Brand Name')['Average Battery Life (in days)'].mean(),0).sort_values(ascending=False)


# In[13]:


#color palette for this notebook
colors = ["#F72585","#B5179E","#7209B7","#560BAD","#480CA8","#3A0CA3","#3F37C9","#4361EE","#4895EF","#4CC9F0","#a5a58d"]
palette = sns.color_palette(palette = colors)

sns.palplot(palette, size =1)
plt.show()


# In[14]:


# Rating vs Selling Price
#filter by Brand
list = ["APPLE","OnePlus","FOSSIL ","SAMSUNG","Honor","FitBit","Xiaomi","Huawei","huami","realme"]
series = df["Brand Name"].isin(list)
df_f = df[series]
fig, ax = plt.subplots(figsize=(15,6))
ax = sns.stripplot(x="Rating (Out of 5)", y="Selling Price", data=df_f,hue="Brand Name", palette=colors,size=7, marker="o")


# In[15]:


round(df.groupby('Brand Name')['Average Battery Life (in days)'].mean(),0).sort_values(ascending=False)


# In[26]:


#average battery life
data={"Brand Name":["GARMIN","huami","Oppo","Xiaomi","SAMSUNG","Honor","Huawei","realme","OnePlus","boAt","Noise","GOQii","LAVA","FitBit","LCARE","Fastrack","FOSSIL","Noise","Infinix","APPLE"],
      "Avg Battery Life":[17.0,16.0,14.0,12.0,12.0,12.0,11.0,10.0,9.0,8.0,7.0,7.0,7.0,7.0,6.0,6.0,5.0,5.0,4.0,1.0]}
df_batt=pd.DataFrame(data)

sns.set_style('white')
plt.figure(figsize=(10,7))
ax=sns.barplot(x="Avg Battery Life", y="Brand Name",data=df_batt, palette= colors)


# In[27]:


#Color counts
sns.countplot(y="Color", hue="Device Type", data=df, palette=colors,
              order=df["Color"].value_counts().iloc[:5].index)


# In[28]:


#commonly available strap
sns.countplot(y="Strap Material", hue="Device Type", data=df, palette=colors,
              order=df["Strap Material"].value_counts().iloc[:5].index)


# In[30]:


fig, ax = plt.subplots(figsize=(24,5))
ax = sns.stripplot(y="Selling Price", x="Brand Name", data=df,palette=colors)


# In[ ]:





# In[ ]:




