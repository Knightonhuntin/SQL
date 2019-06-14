#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sqlalchemy import *
import numpy as np
import pandas as pd
import os
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1500  # Set Duration To 1000 ms == 1 second
directory = os.getcwd()
directory


# In[2]:


import time, sys
from IPython.display import clear_output
def update_progress(progress):
    bar_length = 20
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
    if progress < 0:
        progress = 0
    if progress >= 1:
        progress = 1
    block = int(round(bar_length * progress))
    clear_output(wait = True)
    text = "Progress: [{0}] {1:.1f}%".format( "#" * block + "-" * (bar_length - block), progress * 100)
    print(text)


# In[3]:


engine = create_engine('mysql://root:Hurricane54!@localhost:3306/ceesmart')


# In[4]:


connection = engine.connect()


# In[8]:


num_files = 0
for filename in os.listdir(directory):
    if filename.endswith(".csv"): 
        num_files +=1
num_files


# In[9]:


i = 1
for filename in os.listdir(directory):
    if filename.endswith(".csv"): 
        with open(filename, 'r') as file:
            data = pd.read_csv(file)
            file2 = str(file)
            data = data[pd.notnull(data['Time'])]
            data = data.drop_duplicates()
        data.to_sql("hourlydata", con=engine, index=True, index_label='id', if_exists='append')
        print(i)
        i = i + 1
        update_progress(i/num_files)

winsound.Beep(frequency, duration)    


# In[14]:


engine = create_engine('mysql://root:Hurricane54!@192.168.100.59:3306/ceesmart')


# In[15]:


connection = engine.connect()


# In[41]:


data = pd.read_csv('SoCal_Rainbow Station_Run 2_22-05-2019 672850439 Hourly.csv')
data.iloc[400,1]
data = data[pd.notnull(data['Time'])]

data = data.drop_duplicates()
data

