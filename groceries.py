#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("Groceries_dataset.csv")
print(data)


# In[3]:


data.info()


# In[4]:


data.info()


# In[5]:


data.isnull().sum()


# In[6]:


data.tail()


# In[7]:


data.head()


# In[8]:


data[data.duplicated()]


# In[9]:


data.drop_duplicates(keep='first', inplace = True)
data


# In[11]:


fig, axes = plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios': [1, 3]})
sns.boxplot(data=data["Member_number"], ax=axes[0], color='skyblue', width=0.5, orient = 'h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("item")
sns.histplot(data["Member_number"], kde=True, ax=axes[1], color='purple', bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("item")
axes[1].set_ylabel("Member_number")
plt.tight_layout()
plt.show()


# In[14]:


#import necessary libraries
import pandas as pd 
import mlxtend
from mlxtend.frequent_patterns import apriori,association_rules
import matplotlib.pyplot as plt


# In[17]:


import os
import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import operator as op
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules



# In[19]:


data.Date = pd.to_datetime(data.Date)
data.memberID = data['Member_number'].astype('str')
data.info()


# In[20]:


sns.pairplot(data)
plt.show()


# In[21]:


Sales_weekly = data.resample('w', on='Date').size()
fig = px.line(data, x=Sales_weekly.index, y=Sales_weekly,
              labels={'y': 'Number of Sales',
                     'x': 'Date'})
fig.update_layout(title_text='Number of Sales Weekly',
                  title_x=0.5, title_font=dict(size=18))
fig.show()


# In[23]:


Unique_customer_weekly = data.resample('w', on='Date').Member_number.nunique()
fig = px.line(Unique_customer_weekly, x=Unique_customer_weekly.index, y=Unique_customer_weekly,
              labels={'y': 'Number of Customers'})
fig.update_layout(title_text='Number of Customers Weekly',
                  title_x=0.5, title_font=dict(size=18))
fig.show()


# In[ ]:




