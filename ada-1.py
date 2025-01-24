#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[8]:


data.drop_duplicates(keep='first', inplace = True)
data


# In[ ]:





# In[ ]:




