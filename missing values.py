#!/usr/bin/env python
# coding: utf-8

# <h1 style='color:#9D3582' > Done by Fatimah AlYami</h1>

# In[524]:


#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[525]:


df=pd.read_csv("burritos.csv")


# In[526]:


df.info()


# In[527]:


#The 5 First Rows
df.head()


# In[528]:


# What Data type is NaN 
# row 1 and column 57
type(df.iloc[1,57])


# <h1 style='color:#0D12D5' > How Many Missing Values in each Column  ?</h1>

# In[529]:


# Missing values in each column. 
df.isnull().sum()


# <h1 style='color:#00741B' >  Total Amount of Missing Values   </h1>

# In[530]:


# Bar plot to visualize the total NaN values in each column
plt.figure(figsize=(14,14), dpi= 150)
df.isnull().sum().plot(kind="barh", title = "Total Number of NaN values in each column")


# <h1 style="color:red">Mean </h1>
# 
# 
# ##### Imputing Mean in column Yelp

# In[531]:


df['Yelp'].dtype


# In[532]:


#Histogram with 5 bins to display data distribution
df['Yelp'].plot(kind="hist",bins=5,title="Before handling the missing values of column (Yelp)",color='r')
plt.xlabel("Yelp Values")


# In[533]:


# Variance Calculation before handling NaN values
df['Yelp'].var()


# In[534]:


#mean
yelp_mean=round(df['Yelp'].mean())
yelp_mean


# In[535]:


#Replace the NaN values with the mean
df['Yelp']=df['Yelp'].fillna(yelp_mean)
df['Yelp'].isnull().sum()


# ###### Has The Data Changed ?
# Yes, it has. 

# In[536]:


df['Yelp'].plot(kind="hist",bins=5,title="After handling the missing values of column (Yelp)",color="r")
plt.xlabel("Yelp Values")


# In[537]:


# Variance Calculation after handling NaN values
df['Yelp'].var()


# <h1 style="color:green"> Median </h1>
# 
# 
# ##### Imputing Median in column Mass (g)

# In[538]:


df['Mass (g)'].dtype


# In[539]:


#Histogram with 10 bins to display data distribution
df['Mass (g)'].plot(kind="hist",bins=10,title="Before Handling the Missing Values of column (Mass (g))",color="g")
plt.xlabel("Mass (g) Values")


# In[540]:


# Variance Calculation before handling NaN values
df['Mass (g)'].var()


# In[541]:


#Median
mass_median=round(df['Mass (g)'].median())
mass_median


# In[542]:


#Replace the missing values with the median

df['Mass (g)']=df['Mass (g)'].fillna(mass_median)
df['Mass (g)'].isnull().sum()

#df['Mass (g)']=df['Mass (g)'].replace(np.NaN, mass_median)


# ###### Has The Data Changed ?
# Yes, it has. 

# In[543]:


df['Mass (g)'].plot(kind="hist",bins=10,title="After Handling the Missing Values of column (Mass (g))",color='g')
plt.xlabel("Mass (g) Values")


# In[544]:


# Variance Calculation after handling NaN values
df['Mass (g)'].var()


# <h1 style="color:Blue">Mode </h1>
# 
# 
# ##### Imputing Mode in column Density (g/mL)

# In[545]:


df['Density (g/mL)'].dtype


# In[546]:


# Variance Calculation before handling NaN values
df['Density (g/mL)'].var()


# In[547]:


#Histogram with 10 bins to display data distribution
df['Density (g/mL)'].plot(kind="hist",bins=10,title="Before Handling the Missing Values of column (Density (g/mL))",color="b")
plt.xlabel("Density (g/mL) Values")


# In[548]:


Density_mode=df['Density (g/mL)'].mode()[0]
Density_mode


# In[549]:


#Replace the missing values with the mode

df['Density (g/mL)']=df['Density (g/mL)'].replace(np.NaN,Density_mode)
df["Density (g/mL)"].isnull().sum()


# ###### Has The Data Changed ?
# Yes, it has. 

# In[550]:


df['Density (g/mL)'].plot(kind="hist",bins=10,title="After Handling the Missing Values of column (Density (g/mL))",color='b')
plt.xlabel("Density (g/mL) Values")


# In[551]:


# Variance Calculation after handling NaN values
df['Density (g/mL)'].var()


# <h1 style="color:darkorange">Replacing with Own Value </h1>
# 
# 
# ##### Imputing my own value in column Google

# In[552]:


df['Google'].dtype


# In[553]:


#Histogram with 10 bins to display data distribution
df["Google"].plot(kind="hist", bins=20, title="Histogram of Column Google without Handling NaN Values",color="orange");
plt.xlabel("Google Values")


# In[554]:


google_own=-1
google_own


# In[555]:


df["Google"]=df["Google"].fillna(google_own)


# In[556]:


df["Google"].plot(kind="hist", bins=20, title="Histogram of Column Google After Handling NaN Values",color="orange");
plt.xlabel("Google Values")


# <h1 style="color:#4FBA56">Forward Filling Column  </h1>

# In[557]:


#Column Fillings
df['Fillings']


# In[558]:


df['Fillings'].fillna(method="ffill")


# <h1 style="color:#769CD2">Backward Filling Column  </h1>

# In[559]:


# Column Volume
df['Volume']


# In[271]:


#Backword filling
df['Volume'].fillna(method="bfill")

