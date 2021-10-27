#!/usr/bin/env python
# coding: utf-8

# # Tuple

# ## 1. Allows heterogenous
# ## 2. Index starts from 0 and Retrieve using index
# ## 3. Cann't change data once declared - Immutable
# ## 4. ()

# In[ ]:


sample_tuple = (1,56,3.5,"hi",1+2j)   ### tuple is heterogenous-allows multiple data types
sample_tuple


# In[ ]:


sample_tuple = 1,56,3.5,"hi",1+2j     ### no paranthesis but also it is cpnsidered as tuple
sample_tuple


# In[ ]:


type(sample_tuple)


# In[ ]:


sample_tuple[8]    ### index only from 0 to 4


# In[ ]:


sample_tuple[3]


# In[ ]:


sample_tuple[3] = 13     ###immutable


# In[ ]:


sample_tuple.remove(3)   #Immutable


# In[ ]:


sample_tuple.reverse()


# In[ ]:


A = list(sample_tuple)     #tuple to list conversion
A


# In[ ]:


A.remove(56)
A


# In[ ]:


A.append(8)
A


# In[ ]:


A.insert(3,34)
A


# In[ ]:


# Set
"""
1. Add heterogeneous
2. does not allow duplication
3. cannot be accessed using index
4. immutable using index but mutable
5. ordered-first place
"""


# In[ ]:


set = {21 ,34,65,34.5,43,87,12,"apple","fox","nest"}


# In[ ]:


type(set)


# In[ ]:


set     #output will be in serial-wise


# In[ ]:


set[2]


# In[ ]:


set.remove(34.5)   #remove 34.5 from the set
set


# In[ ]:


set.pop()   # pop randomly picks an element from the set and delete from the set


# In[ ]:


set.pop()


# In[ ]:


set.pop()


# In[ ]:


set.add(669)
set


# # Dictionary

# ### 1. Dictionary has key value pair data structure.
# ### 2. Key is unique and value can be duplicated.
# ### 3. Can retrieve the value using key.
# ### 4. Can change the value using key.
# ### 5. Key is mutable.
# 

# In[ ]:


dic = {1:"alpha",2:"beta",3:"gamma",4:"beta",2:"delta",5:"alpha"}
type(dic)


# In[ ]:


dic[1]   # Value can be retrieved using key


# In[ ]:


dic["alpha"] # key can not be retrieved using value


# In[ ]:


dic[3] = "hero"   # mutable using key
dic


# In[ ]:


dic[8]= "moto"  # we can add key and values to a dictionary
dic


# In[ ]:


dic.reverse()


# In[ ]:


dic.pop(3)  #deletes the key 3
dic


# # Strings

# ### 1. String can be retrieved using index.
# ### 2. String is immutable.

# In[ ]:


a = " My name is Shubhankar Singh"


# In[ ]:


type(a)


# In[ ]:


a


# In[ ]:


a[5]    #Element at index 5


# In[ ]:


a[5]  = "sin"  #Immutable

