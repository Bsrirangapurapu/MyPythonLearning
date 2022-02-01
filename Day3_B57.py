#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Continuation with strings:


# In[2]:


fullname = 'bhargavi srirangapurapu'
print(fullname)


# In[ ]:





# In[ ]:


#String methods:


# In[3]:


print(fullname.title())


# In[ ]:





# In[ ]:


#full name in capital letters


# In[5]:


print(fullname.upper())


# In[ ]:





# In[ ]:


# full name in lower case letters


# In[6]:


print(fullname.lower())


# In[ ]:





# In[7]:


type(fullname)


# In[ ]:


# type method will be helping us to validate and confirm the datatype


# In[ ]:





# In[ ]:


# introduction to f strings


# In[18]:


first_name = 'robert'
last_name = 'mitchell'


# In[ ]:





# In[ ]:


# fullname??


# In[ ]:


#general syntax


# In[ ]:


#f" custom words {placeholder1}, {placeholder2}.... {placeholdern}


# In[ ]:





# In[22]:


full_name = f"{first_name} {last_name}"
print(full_name)


# In[ ]:





# In[23]:


message = f"Keep up the good work, {full_name.title()}"
print(message)


# 

# In[ ]:


#Adding white spaces to strings:


# In[11]:


print('fav_prog_lang:pythonc++javaswiftcobalpascal')


# In[12]:


print('fav_prog_lang:\npython\nc++\njava\nswift\ncobal\npascal') #\n --> new line delimiter


# In[ ]:





# In[17]:


print('fav_prog_lang:\n\tpython\n\tc++\n\tjava\n\tswift\n\tcobal\n\tpascal') #\t --> tab delimiter


# In[ ]:


#removing white spaces from strings


# In[24]:


name = 'manvitha'
print(name)


# In[25]:


name2 = ' manvitha'
print(name2)


# In[26]:


name3 = 'manvitha  '
print(name3)


# In[27]:


name3.strip() # strip is the method used to remove white spaces


# In[ ]:




