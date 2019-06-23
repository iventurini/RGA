
# coding: utf-8

# In[1]:

import pandas as pd
import pyodbc 
import fixerio #import library i create to interact with fixerio api.
from datetime import date

API_KEY = '8282ca766a3168db2caabbb9480cae38'
SQLSERVER = 'GB3SIS10NOTVI\SQLEXPRESS'
SQLDB = 'InterviewProject_IgnacioJavierVenturini' 

ds_erd = pd.read_excel('..\datasources\Employee_Roster_Data.xlsx','Sheet1')


# In[2]:

resp = fixerio.get_historical(API_KEY,date(2013, 4, 3),'EUR',",".join(ds_erd['Currency'].drop_duplicates()))
if (resp.status_code != 200):
    #something went wrong with request
    #should manage this error
    pass
elif (not resp.json()["success"]):
    #something went wrong with api
    #should manage this error
    print("Code: {}".format(resp.json()["error"]["code"]))
    print("Info: {}".format(resp.json()["error"]["info"]))
    print("Type: {}".format(resp.json()["error"]["type"]))
else:
    #convert response into df
    rate = pd.DataFrame.from_dict(resp.json()['rates'], orient='index')
    #rename columns
    rate.columns = ['ER_TO_EUR']
    rate['Currency'] = rate.index
    #as with free license, I can only get Exchange rates with base currency in EUR, so i calculate the Exchange rate to USD
    usd_to_eur = rate[(rate['Currency'] == 'USD')].iloc[0,0]
    rate['ER_TO_USD'] = usd_to_eur / rate['ER_TO_EUR']
    #drop innecesary columns
    rate = rate.drop(columns=['ER_TO_EUR'])
    #left join with original ds
    ds_erd = pd.merge (ds_erd, rate, how='left', left_on=['Currency'], right_on=['Currency'])
    #calulate new column with salary in USD
    ds_erd['Salary_USD'] = ds_erd['Salary']*ds_erd['ER_TO_USD'] 
    #replace single quote in char fields to avoid "Unclosed quotation mark after the character string" error
    for col in ds_erd.columns:
        if (ds_erd[col].dtype == 'object' ):
            ds_erd[col] = ds_erd[col].str.replace("'","''")
    #connect to sql to insert data
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=' + SQLSERVER + ';'
                          'Database=' + SQLDB + ';'
                          'Trusted_Connection=yes;')
    sqlcmd = "INSERT INTO [Employee_Roster_Data]([User_ID],[Email_ID],[Title],[Fullname],[Department],[Gender],[Office],[Region],[Tenure_Yrs],[Seniority],[Salary],[Currency],[Rating],[Survey_Score],[Promotion],[Avg_Hrs],[ER_TO_USD],[Salary_USD]) values ({},{},{},'{}','{}','{}',{},{},{},{},{},'{}',{},{},{},{},{},{})"
    cursor = conn.cursor()
    for index,row in ds_erd.iterrows():
        cursor.execute(sqlcmd.format(row['User_ID'],row['Email_ID'],row['Title'],row['Fullname'],row['Department'],row['Gender'],row['Office'],row['Region'],row['Tenure_Yrs'],row['Seniority'],row['Salary'],row['Currency'],row['Rating'],row['Survey_Score'],row['Promotion'],row['Avg_Hrs'],row['ER_TO_USD'],row['Salary_USD']))
        conn.commit()
    cursor.close()
    conn.close()

