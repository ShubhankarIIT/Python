#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Hello World")


# In[ ]:


print("hi this is Shubhankar")


# In[ ]:


2+3-5


# ### Python

# ### Python

# ## Python

# # Shubhankar

# In[ ]:


get_ipython().system('python --version')


# In[ ]:


# Addition
a=4
b=5
sum = a+b
sum


# In[ ]:


4+5


# In[ ]:


a=4
b=5
a+b


# In[ ]:


a,b,c=23,54,"Shubhankar"
c


# ### Variables are containers for storing values
# ### Python has no command for declaring the variables
# ### When you assign a value , a variable is created

# In[ ]:


### Declaring a  Variable
x=5


# In[ ]:


x


# In[ ]:


Name = Shubhankar
Name 


# In[ ]:


Name = "Shubhankar"
Name


# In[ ]:


Name_nick = "Shubhankar"
Name_nick


# In[ ]:


1Name = "Shubham" ##var should not start with a number


# In[ ]:


N1 = "shubham"
N1


# In[ ]:


N@ame = "Shubham"
N@ame


# In[ ]:


age = 25
age


# In[ ]:


Age


# In[ ]:


AGE


# In[ ]:


age


# # Rules for declaring a Variable
# ### A variable name must start with a letter or underscore character.
# ### A variable name cann't start with a number.
# ### A variable name can only contain alpha-numeric characters and underscore(A-Z,a-z,_)
# ### Variable names are case sensitive

# # DATA Types

# In[ ]:


a = "Python"
type(a)


# In[ ]:


b=4.5
type(b)


# In[ ]:


c=True
type(c)


# In[ ]:


x="True"
type(x)


# In[ ]:


d=3+2j
type(d)


# In[ ]:


a=2,b=3.2 add and store in the sum
subtract and store in the sub
print both outputs


# In[ ]:


a=2
b=3.2
sum=a+b
sub = a-b
sum,sub,type(sum),type(sub)


# # DATA Structures

# ## List
# ### 1. Allows heterogenous

# In[2]:


sample_list=[12,43,56,"hi",1+2j,6.7]
sample_list


# In[ ]:


type(sample_list)


# In[3]:


sample_list[0]


# In[4]:


sample_list[20]


# In[ ]:


sample_list[2]=3.5
sample_list


# In[ ]:


sample_list.reverse()


# In[ ]:


sample_list


# In[5]:


s=[21,34,5,76,8,0]
s.sort()
s


# In[ ]:


adi = ["apple","guava","banana","cherry"]
print("guava" in adi)


# In[ ]:


print("pineapple" in adi)


# In[6]:


list = [2 , 3.4,3,23 , 54 ,34]
list.sort()
list


# In[7]:


len(list) #length of the list


# In[8]:


max(list),min(list)   #max and min values in the list


# In[9]:


list.append(786)   #add a single element at the end of the list
list


# In[10]:


new = list.copy()  #copy of the list
new


# In[ ]:


list.insert(3,26) #Insert a new element at the specified index
list


# In[11]:


list.reverse()   #Reverse of list
list


# In[12]:


list.sort()    #sorting of list
list


# In[13]:


a=list.index(23)  #Index Position of an element
a


# In[15]:


list.remove(786)  #delete an element from the list
list


# In[16]:


list.pop(4)       #deletes an element from the list based on  the index given
list              #deletes an element from 4th index of list


# In[17]:


list.clear()     #remove all element from the list
list


# In[ ]:




