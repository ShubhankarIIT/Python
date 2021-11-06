#!/usr/bin/env python
# coding: utf-8

# # Numpy : Package for Multi-dimensional array

# ### Vector(1-D)
# ### Matrix(2-D or 1-D)

# In[ ]:


# Create an array
import numpy as np


# In[ ]:


a= [2,6,4]
np.array(a)


# In[ ]:


arr = np.array([3,7,12])
arr


# In[ ]:


type(arr)


# In[ ]:


list_of_list=[[2,5,8],[5,7,8],[3,6,5]]
np.array(list_of_list)


# In[ ]:


array = np.array([[0,5,3],[6,5,4],[1,5,9]])
array


# In[ ]:


np.arange(2,100)  #number from 2 to 99


# In[ ]:


np.arange(5,45,9)   #no. from 5 to 45 with a gap of 9 excluding 45


# In[ ]:


np.zeros(6)      #six zeros of float type


# In[ ]:


np.zeros(6,dtype = int)     #six zeros of integer type


# In[ ]:


np.ones(8)


# In[ ]:


np.ones(9,dtype = int)


# In[ ]:


np.ones((3,5),dtype = int)


# In[ ]:


np.linspace(0,1,20)   #linearly spaced between 0 to 1 ,total 20 numbers between 0 and 1


# In[ ]:


np.linspace(1,35,35)


# In[ ]:


np.eye(5,dtype=int)   #identity matrix of 5*5 dimension


# In[ ]:


np.random.rand(2,4)   #uniformly distributed random variable between 0 and 1 of order 2*4


# In[ ]:


np.random.randn(2,4)     #normally distributed random variable


# In[ ]:


np.random.randint(2,4)     #integer values


# In[ ]:


np.random.randint(0,10,15)      # 15 random variables between 0 and 10 .


# In[ ]:


sample = np.arange(2,20)
sample


# In[ ]:


sample.min()     #minimum value from array


# In[ ]:


sample.argmin()    #index of min value


# In[ ]:


sample.max()


# In[ ]:


sample.argmax()


# In[ ]:


sample.dtype   #data type


# In[ ]:


a=np.eye(5)
a


# In[ ]:


b=np.random.rand(3,4)
b


# In[ ]:


b.T     #transpose of matrix b


# In[ ]:


c=np.arange(10,30)    #total 20 elements
c


# In[ ]:


c=c.reshape(4,5)      #reshape the above array into 4*5 matrix
c


# In[ ]:


c=c.reshape(3,6)    #20 elements can not grouped into 3*6 matrix
c  


# In[ ]:


c[5] = 200
c


# In[ ]:


c[1:15]       #from index 1 to 14


# In[ ]:


subset  = c[0:6]  #from index 0 to 5
subset 


# In[ ]:


c[:] = 786    # All elements of array changed to 786
c


# # 2-D Matrix

# In[3]:


import numpy as np


# In[8]:


a = np.array([[23,45,65,4],[122,54,34,23],[21,53,69,76]])
a


# In[14]:


a[2,3]      #row  3(index 2), column 4(index 3)


# In[15]:


a[2][3]


# In[12]:


a[:,3]     #all row ,column 4


# In[13]:


a[2,2]


# In[16]:


a[1:3,2:4]


# In[18]:


a[0:,2:]


# In[20]:


a[2]


# In[22]:


a = np.arange(3,33)
a

