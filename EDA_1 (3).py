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


# In[17]:


plt.figure(figsize=(6,2))
boxplot_data = plt.boxplot(data["Ozone"], vert=False)
[item.get_xdata() for item in boxplot_data['fliers']]


# method 2
# 

# In[18]:


data["Ozone"].describe()


# In[19]:


mu = data["Ozone"].describe()[1]
sigma = data["Ozone"].describe()[2]

for x in data["Ozone"]:
    if ((x < (mu - 3*sigma)) or (x > (mu + 3*sigma))):
        print(x)


# In[20]:


import scipy.stats as stats


# In[21]:


plt.figure(figsize=(8, 6))
stats.probplot(data["Ozone"], dist="norm", plot=plt)
plt.title("Q-Q plot for Outliers Detection", fontsize=14)
plt.xlabel("Theoretical Quantites", fontsize=12)


# In[22]:


sns.violinplot(data=data["Ozone"], color='Lightgreen')
plt.title("viloin plot")


# # other visualizations that could help understand the data 

# In[23]:


sns.violinplot(data=data["Ozone"], color='Lightgreen')
plt.title("viloin plot")
plt.show()


# In[24]:


sns.swarmplot(data=data, x = "Weather" , y = "Ozone",color="orange",palette="Set2", size=6)


# In[25]:


#it is very useful than strip plot 


# In[26]:


sns.stripplot(data=data, x = "Weather" , y = "Ozone",color="orange",palette="Set2", size=6, jitter = True)


# In[27]:


sns.kdeplot(data=data["Ozone"], fill=True, color="blue")
sns.rugplot(data=data["Ozone"], color="black")


# In[28]:


sns.boxplot(data = data, x = "Weather", y="Ozone")


# In[29]:


sns.boxplot(data = data, y="Ozone")


# Correlation coefficient and pair plots

# In[30]:


plt.scatter(data["Wind"], data["Temp"])


# In[31]:


# Compute peearson correlation coefficient
#between wind speed and Temperature
data["Wind"].corr(data["Temp"])


# In[32]:


data_numeric = data.iloc[:,[0,1,2,6]]
data_numeric


# In[33]:


data.head()


# In[34]:


data.info()


# In[35]:


data["Wind"].corr(data["Temp"])


# the correlation between wind and temp is observed to be negatively correlation 

# In[36]:


data_numeric = data.iloc[:,[0,1,2,6]]
data_numeric


# In[37]:


#print correlation coefficient for all the above columns 
data_numeric.corr()


# ##the highest correlation is found between ozone and solar
# 
# 

# In[38]:


sns.pairplot(data_numeric)


# ###TRANSFORMATION

# In[53]:


import pandas as pd
data = pd.get_dummies(data, columns=['Weather'])
data


# In[45]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[54]:


data_numeric.values


# In[59]:


#Normalization of the data
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler

array = data_numeric.values

scaler = MinMaxScaler(feature_range=(0,1))
rescaledX = scaler.fit_transform(array)

#tranformed data
set_printoptions(precision=2)
print(rescaledX[0:10,:])


# In[ ]:




