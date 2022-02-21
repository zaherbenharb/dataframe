#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np


# In[32]:


exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


# In[33]:


df = pd.DataFrame(exam_data)


# In[ ]:





# In[34]:


df.head(3)


# In[35]:


df[['name','score']]


# In[37]:


df.loc[1]=['Suresh',15.5,1,'yes']


# In[40]:


df.head(15)


# In[41]:


df.drop('attempts', axis=1)


# In[42]:



    conditionlist = [
    (df['score'] >10) ,
    (df['score'] <=10)]
choicelist = ['1', '0']
df['Success'] = np.select(conditionlist, choicelist, default='Not Specified')

    


# In[43]:


df.head()


# In[44]:


My_data=df.to_csv()


# In[ ]:




