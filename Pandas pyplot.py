#!/usr/bin/env python
# coding: utf-8

# In[23]:


#import the necessary libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[24]:


df = pd.read_csv('D:/Data analysis/practice/cars.csv')
df


# In[25]:


df.columns


# In[26]:


#Analytical summary of the dataset
df.describe(include='all')


# In[27]:


#histogram graph
df.hist(figsize=(20,30))


# In[28]:


#Relationship between categorical and continuous variable

#sns.boxplot(x="Dimensions.Width", y="Engine Information.Driveline", data = df)
sns.boxplot(x="Engine Information.Driveline", y="Dimensions.Width", data = df)


# In[29]:


sns.pairplot(df)


# In[30]:


df.columns


# In[31]:


#Drop irrelevant columns
df = df.drop(['Engine Information.Hybrid', 'Engine Information.Transmission', 'Fuel Information.City mpg', 'Fuel Information.Highway mpg', 'Engine Information.Engine Statistics.Horsepower', 'Engine Information.Engine Statistics.Torque'], axis=1)
df.head(5)


# In[33]:


df = df.drop(['Engine Information.Number of Forward Gears'], axis=1)
df.head(5)


# In[36]:


#rename the columns
df = df.rename(columns={"Dimensions.Height":"Car Height", "Dimensions.Length":"Car Length", "Dimensions.Width":"Car Width"})
df.head(5)


# In[37]:


df = df.rename(columns={"Identification.Classification":"Transmission"})
df.head(5)


# In[38]:


# show total number of rows and columns
df.shape


# In[40]:


#show rows that containing duplicate data
duplicate_rows_car = df[df.duplicated()]
print("Number of duplicate rows: ", duplicate_rows_car.shape)


# In[41]:


#Count the rows before removing the data
df.count()


# In[42]:


#Remove the duplicate data
df = df.drop_duplicates()
df.head(5)


# In[45]:


df.count()


# In[46]:


#Find the null values
print(df.isnull().sum())


# In[47]:


#Drop the missing values
df = df.dropna()
df.count()


# In[51]:


df = df.rename(columns={"Identification.Make":"Make"})
df.head(5)


# In[48]:


#Finding the outliers
sns.boxplot(x=df['Car Height'])


# In[54]:


# Plotting a Histogram for number of cars per brand
df.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("Number of cars by make")
plt.ylabel("Number of cars")
plt.xlabel("Make");


# In[55]:


#Find the relations between the variables
    #closer to 1 is higher the correlations
plt.figure(figsize=(20,10))
c = df.corr()
sns.heatmap(c, cmap="BrBG", annot=True)
c


# In[ ]:




