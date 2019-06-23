
# coding: utf-8

# In[3]:

import pandas as pd
import pyodbc 
from datetime import date

SQLSERVER = 'GB3SIS10NOTVI\SQLEXPRESS'
SQLDB = 'InterviewProject_IgnacioJavierVenturini' 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=' + SQLSERVER + ';'
                      'Database=' + SQLDB + ';'
                      'Trusted_Connection=yes;')

sqlcmd = "Select * From [dbo].Hours"
fv_hours = pd.read_sql(sqlcmd,conn)
fv_hours.to_excel('fv_hours.xlsx', index=False)

del fv_hours

sqlcmd = "Select * From [dbo].Skills"
fv_skills = pd.read_sql(sqlcmd,conn)
fv_skills.to_excel('fv_skills.xlsx', index=False)

del fv_skills

sqlcmd = "Select * From [dbo].Employee_Roster_Data"
fv_erd = pd.read_sql(sqlcmd,conn)
fv_erd.to_excel('fv_erd.xlsx', index=False)

del fv_erd

