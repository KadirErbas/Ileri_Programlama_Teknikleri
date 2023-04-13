#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fonk(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    return fonk(a,b-1) * a   
    


# In[3]:


fonk(4,3)


# In[ ]:




