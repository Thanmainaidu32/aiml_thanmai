#!/usr/bin/env python
# coding: utf-8

# IMPORT libraries and data set

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


# In[2]:


data1 = pd.read_csv("NewspaperData.csv")
data1


# In[3]:


data1.info()


# In[4]:


data1.describe()


# In[5]:


fig, axes = plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios': [1, 3]})
sns.boxplot(data1=data1["Newspaper"], ax=axes[0], color='skyblue', width=0.5, orient = 'h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("sunday")
sns.histplot(data1["Newspaper"], kde=True, ax=axes[1], color='purple', bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("sunday")
axes[1].set_ylabel("daily")
plt.tight_layout()
plt.show()


# In[6]:


plt.scatter(data1["sunday"], data1["daily"])


# ##a positive corelation strength is observed between daily and sunday

# In[7]:


fig,axes=plt.subplots(2,1,figsize=(8,6),gridspec_kw={'height_ratios':[1,3]})
sns.boxplot(data1=data1['Newspaper'],ax=axes[0],color='skyblue',width=2.5,orient='h')
axes[0].set_title('Boxplot')
axes[0].set_xlabel(' Sales')
sns.histplot(data1["daily"],kde=True,ax=axes[1],color='purple',bins=30)
axes[1].set_title("Newspaper")
axes[1].set_xlabel("Daily")
axes[1].set_ylabel("Sunday")
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




