#!/usr/bin/env python
# coding: utf-8

# # Notebook with plotly

# In[57]:


import plotly.io as pio
import plotly.express as px
import plotly.offline as py
import pandas as pd
import plotly.graph_objects as go

pio.renderers.default='notebook'

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", size="sepal_length")
fig.show()


# In[58]:


df_summary = pd.read_csv(r'C:\Users\azuka\Documents\Shipper\Ad-hoc\df_summary_dev_220307.csv')


# In[59]:


fig = px.bar(df_summary.groupby(['shipmentstatus_name','logistic_name']).size().to_frame().reset_index().rename(columns={0:'total'}).sort_values('total'), x="total", y="logistic_name", color='shipmentstatus_name', orientation='h',
            #  hover_data=["tip", "size"],
             height=500,
             title='status paket'
             )
fig.show()


# In[60]:


for i,statusname in enumerate(sorted(df_summary.shipmentstatus_name.unique())[::-1]):
    df_logistic_status = df_summary[df_summary.shipmentstatus_name==statusname][['logistic_name','shipmentstatus_name']].groupby('logistic_name')['shipmentstatus_name'].size().to_frame().reset_index()
    if i == 0:
        fig = go.Figure(go.Bar(y=df_logistic_status.logistic_name, x=df_logistic_status.shipmentstatus_name, name=statusname, orientation='h', width=.8))
    else: fig.add_trace(go.Bar(y=df_logistic_status.logistic_name, x=df_logistic_status.shipmentstatus_name, name=statusname, orientation='h', width=.8))
fig.update_layout(barmode='stack',
                  yaxis={'categoryorder':'array',
                         'categoryarray': df_summary.logistic_name.value_counts(ascending=True).index},
                  xaxis={'title':'total'},
                  title='Status Paket',
                  
            )
fig.show()


# In[ ]:




