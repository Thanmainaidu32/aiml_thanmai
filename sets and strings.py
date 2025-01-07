#!/usr/bin/env python
# coding: utf-8

# In[43]:


s1 ={1,8,9,0,10,9,0,1,}
print(s1)
print(type(s1))


# In[44]:


lst1 = [0,1,8,9,10,20,78,8,8,8]


# In[45]:


s2 = set(lst1)
print(s2)
print(type(s2))


# In[46]:


s1 = {1,2,3,4}
s2 = {3,4,5,6}


# In[47]:


s1 | s2


# In[48]:


s1.union(s2)


# In[49]:


s1 = {1,2,3,4}
s2 = {3,4,5,6}


# In[50]:


s1 & s2


# In[51]:


s1.intersection(s2)


# In[52]:


s1 = {2,3,5,6,7}
s2 = {5,6,7}


# In[53]:


s1 - s2


# In[54]:


s2 - s1


# In[55]:


# symmetric difference
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}


# In[56]:


s1.symmetric_difference(s2)


# In[57]:


s2.symmetric_difference(s1)


# In[58]:


#strings


# In[59]:


str1 = "welcome to aiml class"
print(str1)
str2 ='we strated with the python'
print(str2)
str3 = '''This is an awsome class'''
print(str3)


# In[60]:


str = '''he said,"It's awsome!"'''
print(str)


# In[61]:


#slice
print(str1)
str1[5:10]


# In[62]:


#reverse
str1[::-1]


# In[63]:


dir(str)


# In[64]:


#split
print(str1)
str1.split()


# In[65]:


#join
str4 = "Hello.How are you?"
' '.join(str4)


# In[66]:


reviews = ["the product is awsome" , "Great service"]
' '.join(reviews)


# In[67]:


#strip
str5 = "   Hello, how are you?   "
str5


# In[68]:


str5.strip()


# In[69]:


sales_data = {
    "ProductID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "ProductName": ["Laptop", "Mouse", "Keyboard", "Monitor", "Chair", "Desk", "Webcam", "Headphones", "Printer", "Tablet"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Furniture", "Furniture", "Electronics", "Accessories", "Electronics", "Electronics"],
    "PriceRange": ["High", "Low", "Low", "Medium", "Medium", "Medium", "Low", "Low", "Medium", "High"],
    "StockAvailable": [15, 100, 75, 20, 10, 8, 50, 60, 25, 12],
}


# In[70]:


for k,v in sales_data.items():
    print(k,set(v), end =',')
    print('/n')


# In[71]:


# Original reviews dictionary
#we use this in meachine learning code
reviews = {
    "Review1": "The product quality is excellent and delivery was prompt. The product functionality is versatile",
    "Review2": "Good service but the packaging could have been better. The customer service has to improve",
    "Review3": "The product works fine, but the customer support is not very helpful. I rate the product as excellent",
}

review_analysis = {}
for key, review in reviews.items():
    words = review.lower().replace('.', '').replace(',', '').split() 
    review_analysis[key] = {
        "WordCount": len(words),
        "UniqueWords": list(set(words))
    }
review_analysis


# In[72]:


#how  to use for loop 
d1 = {"ram":180, "shaym": 170, "ramya":176}


# In[73]:


for k in d1.keys():
    print(k)


# In[74]:


for v in d1.values():
    print(v)


# In[75]:


for k,v in d1.items():
    print(k,v)


# In[77]:


d1["john"] = 165
d1


# In[ ]:




