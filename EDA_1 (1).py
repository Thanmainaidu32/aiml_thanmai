#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[3]:


data[data.duplicated()]


# In[4]:


data.drop_duplicates(keep='first', inplace = True)
data


# # rename the colum

# In[5]:


data.rename({'Solar.R': 'Solar'}, axis=1, inplace = True)
data


# impute the missing values

# In[6]:


data.info()


# In[7]:


data.isnull().sum()


# In[8]:


cols = data.columns
colors = ['black' , 'yellow']
sns.heatmap(data[cols].isnull(),cmap=sns.color_palette(colors),cbar = True)


# In[9]:


median_Ozone = data["Ozone"].median()
mean_Ozone = data["Ozone"].mean()
print("Median of Ozone: ", median_Ozone)
print("Mean of Ozone: ", mean_Ozone)


# In[10]:


data['Ozone'] = data['Ozone'].fillna(median_Ozone)
data.isnull().sum()


# In[11]:


mean_Solar = data["Solar"].mean()
mean_Solar


# In[12]:


print(data["Weather"].value_counts())
mode_Weather = data["Weather"].mode()[0]
print(mode_Weather)


# In[13]:


data["Weather"] = data["Weather"].fillna(mode_Weather)
data.isnull().sum()


# In[14]:


fig, axes = plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios': [1, 3]})
sns.boxplot(data=data["Ozone"], ax=axes[0], color='skyblue', width=0.5, orient = 'h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("Ozone Levels")
sns.histplot(data["Ozone"], kde=True, ax=axes[1], color='purple', bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Ozone Levels")
axes[1].set_ylabel("Frequecy")
plt.tight_layout()
plt.show()


# observations
# >The ozone column has extreme values beyond 81 as seen from boxblot
# >The same is confirmed from the bellow right=Skewed histogram
# 

# In[15]:


fig, axes = plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios': [1, 3]})
sns.boxplot(x=data["Solar"], ax=axes[0], color='skyblue', width=0.5)
axes[0].set_title("Boxplot")
axes[0].set_xlabel("Solar Levels")
sns.histplot(data["Solar"], kde=True, ax=axes[1], color='purple', bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Solar Levels")
axes[1].set_ylabel("Frequency")
plt.tight_layout()
plt.show()


# >>solar has no outliers are observed 
# >>the solar distribution is not perfectly symmetric but slightly skewed

# In[16]:


plt.figure(figsize=(6,2))
plt.boxplot(data["Ozone"], vert= False)


# In[19]:


plt.figure(figsize=(6,2))
boxplot_data = plt.boxplot(data["Ozone"], vert=False)
[item.get_xdata() for item in boxplot_data['fliers']]


# method 2
# 

# In[25]:


data["Ozone"].describe()


# In[26]:


mu = data["Ozone"].describe()[1]
sigma = data["Ozone"].describe()[2]

for x in data["Ozone"]:
    if ((x < (mu - 3*sigma)) or (x > (mu + 3*sigma))):
        print(x)


# In[27]:


import scipy.stats as stats


# In[28]:


plt.figure(figsize=(8, 6))
stats.probplot(data["Ozone"], dist="norm", plot=plt)
plt.title("Q-Q plot for Outliers Detection", fontsize=14)
plt.xlabel("Theoretical Quantites", fontsize=12)


# In[30]:


sns.violinplot(data=data["Ozone"], color='Lightgreen')
plt.title("viloin plot")


# In[ ]:




