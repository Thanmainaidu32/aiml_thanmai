#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from sklearn.cluster import KMeans
import seaborn as sns


# In[2]:


Univ = pd.read_csv("Universities.csv")
Univ


# In[3]:


Univ.info()


# In[4]:


Univ.isna().sum()


# In[5]:


plt.figure(figsize=(10, 6))  
plt.boxplot(Univ['SAT'], vert=False)  
plt.title('Boxplot of Universities')  
plt.xlabel('SAT')  
plt.show()  


# In[6]:


#**read all numeric columns into Univ1**
Univ1 = Univ.iloc[:,1:]


# In[7]:


Univ1


# In[8]:


cols= Univ.columns
cols


# In[11]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_Univ_df = pd.DataFrame(scaler.fit_transform(Univ1),columns = cols )
scaled_Univ_df


# In[ ]:




