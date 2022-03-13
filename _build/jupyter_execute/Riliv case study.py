#!/usr/bin/env python
# coding: utf-8

# In[142]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
import seaborn as sns
import re
import pyodbc
import gspread
import matplotlib.dates as mdates
from datetime import datetime
import math
# import itertools
sns.set()


# In[31]:


custom_date_parser = lambda x: datetime.strptime(x, "%m-%d-%y")


# In[37]:


df_sales = pd.read_csv(r'C:\Users\azka\Downloads\SOAL TEST DATA ANALYST RILIV.csv', parse_dates=['Order Date','Ship Date'],dayfirst=False)
df_sales.head()


# In[38]:


df_sales = df_sales.iloc[:,:-1]
df_sales.head(10)


# In[39]:


df_sales.to_csv('df_sales.csv',index=False)


# In[40]:


df_sales.head()


# In[41]:


df_sales['Order Date'].max()


# In[47]:


df_sales.groupby('Country')['Order Date'].min().dt.year.plot.hist()


# In[49]:


df_sales.groupby('Item Type').size().plot.barh()


# In[51]:


df_sales['sales'] = df_sales['Units Sold']*df_sales['Unit Price']


# In[52]:


df_sales.resample('Q',on='Order Date')['sales'].sum()


# In[50]:


df_sales.columns


# In[53]:


df_sales['transaction_amount'] = df_sales['Units Sold']*(df_sales['Unit Price']-df_sales['Unit Cost'])


# In[54]:


df_sales.resample('Q',on='Order Date')['transaction_amount'].sum()


# In[55]:


df_sales['Item Type'].nunique()


# In[79]:


items_fnb = ['Baby Food','Beverages','Cereal','Snacks']
items_personal = ['Cosmetics','Clothes','Personal Care']
items_fresh = ['Fruits','Meat','Vegetables']
items_house = ['Household','Office Supplies']


# In[80]:


df_sales['item_group'] = ''
df_sales.loc[df_sales['Item Type'].isin(items_fnb),'item_group'] = 'FnB'
df_sales.loc[df_sales['Item Type'].isin(items_personal),'item_group'] = 'Personal'
df_sales.loc[df_sales['Item Type'].isin(items_fresh),'item_group'] = 'Fresh'
df_sales.loc[df_sales['Item Type'].isin(items_house),'item_group'] = 'Household'


# In[81]:


df_sales[(df_sales['Order Date'].dt.quarter==2)&(df_sales['Order Date'].dt.year==2017)&(df_sales.item_group=='FnB')].groupby(['item_group','Country']).transaction_amount.sum().sort_values(ascending=False).head(10)


# In[64]:


df_sales['Item Type'].unique()


# In[73]:


df_sales[(df_sales['Order Date'].dt.quarter==2)&(df_sales['Order Date'].dt.year==2017)].groupby(['Country']).sales.sum().sort_values(ascending=False).head(10)


# In[72]:


df_sales[(df_sales['Order Date'].dt.quarter==2)&(df_sales['Order Date'].dt.year==2017)]['Order Date'].describe()


# In[76]:


df_sales.groupby('Item Type').sales.sum().sort_values().plot.barh()


# In[82]:


df_sales.groupby('item_group').sales.sum().sort_values().plot.barh()


# In[88]:


df_sales.columns = [i.lower().replace(' ','_') for i in df_sales.columns]


# In[89]:


df_sales.columns


# In[90]:


df_sales['profit_margin'] = (df_sales.unit_price-df_sales.unit_cost)/df_sales.unit_price


# In[ ]:


df.groupby('Location').resample('H')['Event'].count()


# In[111]:


df_sales.groupby('item_type').resample('Q',on='order_date')['profit_margin'].mean().to_frame().reset_index()


# In[121]:


fig,ax=plt.subplots(figsize=(20,8))
sns.lineplot(data=df_sales.groupby('sales_channel').resample('M',on='order_date')['profit_margin'].mean().to_frame().reset_index(),x='order_date',y='profit_margin',hue='sales_channel',ax=ax)
# ax.set(ylim=(.25,.31))


# In[125]:


fig,ax=plt.subplots(figsize=(20,8))
sns.lineplot(data=df_sales.groupby('sales_channel').resample('M',on='order_date')['profit_margin'].std().to_frame().reset_index(),x='order_date',y='profit_margin',hue='sales_channel',ax=ax)
# ax.set(ylim=(.25,.31))


# In[124]:


df_sales.groupby('sales_channel').resample('M',on='order_date')['profit_margin'].std()


# In[128]:


df_sales[df_sales.item_type=='Cereal'].unit_price.nunique()


# In[139]:


df_sales.groupby('region').resample('Q',on='order_date')['region'].size().to_frame().rename(columns={'region':'total'}).reset_index()


# In[179]:


fig,ax=plt.subplots(figsize=(12,8))
sns.lineplot(ax=ax,data=df_sales.groupby('region').resample('Q',on='order_date')['region'].size().to_frame().rename(columns={'region':'total'}).reset_index(),x='order_date',y='total',hue='region')


# In[194]:


df_sales[df_sales.item_type=='Cereal'].set_index('order_date').groupby('region').resample('Q')['region'].size().to_frame().rename(columns={'region':'total'}).reset_index()


# In[187]:


sns.relplot(data=df_sales.set_index('order_date').groupby(['region','item_type']).resample('Q')['region'].size().to_frame().rename(columns={'region':'total'}).reset_index(), x='order_date',y='total',hue='region',col='item_type',kind='line',col_wrap=3)


# In[195]:


df_sales.resample('Q',on='order_date').sales.sum()


# In[206]:


df_sales[df_sales.order_date.dt.date>=pd.to_datetime('2013-07-01')].resample('W',on='order_date').sales.cumsum()


# In[198]:


df_sales.resample('Q',on='order_date').country.count()


# In[199]:


df_sales.order_date.max()


# In[200]:


df_sales.ship_date.max()


# In[202]:


df_sales.groupby('item_type')['order_date'].min()


# In[214]:


df_sales[(df_sales.order_date.dt.quarter==2)&(df_sales.order_date.dt.year==2017)].groupby('country').sales.sum().sort_values(ascending=False).head(10)


# In[216]:


df_sales[(df_sales.order_date.dt.quarter==1)&(df_sales.order_date.dt.year==2017)&(df_sales.country.isin(df_sales[(df_sales.order_date.dt.quarter==2)&(df_sales.order_date.dt.year==2017)].groupby('country').sales.sum().sort_values(ascending=False).head(10).index))].groupby('country').sales.sum()


# In[212]:


df_sales[(df_sales.order_date.dt.quarter==2)&(df_sales.order_date.dt.year==2017)&(df_sales.sales_channel=='Offline')].groupby('country').sales.sum().sort_values(ascending=False).head(10)


# In[218]:


df_sales[(df_sales.order_date.dt.quarter==2)&(df_sales.order_date.dt.year==2017)].groupby('item_type').sales.sum().sort_values(ascending=False).head(5).plot.barh()


# In[ ]:




