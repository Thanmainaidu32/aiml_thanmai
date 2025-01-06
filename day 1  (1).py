#!/usr/bin/env python
# coding: utf-8

# In[1]:


#list
l=[100,50,193,443,256,53,1000]


# In[7]:


l1 = []
l2 = []
for x in l:
    if x%2 == 0:
        l1.append(x)
    else:
        l2.append(x)
print ("even:",l1)
print ("odd:",l2)


# In[14]:


l=["A",100,"B",20.5,True,6+8j]
s = []
i = []
b = []
n = []
f = []
for x in l:
    if type(x) == str:
        s.append(x)
    elif type(x) == int:
        i.append(x)
    elif type(x) == bool:
        b.append(x)
    elif type(x) == complex:
        n.append(x)
    elif type(x) == float:
        f.append(x)
print(s)
print(i)
print(b)
print(n)
print(f)
    


# In[1]:


#heterogeneous 
my_list = [1, "hello" , 3.41, 8+6j]
print(my_list)


# In[6]:


#indexing and slicing 
my_list = [10,20,30,40,50]
print(my_list[1])
print(my_list[1:3])
print(my_list[1:])
print(my_list[:3])
print(my_list[:])


# In[7]:


#iterable
my_list = [10,20,30,40,50]
for item in my_list:
    print(3*item)


# In[12]:


my_list = [10,20,30,40,50]
for x in range(len(my_list)):
    print(3*my_list[x])


# In[13]:


#duplicate_values
duplicate_values = [1,2,3,4,5]
duplicate_values


# In[15]:


#support nesting
nested_list = [[1,2],[2,3]]
nested_list


# In[16]:


dir(list)


# In[7]:


#orders
orders = [["apple ",10] , ["banana",5] , ["cherry" ,7] , ["banana" , 7]]
orders


# In[8]:


new_orders1 = ["date", 12]
orders.append(new_orders1)
orders


# In[11]:


new_orders = [["grape", 9], ["apple",20]]
orders.extend(new_orders)
orders


# In[12]:


#insert
new_order2 = ["dragon", 10]
orders.insert(3,new_order2)
orders


# In[13]:


#remove duplicate
duplicate_order = ["banana", 5]
orders.pop(4)


# In[ ]:





# In[21]:


orders = [['apple ', 10], ['banana', 5], ['cherry', 7],['dragon',10],['grape',9],['apple',20]]
for each in orders:
    if each[0] == "cherry":
        each[1] = 10
        print(orders)


# In[27]:


orders = [['apple',10],['banana',5],['cherry',7],['dragon',10],['grape',9],['apple',20]]
apple_orders = []
for each in orders:
    if each[0] == 'apple':
        apple_orders.append(each[1])
print(apple_orders)
print(sum(apple_orders))


# In[ ]:





# In[1]:


#tupple
tup1=(3,5,9,10)
tup2=(10,20,30,"hi")
tup3=tuple([1,2,5,7])
print(tup1,tup2,tup3)
tup4=([3,4,5],(1,3,6),"hello",10.5)
print(tup4)
tup4[1][1] = 100



# In[3]:


tup4.index('hello')


# In[5]:


tup5 = (10,20,1,10,10,30,10,10)
tup5.count(10)


# In[ ]:




