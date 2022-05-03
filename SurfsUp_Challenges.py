#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import numpy as np
import pandas as pd

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# In[2]:


# create engine to hawaii.sqlite
engine = create_engine("sqlite:///hawaii.sqlite")


# In[3]:


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# In[4]:


# We can view all of the classes that automap found
Base.classes.keys()


# In[5]:


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# In[6]:


# Create our session (link) from Python to the DB
session = Session(engine)


# ## D1: Determine the Summary Statistics for June

# In[7]:


# 1. Import the sqlalchemy extract function.
from sqlalchemy import extract

# 2. Write a query that filters the Measurement table to retrieve the temperatures for the month of June. 
june_temps = session.query(Measurement).filter(extract('month', Measurement.date) == 6)


# In[8]:


#  3. Convert the June temperatures to a list.
june_temps_list = [temp.tobs for temp in june_temps]


# In[9]:


# 4. Create a DataFrame from the list of temperatures for the month of June. 
june_df = pd.DataFrame(june_temps_list,columns=['June Temps'])
june_df.head()


# In[10]:


# 5. Calculate and print out the summary statistics for the June temperature DataFrame.
june_df.describe()


# ## D2: Determine the Summary Statistics for December

# In[11]:


# 6. Write a query that filters the Measurement table to retrieve the temperatures for the month of December.
dec_temps = session.query(Measurement).filter(extract('month', Measurement.date) == 12)


# In[12]:


# 7. Convert the December temperatures to a list.
dec_temps_list = [temp.tobs for temp in dec_temps]


# In[13]:


# 8. Create a DataFrame from the list of temperatures for the month of December. 
dec_df = pd.DataFrame(dec_temps_list,columns=['December Temps'])
dec_df.head()


# In[14]:


# 9. Calculate and print out the summary statistics for the Decemeber temperature DataFrame.
dec_df.describe()


# In[ ]:




