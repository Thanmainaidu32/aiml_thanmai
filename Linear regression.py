#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf



# In[3]:


data1 = pd.read_csv("NewspaperData.csv")
data1


# In[6]:


data1.info()


# In[5]:


data1.isnull().sum()


# In[4]:


data1.describe()


# In[9]:


import matplotlib.pyplot as plt

plt.figure(figsize=(6, 3))  # Set figure size
plt.title("Box plot for Daily Sales")  # Set title
plt.boxplot(data1["daily"], vert=False)  # Create horizontal box plot
plt.show()  # Display the plot


# In[11]:


sns.histplot(data1['daily'], kde = True,stat='density',)
plt.show


# # OBSERVATIONS
# 
# 

#     There are no missing values .
#     The daily column values appears to be right skewed.
#     The sunday column values appear to be right skewed. 
#     There are two outliers in both daily column and also in sunday column as observed from the boxplot

# In[12]:


x= data1['daily']
y = data1["sunday"]
plt.scatter(data1["daily"], data1["sunday"])
plt.xlim(0, max(x) + 100)
plt.ylim(0, max(y) + 100)
plt.show()


# In[13]:


data1["daily"].corr(data1["sunday"])


# In[14]:


data1[["daily","sunday"]].corr()


# In[15]:


data1.corr(numeric_only=True)


# # OBSERVATION ON CORRELATION STRENGTH
# 
#     .The relationship between x(daily) and y (sunday) is seen to be linear as seen from scatter plot
#     .The correlation is strong and positive with Pearson's correlation coefficient of 0.958154

# In[16]:


import statsmodels.formula.api as smf
model1 = smf.ols("sunday~daily", data = data1).fit()


# In[17]:


model1.summary()


# In[ ]:




