#!/usr/bin/env python
# coding: utf-8

# # Part II: Feature Engineering
# Part I was tough wasn't it? Well done for surviving. 
# 
# Right now, we only have coordinates and time - not to mention our filesize is rather unwieldy. In this Part II, we will extract the most important pieces of information in the CSV we have and simplify the data that we'll be working with in subsequent Parts. 
# 
# In this notebook, you will do the following:
# 1. Load the CSV that you obtained from Part I (go back there and do it first if you haven't)
# 2. Convert the string representation of lists as actual lists
# 3. Divide the coordinates of taxis into different sectors
# 4. Engineer new features out of the time data
# 5. Drop unneeded columns
# 6. Export the engineered DataFrame
# 
# ### Step 1: Import the following libraries
# - pandas

# In[1]:


# # Step 1: Import pandas
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import ast
# from tqdm import tqdm
# sns.set()


# ### Step 2: Read the CSV from Part I
# We'll now read the CSV that we got from Part I as a DataFrame.

# In[2]:


# Step 2: Read the CSV
df_taxi = pd.read_csv('df_taxi.csv')
df_taxi.shape


# In[10]:


df_taxi.head()


# ### Step 3: Check the type of data in 'geometry.coordinates' column
# We'll need to be working with the 'geometry.coordinates' column so it's important to check the column data.
# 
# ![GeometryCoordinates.png](attachment:GeometryCoordinates.png)
# 
# This is what happens when you look at the first row's 'geometry.coordinates'.

# In[3]:


# Step 3: Take a look at the first row's geometry coordinates
df_taxi.geometry_coordinates[0]


# In[4]:


type(df_taxi.geometry_coordinates[0])


# ### Step 4: Convert string representation of list to an actual list (10 minutes)
# Wait a minute, something's wrong. If your eyes are sharp, you would have noticed that the lists are not really lists - they're strings! 
# 
# That's because when you read the CSV using pandas, pandas can't automatically parse the lists to become lists. 
# 
# You'll have to find a library and a function to do that, and <strong>apply</strong> this function to the string list in every single row. This process will take a bit of time (7-10 mins). 
# 
# ![StringToList.png](attachment:StringToList.png)
# 
# <strong>Hint: Google "convert string list into list python"</strong>
# 
# <strong>Hint 2: Google "use function on every row pandas"</strong>

# In[5]:


# Step 4: Turn the values in 'geometry.coordinates' column into actual lists
type(ast.literal_eval(df_taxi.geometry_coordinates[0]))


# In[6]:


get_ipython().run_cell_magic('time', '', "df_taxi['geometry_coordinates'] = df_taxi['geometry_coordinates'].apply(lambda x: ast.literal_eval(x))")


# ### Step 5: Sort the coordinates into nine sectors
# Now that we've successfully converted the string into lists, we can now loop through them.
# 
# Why, you ask? The reason for needing to loop through them is so that we can ascertain where the taxis are generally during a particular period of time. 
# 
# ![MapDivision.png](attachment:MapDivision.png)
# 
# We will be dividing Singapore into nine parts, based on its longtitude and latitude. We can slice more, but for the sake of simplicity we'll be using nine parts first. 
# 
# A few things to take note of:
# 1. Left limit - 103.6
# 2. Right limit - 104.1
# 3. Upper limit - 1.48
# 4. Lower limit - 1.15
# 
# Use the numbers at the edge of the map as boundaries when you sort the coordinates.
# 
# ![SortedDataFrameExpectation.png](attachment:SortedDataFrameExpectation.png)
# 
# Make sure your DataFrame has new columns that reflect the number of taxis available in different sectors throughout a day.
# 
# <strong>Hint: Use inequalities signs, e.g., >= and <, and the "and" operator to sort your coordinates</strong>

# In[7]:


# np.array(df_taxi['geometry_coordinates'][:10])[0]


# In[8]:


# Step 5: Sort the coordinates into the nine sectors
# np.where(np.array(df_taxi['geometry_coordinates'][:10]))


# In[22]:


# [Use this if you're really stuck] Step 5: Sort the coordinates into the nine sectors
# declare nine empty lists
sector_1 = []
sector_2 = []
sector_3 = []
sector_4 = []
sector_5 = []
sector_6 = []
sector_7 = []
sector_8 = []
sector_9 = []
# start a for loop to loop through the list of coordinates in geometry.coordinates column
for coord in tqdm(df_taxi.geometry_coordinates):
    # initialize nine variables with 0 to keep count of the available taxis
    num1,num2,num3,num4,num5,num6,num7,num8,num9=0,0,0,0,0,0,0,0,0
    # use another for loop to loop through the coordinate pairs in the list of coordinates
    for x,y in coord:
        # if the first half of the coordinates is less or equals than 103.77 and the second half is equals to or more than 1.37
        if x<=103.77:
            if y>=1.37: num1+=1
            elif y>=1.26: num4+=1
            else:num7+=1
            # increment the count for sector 1 by 1
        elif x<=109.93:
            if y>=1.37: num2+=1
            elif y>=1.26: num5+=1
            else:num8+=1
        else:
            if y>=1.37: num3+=1
            elif y>=1.26: num6+=1
            else:num9+=1
    sector_1.append(num1)
    sector_2.append(num2)
    sector_3.append(num3)
    sector_4.append(num4)
    sector_5.append(num5)
    sector_6.append(num6)
    sector_7.append(num7)
    sector_8.append(num8)
    sector_9.append(num9)
        
    # append the counts of the free taxis in each in the nine lists

# once all of the rows have been looped through, create new columns using the lists that you've create


# ### Step 6: Turn the strings in 'time' column into a DataTime object
# Next, we will get additional information from the "time", i.e. dayofweek, minute, hour. 
# 
# Currently, the values in the 'time' column are still strings so we will have to convert the values into to a DateTime object.
# 
# <strong>Hint: Google "convert DataFrame column type from string to datetime</strong>

# In[23]:


len(sector_1)


# In[24]:


df_taxi['sector_1'] = sector_1
df_taxi['sector_2'] = sector_2
df_taxi['sector_3'] = sector_3
df_taxi['sector_4'] = sector_4
df_taxi['sector_5'] = sector_5
df_taxi['sector_6'] = sector_6
df_taxi['sector_7'] = sector_7
df_taxi['sector_8'] = sector_8
df_taxi['sector_9'] = sector_9


# In[25]:


# Step 6: convert the strings in "time" column into DateTime object
df_taxi['time'] = pd.to_datetime(df_taxi.time)


# ### Step 7:Get 'dayofweek', 'minute', and 'hour from 'time' column
# Now that the column is now a proper DateTime object, we can now extract more information.
# 
# We will be creating new three new columns with:
# 1. day_of_week - day of the week, i.e. 0 (Monday) - 6 (Sunday)
# 2. minute - minute in day
# 3. hour - hour in day
# 
# ![DateTimeEngineering.png](attachment:DateTimeEngineering.png)
# 
# We can only extract data for the following columns because we've collected only one month's worth of data. Of course, you can always revisit this after you're done with Part IV.
# 
# <strong>Hint: Google "get column datetime attributes"</strong>

# In[26]:


# Step 7: Get dayofweek, minute, hour from 'time' column
df_taxi['dow'] = df_taxi.time.dt.dayofweek
df_taxi['hour'] = df_taxi.time.dt.hour
df_taxi['minute'] = df_taxi.time.dt.minute


# ### Step 8: Get the only parts you need
# As we have more and more columns, it's important to take the only ones you need. We can ditch the raw coordinates, and keep only the numbers of the taxis available in the nine sectors that we've defined. 
# 
# ![FinalOutputExpectations.png](attachment:FinalOutputExpectations.png)
# 
# You should only have the following at the end <strong>(in this order)</strong>:
# 1. the time at which the API was called
# 2. taxi count
# 3. day_of_week
# 4. minute
# 5. hour
# 6. taxis available for sectors 1-9
# 
# You should also have 8,641 rows and 14 columns after you're done. Depending on how you defined the inequality signs, you should have slightly different numbers but it generally should be of the same scale. 
# 
# <strong>Hint: Google "select multiple columns pandas" if you need help</strong>

# In[27]:


df_taxi.head()


# In[28]:


df_taxi.properties_api_info_status.unique()


# In[7]:


df_taxi_totals = pd.read_csv('df_taxi_totals.csv')
df_taxi_totals.head()


# In[14]:


df_taxi['time_2']= pd.to_datetime(df_taxi.time)
df_taxi['dow'] = pd.to_datetime(df_taxi.time).dt.dayofweek
df_taxi['hour'] = pd.to_datetime(df_taxi.time).dt.hour
df_taxi['minute'] = pd.to_datetime(df_taxi.time).dt.minute


# In[23]:


# Step 8: Select only the necessary columns for the DataFrame
cols = ['time','properties_taxi_count','dow','hour','minute','sector_1','sector_2','sector_3','sector_4','sector_5','sector_6','sector_7','sector_8','sector_9']
df_taxi_totals['dow'] = df_taxi.dow
df_taxi_totals['hour'] = df_taxi.hour
df_taxi_totals['minute'] = df_taxi.minute
df_taxi_totals['time'] = df_taxi.time
df_taxi_totals[cols].head()


# ## Step 9: Export your DataFrame as CSV
# Well done! You're finally done for this Part. It was tough but you did it. Time to export your DataFrame as a CSV for Part III. 

# In[24]:


# Step 9: Export the DataFrame from Step 8 as CSV
df_taxi_totals[cols].to_csv('df_taxi_totals_2.csv',index=False)


# In[ ]:




