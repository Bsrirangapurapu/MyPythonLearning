#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#introduction to list datatype:


# In[ ]:


#defination : A list is a collection of items declared in a particular order.
#classification: it is classified as mutable datatype
#how to declare a list ----->[]


# In[ ]:





# In[10]:


students = ['Bhargavi', 'Vijay', 'Prashanth']


# In[11]:


print(students)


# In[12]:


type(students)


# In[ ]:





# In[ ]:


#introdution to indexing : 0, 1, 2, 3, 4......


# In[ ]:


#how to access the individual elements in a list...!


# In[ ]:


#req : i want to access Bhargavi from list above


# In[14]:


print(students[0])


# In[15]:


print(students[2])


# In[ ]:





# In[ ]:


1. how to add new elements to the list
2. how to modify the elements in the list
3. how to delete elements in the list


# In[ ]:


#1. how to add new elements to the list


# In[16]:


print(students)


# In[ ]:


# Add kalyan to list above


# In[17]:


students.append('Kalyan')


# In[18]:


print(students)


# In[ ]:


# Add srujan to list above


# In[19]:


students.append('srujan')


# In[20]:


print(students)


# In[ ]:


# Add yeshwanth to 2nd index


# In[21]:


students.insert(2, 'Yeswanth')


# In[22]:


print(students)


# In[ ]:


## What is difference between append and insert methods in list data type


# In[ ]:





# In[ ]:


#2. how to modify the elements in the list


# In[23]:


print(students)


# In[ ]:


# modify Vijay name to VJ


# In[25]:


students[1] = 'VJ'


# In[26]:


print(students)


# In[ ]:





# In[ ]:


#3. how to delete elements in the list


# In[ ]:


# Delete yeswanth from list above


# In[32]:


del students[3]


# In[33]:


print(students)

