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


# In[9]:


import pandas as pd
from sklearn.preprocessing import StandardScaler
cols = Univ1.columns
Univ1.drop_duplicates(keep='first', inplace=True)
scaler = StandardScaler()
scaled_Univ_df = pd.DataFrame(scaler.fit_transform(Univ1), columns=cols)
scaled_Univ_df.to_csv('scaled_university.csv', index=False)
print(scaled_Univ_df)


# In[10]:


from sklearn.cluster import KMeans
clusters_new = KMeans(3, random_state=0)
clusters_new.fit(scaled_Univ_df)


# In[11]:


clusters_new.labels_


# In[12]:


set(clusters_new.labels_)


# In[13]:


Univ['clusterid_new'] = clusters_new.labels_


# In[14]:


Univ


# In[15]:


Univ.sort_values(by = "clusterid_new")


# In[16]:


Univ.iloc[:,1:].groupby("clusterid_new").mean()


# **OBSERVATIONS**
# + cluter 2 appears to be the top rated universities cluster as the cutoff score, top 10,SF ratio parameters mean values are highest cluster
# + Cluster one appears to occupy the middle level rated University
# + Cluster 0 comes as the lower level rated universities
# 

# In[17]:


Univ[Univ['clusterid_new']==0]


# In[27]:


wcss = []
for i  in range(1, 20):
    Kmeans = KMeans(n_clusters=i,random_state=0)
    kmeans.fit(scaled_Univ_df)
    wcss.append(Kmeans.inertia_)
print(wcss)
plt.plot(range(1, 20), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


# from the above graph we can choose k = 3  or 4 which indicates the elbow joint i.e the rate of change of slope decreces

# In[ ]:




