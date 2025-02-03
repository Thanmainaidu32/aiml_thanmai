#!/usr/bin/env python
# coding: utf-8

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


data1.isnull().sum()


# In[5]:


data1.describe()


# In[6]:


import matplotlib.pyplot as plt

plt.figure(figsize=(6, 3))  # Set figure size
plt.title("Box plot for Daily Sales")  # Set title
plt.boxplot(data1["daily"], vert=False)  # Create horizontal box plot
plt.show()  # Display the plot


# In[7]:


sns.histplot(data1['daily'], kde = True,stat='density',)
plt.show


# # OBSERVATIONS
# 
# 

#     There are no missing values .
#     The daily column values appears to be right skewed.
#     The sunday column values appear to be right skewed. 
#     There are two outliers in both daily column and also in sunday column as observed from the boxplot

# In[8]:


x= data1['daily']
y = data1["sunday"]
plt.scatter(data1["daily"], data1["sunday"])
plt.xlim(0, max(x) + 100)
plt.ylim(0, max(y) + 100)
plt.show()


# In[9]:


data1["daily"].corr(data1["sunday"])


# In[10]:


data1[["daily","sunday"]].corr()


# In[11]:


data1.corr(numeric_only=True)


# # OBSERVATION ON CORRELATION STRENGTH
# 
#     .The relationship between x(daily) and y (sunday) is seen to be linear as seen from scatter plot
#     .The correlation is strong and positive with Pearson's correlation coefficient of 0.958154

# In[12]:


import statsmodels.formula.api as smf
model1 = smf.ols("sunday~daily", data = data1).fit()


# In[13]:


model1.summary()


# INTERPRETATION 
#         R square=1 -> perfect fit(ALL varience explianed).
#     R square=0-> Model does not explian any variance.
#     R square close to 1 ->Good model fit.
#     R square close to 0 ->poor model fit.
# 

# In[14]:


# plot the scatter plot and overlay the fitted straight line using matplotlib
x = data1["daily"].values
y = data1["sunday"].values
plt.scatter(x, y, color = "m", marker = "o", s = 30)
b0 = 13.84
b1 = 1.33
# predicated response vctor
y_hat = b0 + b1*x

#ploting the regression line
plt.plot(x, y_hat, color = "g")

#putting labels
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# OBSERVATIONS FROM SUMMERY
# >the probability (P_value) for intercept (beta_0) is 0.707>0.05
# >therefore that intercept coefficient may not be that much significant in prediction 
# >However the p-value for "Daily"(beta_1) is < 
# >therefor the beta_1 coefficient is hihgly significant and contributition prediction

# In[15]:


model1.params


# In[16]:


print(f'model t-values:\n{model1.tvalues}\n------------\nmodel p-values: \n{model1.pvalues}')


# In[17]:


model1.rsquared,model1.rsquared


# In[18]:


newdata=pd.Series([200,300,15000])


# In[21]:


data_pred=pd.DataFrame(newdata,columns=['daily'])
data_pred


# In[22]:


model1.predict(data_pred)


# In[24]:


#predicting on all given training data
pred = model1.predict(data1["daily"])


# In[26]:


#Add predicted value as a column in data1
data1["Y_hat"] = pred
data1


# In[30]:


#compute the eroor value(residual) and add as another column
data1["residuals"]= data1["sunday"]-data1["Y_hat"]
data1


# In[ ]:




