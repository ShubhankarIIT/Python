#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


sample = np.arange(1,31)
sample


# In[ ]:


sample+sample   #array will be added


# In[ ]:


np.exp(sample)         #exponent of nos


# In[ ]:


np.log(sample)    #log of each element of array


# In[ ]:


np.sqrt(sample)    #square root


# In[ ]:


np.square(sample)   #square of nos


# In[ ]:


np.std(sample)      #std deviation


# In[ ]:


np.mean(sample)


# In[ ]:


array = np.random.randn(3,4) 
array      ## normal distribution


# In[ ]:


np.round(array,decimals = 3)


# In[ ]:


sports = np.array(['golf','cricket','chess','khokho','chess'])
sports


# In[ ]:


sports = np.array(['golf','cricket','chess','khokho','chess'])    #unique elements
np.unique(sports)


# # Pandas

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# # Pandas DataFrame and Indexing

# In[3]:


sports1 = pd.Series([1,2,3,4],index = ['cricket','football','basketball','golf'])
sports1


# In[4]:


sports1['football']


# In[5]:


sports2 = pd.Series([11,12,13,5],index = ['cricket','football','baseball','golf'])
sports2


# In[6]:


sports1 + sports2


# In[7]:


df1 = pd.DataFrame(np.random.rand(10,8),index = 'A B C D E F G H I J'.split(),columns = 'Score1 Score2 Score3 Score4 Score5 Score6 Score7 Score8'.split())
df1


# In[8]:


df1['Score5']          #obtain a particular column


# In[9]:


df1[['Score3','Score7']]    #multiple columns


# In[10]:


df1['Score 9']=df1['Score2']+df1['Score4']
df1


# In[11]:


df1.drop('Score4',axis=1)  # to remove a column use axis = 1 


# In[12]:


df1.drop('G')    #to remove a row use axis = 0 or nothing


# In[13]:


df1.drop(['Score1','Score6'],axis = 1)


# In[16]:


df2 = {'ID':[101,102,103,104,105],'Name':['John','Mary','Joe','Ankit','Babulal'],'Profit':[20,30,12,45,23]}
df=pd.DataFrame(df2)
df


# In[17]:


df.drop('ID',axis = 1)


# In[18]:


df.drop(4)


# In[19]:


df['Name']

