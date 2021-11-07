#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr = np.array([1,2,3,4,5])
mean = np.mean(arr)
print(mean)


# In[2]:


median=np.median(arr)
print(median)


# In[11]:


from scipy import stats
print(stats.mode(arr))
print(np.var(arr))
print(np.std(arr))


# In[10]:


ar = np.array([1,2,3,4,5,500])
print(np.mean(ar))
print(np.median(ar))
print(stats.mode(ar))
print(np.var(ar))
print(np.std(ar))


# In[9]:


a = np.array([5,8,11,14,17,22])
print(np.mean(a))
print(np.median(a))
print(stats.mode(a))
print(np.var(a))
print(np.std(a))


# In[8]:


b = np.array([2,4,4,6,8])
print(np.mean(b))
print(np.median(b))
print(stats.mode(b))
print(np.var(b))
print(np.std(b))

