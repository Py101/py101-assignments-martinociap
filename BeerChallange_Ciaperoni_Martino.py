
# coding: utf-8

# In[9]:

from functools import reduce
def fact(n):
    lst = [i for i in range(i,n+1)]
    a = reduce(lambda x,y : x*y, lst)
    return(a)


# In[10]:

fact(4)


# In[ ]:



