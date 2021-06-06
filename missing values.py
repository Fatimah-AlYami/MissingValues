#!/usr/bin/env python
# coding: utf-8

# <h1 style='color:#9D3582' > <u> <b>Done by Fatimah AlYami </h1>

# In[488]:


#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[489]:


df=pd.read_csv("burritos.csv")


# In[490]:


df.info()


# In[491]:


#The 5 First Rows
df.head()


# In[492]:


# What Data type is NaN 
# row 1 and column 57
type(df.iloc[1,57])


# <h1 style='color:#0D12D5' > How Many Missing Values in each Column  ?</h1>

# In[493]:


# Missing values in each column. 
df.isnull().sum()


# <h1 style='color:#00741B' >  Total Amount of Missing Values   </h1>

# In[494]:


# Bar plot to visualize the total NaN values in each column
plt.figure(figsize=(14,14), dpi= 150)
df.isnull().sum().plot(kind="barh", title = "Total Number of NaN values in each column")


# <h1 style="color:red"><u> Mean</u> </h1>
# 
# 
# ##### Imputing Mean in column Yelp

# In[495]:


df['Yelp'].dtype


# In[496]:


#Histogram with 5 bins to display data distribution
df['Yelp'].plot(kind="hist",bins=5,title="Before handling the missing values of column (Yelp)",color='r')
plt.xlabel("Yelp Values")


# In[497]:


# Variance Calculation before handling NaN values
df['Yelp'].var()


# In[498]:


#mean
yelp_mean=round(df['Yelp'].mean())
yelp_mean


# In[499]:


#Replace the NaN values with the mean
df['Yelp']=df['Yelp'].fillna(yelp_mean)
df['Yelp'].isnull().sum()


# ###### Has The Data Changed ?
# Yes, it has. 

# In[500]:


df['Yelp'].plot(kind="hist",bins=5,title="After handling the missing values of column (Yelp)",color="r")
plt.xlabel("Yelp Values")


# In[501]:


# Variance Calculation after handling NaN values
df['Yelp'].var()


# <h1 style="color:green"><u> Median </h1>
# 
# 
# ##### Imputing Median in column Mass (g)

# In[502]:


df['Mass (g)'].dtype


# In[503]:


#Histogram with 10 bins to display data distribution
df['Mass (g)'].plot(kind="hist",bins=10,title="Before Handling the Missing Values of column (Mass (g))",color="g")
plt.xlabel("Mass (g) Values")


# In[504]:


# Variance Calculation before handling NaN values
df['Mass (g)'].var()


# In[505]:


#Median
mass_median=round(df['Mass (g)'].median())
mass_median


# In[506]:


#Replace the missing values with the median

df['Mass (g)']=df['Mass (g)'].fillna(mass_median)
df['Mass (g)'].isnull().sum()

#df['Mass (g)']=df['Mass (g)'].replace(np.NaN, mass_median)


# ###### Has The Data Changed ?
# Yes, it has. 

# In[507]:


df['Mass (g)'].plot(kind="hist",bins=10,title="After Handling the Missing Values of column (Mass (g))",color='g')
plt.xlabel("Mass (g) Values")


# In[508]:


# Variance Calculation after handling NaN values
df['Mass (g)'].var()


# <h1 style="color:Blue"><u> Mode </h1>
# 
# 
# ##### Imputing Mode in column Density (g/mL)

# In[509]:


df['Density (g/mL)'].dtype


# In[510]:


# Variance Calculation before handling NaN values
df['Density (g/mL)'].var()


# In[511]:


#Histogram with 10 bins to display data distribution
df['Density (g/mL)'].plot(kind="hist",bins=10,title="Before Handling the Missing Values of column (Density (g/mL))",color="b")
plt.xlabel("Density (g/mL) Values")


# In[512]:


Density_mode=df['Density (g/mL)'].mode()[0]
Density_mode


# In[513]:


#Replace the missing values with the mode

df['Density (g/mL)']=df['Density (g/mL)'].replace(np.NaN,Density_mode)
df["Density (g/mL)"].isnull().sum()


# ###### Has The Data Changed ?
# Yes, it has. 

# In[514]:


df['Density (g/mL)'].plot(kind="hist",bins=10,title="After Handling the Missing Values of column (Density (g/mL))",color='b')
plt.xlabel("Density (g/mL) Values")


# In[515]:


# Variance Calculation after handling NaN values
df['Density (g/mL)'].var()


# <h1 style="color:darkorange"><u> Replacing with Own Value </h1>
# 
# 
# ##### Imputing my own value in column Google

# In[516]:


df['Google'].dtype


# In[517]:


#Histogram with 10 bins to display data distribution
df["Google"].plot(kind="hist", bins=20, title="Histogram of Column Google without Handling NaN Values",color="orange");
plt.xlabel("Google Values")


# In[518]:


google_own=-1
google_own


# In[519]:


df["Google"]=df["Google"].fillna(google_own)


# In[520]:


df["Google"].plot(kind="hist", bins=20, title="Histogram of Column Google After Handling NaN Values",color="orange");
plt.xlabel("Google Values")


# <h1 style="color:#4FBA56">Forward Filling Column  </h1>

# In[521]:


#Column Fillings
df['Fillings']


# In[522]:


df['Fillings'].fillna(method="ffill")


# <h1 style="color:#769CD2">Backward Filling Column  </h1>

# In[523]:


# Column Volume
df['Volume']


# In[271]:


#Backword filling
df['Volume'].fillna(method="bfill")

