#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the essential libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[3]:


# load the dataset
df=pd.read_csv('Crop Production data.csv')
df


# In[4]:


# check the brief info of the dataset
df.head()


# In[5]:


# shape of the dataset
df.shape


# In[6]:


# index of the datset
df.index


# In[7]:


# columns of the dataset
df.columns


# In[8]:


# check the basic info about the dataset
df.info()


# In[12]:


# separete the list of features based on their data type
continuous_features=[]
categorical_features=[]
either_continuous_or_discrete_count=[]
for features in df.columns:
    if df[features].dtypes=='float64':
        continuous_features.append(features)
    elif df[features].dtypes=='object':
        categorical_features.append(features)
    else:
        either_continuous_or_discrete_count.append(features)
print('continuous features:',continuous_features)
print('categorical features:',categorical_features)
print('continuous or discrete count:',either_continuous_or_discrete_count)


# In[13]:


# check is there any null values
df.isnull().sum()


# In[14]:


# check the duplicated records
df.duplicated().sum()


# In[15]:


# It is a huse dataset so remove the null values
df.dropna(inplace=True)


# In[16]:


# after removing the null values
df.isnull().sum()


# In[17]:


# after removing the null values shape of the dataset
df.shape


# In[18]:


# value counts
df['State_Name'].value_counts() # 33 states


# In[19]:


# len of unique values
df['District_Name'].nunique()


# In[20]:


# crop year unique values
df['Crop_Year'].value_counts()


# In[21]:


# season value counts
df['Season'].value_counts()


# In[22]:


# unique values of crop
df['Crop'].unique()


# In[23]:


# after cleaning the dataset converted into new dataframe
df1=df.copy()


# In[24]:


# view the new dataframe
df1


# In[25]:


# check the null values of the new dataset
df1.isnull().sum()


# In[26]:


# check the duplicated values of the new dataframe
df1.duplicated().sum()


# In[27]:


# converted into new file
df1.to_csv('Crop_producion data.csv',index=False)


# In[ ]:




