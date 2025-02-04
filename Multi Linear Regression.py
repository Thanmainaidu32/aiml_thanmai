#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import influence_plot
import numpy as np


# In[6]:


cars = pd.read_csv("Cars.csv")
cars.head()


# In[7]:


cars = pd.DataFrame(cars, columns=["HP","VOL","SP","WT","MPG"])
cars.head()

- MPG : Milege of the (Mile per Gallon) (This is Y-column to be predicted)
- HP : Horse Power of the car(X1 column)
- VOL : Volume of the car (size) (X2 column)
- SP : Top speed of the car (Miles per Hour)(X3 column)
- WT : Weight of the car (Pounds) (X4 Column)
    
# In[ ]:




