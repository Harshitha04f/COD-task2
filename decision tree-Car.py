#!/usr/bin/env python
# coding: utf-8

# ## Decision Tree

# ### Import all necessary libraries

# In[1]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np


# ### Import the data

# In[2]:


df=pd.read_csv(r"D:\pandu\machine learning\Car.csv")
print(df) 


# ### Seperate independent and dependent variables.

# In[22]:


X = df.iloc[:, 0:-1]
Y = df["class"]


# In[23]:


X


# #### Since the X training dataset has the categorical values, let us use OrdinalEncoder to tranform it an make the model understand

# In[24]:


enc = preprocessing.OrdinalEncoder()
X = enc.fit_transform(X)


# In[25]:


X


# In[7]:


Y


# ### Split the Data

# In[8]:


X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.40)


# X-Train: Training Questions
# Y-Train: Training Answers
# 
# X-Test: Test Questions
# Y-Test: Test Answers

# ### Call the Model

# In[9]:


dt_model = DecisionTreeClassifier(criterion="entropy")


# ### Train the Model

# In[10]:


dt_model.fit(X_train,Y_train)


# In[11]:


plot_tree(dt_model)


# ### Make the Predictions(Non-Probabilistic)

# In[12]:


Y_pred_class=dt_model.predict(X_test)


# In[13]:


Y_pred_class


# In[14]:


Y


# In[15]:


dt_model.score(X_test,Y_test)


# ### Make the Predictions(Probabilistic)

# In[16]:


Y_pred_prob=dt_model.predict_proba(X_test)


# In[17]:


Y_pred_prob


# ### Access the Model

# In[18]:


(Y_pred_class==Y_test).sum()/Y_test.shape[0]


# In[19]:


dt_model.score(X_test,Y_test)


# In[ ]:





# In[ ]:





# In[20]:


print(Y_pred_prob[0],Y_pred_class[0])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




