
# coding: utf-8

# In[1]:

import pandas as pd
import pyodbc 
from datetime import date

SQLSERVER = 'GB3SIS10NOTVI\SQLEXPRESS'
SQLDB = 'InterviewProject_IgnacioJavierVenturini' 

ds_hours = pd.read_excel('..\datasources\hours.xlsx','Sheet1')
ds_skills = pd.read_excel('..\datasources\skills.xlsx','Sheet1')
ds_Email_Data = pd.read_csv('..\datasources\Email_Data.txt',delimiter="\t")


# In[2]:

#remove special characters
for col in ds_hours.columns:
        if (ds_hours[col].dtype == 'object' ):
            ds_hours[col] = ds_hours[col].str.replace("[^ \t\n\r\f\va-zA-Z0-9_]", '')


# In[3]:

#remove Department and Gender columns, as those are the same in Employee_Roster_Data
ds_skills = ds_skills.drop(columns=['Department','Gender'])
#remove special characters
for col in ds_skills.columns:
        if (ds_skills[col].dtype == 'object' ):
            ds_skills[col] = ds_skills[col].str.replace("[^ \t\n\r\f\va-zA-Z0-9_]",'')


# In[4]:

#remove special characters
for col in ds_Email_Data.columns:
        if (ds_Email_Data[col].dtype == 'object' ):
            ds_Email_Data[col] = ds_Email_Data[col].str.replace("[^ \t\n\r\f\va-zA-Z0-9_]",'')


# In[5]:

#connect to sql to insert data
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=' + SQLSERVER + ';'
                      'Database=' + SQLDB + ';'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
#insert hours data source
sqlcmd = "INSERT INTO [Hours]([Date],[UserId],[AdminHrs1],[AdminHrs2],[AdminHrs3],[ClientHrs1],[ClientHrs2],[ClientHrs3],[TargetClientHrs]) values ('{}',{},{},{},{},{},{},{},{})"
for index,row in ds_hours.iterrows():
    cursor.execute(sqlcmd.format(row['Date'],row['UserId'],row['AdminHrs1'],row['AdminHrs2'],row['AdminHrs3'],row['ClientHrs1'],row['ClientHrs2'],row['ClientHrs3'],row['TargetClientHrs']))
    conn.commit()
#insert skills data source
sqlcmd = "INSERT INTO [Skills]([UserId],[Fullname],[Attribute Group],[Attribute Sub-Group],[Attribute Type],[Attribute Name],[Attribute Level],[Attribute Verified]) values ({},'{}','{}','{}','{}','{}',{},{})"
for index,row in ds_skills.iterrows():
    cursor.execute(sqlcmd.format(row['UserId'],row['Fullname'],row['Attribute Group'],row['Attribute Sub-Group'],row['Attribute Type'],row['Attribute Name'],row['Attribute Level'],row['Attribute Verified']*1))
    conn.commit()
#insert Email_Data data source
sqlcmd = "INSERT INTO [Email_Data]([from_ID],[to_ID]) values ({},{})"
for index,row in ds_Email_Data.iterrows():
    cursor.execute(sqlcmd.format(row['from_ID'],row['to_ID']))
    conn.commit()
cursor.close()
conn.close()

