#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np


# In[4]:


df=pd.read_csv("Universities.csv")
df


# In[8]:


np.mean(df["SAT"])


# In[9]:


np.median(df["SAT"])


# In[10]:


np.std(df["GradRate"])


# In[6]:


np.var(df["SFRatio"])


# In[11]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[13]:


plt.figure(figsize=(6,3))
plt.title("Graduation Rate")
plt.hist(df["GradRate"])


# In[ ]:




