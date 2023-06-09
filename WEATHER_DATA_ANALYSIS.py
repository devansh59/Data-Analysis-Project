#!/usr/bin/env python
# coding: utf-8

# # WEATHER_DATA_ANALYSIS
# 

#  
#  
#  

# In[1]:


#importing different libraries
import pandas as pd


# In[2]:


#import the datase
data = pd.read_csv('weather_data.csv')


# In[3]:


data


# 
# 

# # Exploring the data

# **.head()**     
# To show the first N rows in data(by default N=5)

# In[4]:


data.head()


#    
#    

# **.shape**    
# To show the total no. of row and cols in dataset

# In[5]:


data.shape


#     
#        
#        

# **.index**   
# This attribute provides the index of dataframe

# In[6]:


data.index


#    
#    

# **.columns**   
# It's shows the name of each column

# In[8]:


data.columns


#   
#      

# **.dtypes**   
# It show the data type of each column

# In[10]:


data.dtypes


#    
#    

# **.unique()**   
# In a column ,it show all unique values,it can apply on single column only not on entire dataframe

# In[11]:


data['Weather'].unique()


#    
#         
#         

# **.nunique()**   
# it show total no. of unique values in each column.   
# it can be applied on single column as well as entire dataframe

# In[12]:


data.nunique() #entire dataframe


# In[13]:


data['Weather'].nunique()   #weather column


#   
#     
#     

# **.count()**   
# it show the total no. of non-null values in each columns  
# it can be applied on single column as well as entire dataframe

# In[15]:


data.count()


#  
#   
#     
#      
#       

# **.value_counts**     
# In a column it shows all the unique value with their count.   
# applied on single column only

# In[20]:


data['Weather'].value_counts()


#    
#      
#      

# **.info**  
# Provides basic information about dataframe

# In[22]:


data.info()


#  
#  
#  

#   
#   
#   

# # Q-1 Find all the unique  'Wind speed' value in data

# In[23]:


data.head()


# In[24]:


data['Wind Speed_km/h'].unique()


#   

# # Q-2 Find the number  of times when the weather is exactly clear

# In[25]:


data.head(2)


# In[27]:


#using value_counts
data['Weather'].value_counts()
#clear->1326


# In[30]:


#usisng filtering 
data[data.Weather == 'Clear']
#it will shows all the record with weather will be clear only


# In[31]:


#using groupby()
data.groupby('Weather').get_group('Clear')


#  
#   
#   

# # Q-3 Find the number of times when the wind speed was exactly 4km/hr
# 

# In[32]:


data.head(2)


# In[34]:


data[data['Wind Speed_km/h']==4]


#  
#   
#    

# # Q-4 Find out the all null values in data

# In[40]:


data.isnull().sum()


# In[41]:


data.notnull().sum()


#  

# # Q-5 Rename the column name 'Weather' to 'Weather_condition'

# In[43]:


data.rename(columns={'Weather':'Weather_condition'})


#   
#   

# # Q-6 What is the mean 'visibility'?

# In[45]:


data.head(2)


# In[48]:


data['Visibility_km'].mean()


# In[49]:


data.Visibility_km.mean()


#   
#   

# # Q-7 What is the standard deviation of 'pressure' in this data?

# In[50]:


data.Press_kPa.std()


# 
# 
# 

# # Q-8 What is the variance of 'Relative humidity' in this data?
# 

# In[52]:


data['Rel Hum_%'].var() 
#there is a space b/w two letters so that we used []


#   
#   

# # Q-9 Find all instances when 'Snow' was recorderd

# In[53]:


#value_count()
data.head(2)


# In[54]:


data['Weather'].value_counts()
#snow->390 times


# In[55]:


#filtering
data[data.Weather=='Snow']


# In[59]:


#str.contains
data[data['Weather'].str.contains('Snow')]


#   
#   

# # Q-10 Find all instances when 'Wind Speed' is above 24 and 'visibility' is 25

# In[60]:


data.head(2)


# In[62]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


#   
#     
#      
#      

# # Q-11 What is the mean value of each column against each 'Weather'?

# In[4]:


data.head(2)


# In[5]:


data.groupby('Weather').mean()


#   
#   

# # Q-12 What is the max and min value of each column against each 'Weather'?

# In[6]:


data.groupby('Weather').max()


# In[7]:


data.groupby('Weather').min()


#     
#      
#       
#        

# # Q-13 Show all the records where weather condition is 'Fog'

# In[8]:


data[data.Weather=='Fog']


#     
#     

# # Q-14 Find all instances when weather is clear or visibility is above 40 

# In[11]:


data[(data.Weather=='Clear') | (data.Visibility_km>40)]


#  
#   
#   

# # Q-15 Find All instances when 
# **A) Weather is clear and Relative humidity is grater than 50      
# or    
# B) Visibility is above 40**

# In[13]:


data[(data.Weather=='Clear') & (data['Rel Hum_%']>50) | (data.Visibility_km>40)]


# In[ ]:




