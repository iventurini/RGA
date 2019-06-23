
SELECT *
FROM(
SELECT b.[User_ID] as [User_ID]
	  ,'Sent' as Type
	  ,CASE WHEN c.[Region] IS NULL  THEN ('EXTERNAL') ELSE (CASE when (b.Region = c.Region) then 'SAME REGION' else 'ANOTHER REGION' end) end as Email_Region
	  ,CASE WHEN c.[Office] IS NULL  THEN ('EXTERNAL') ELSE (CASE when (b.Office = c.Office) then 'SAME OFFICE' else 'ANOTHER OFFICE' end) end as Email_Office
	  ,CASE WHEN c.[Department] IS NULL  THEN ('EXTERNAL') ELSE (CASE when (b.Department = c.Department) then 'SAME DEPARTMENT' else 'ANOTHER DEPARTMENT' end) end as Email_Department
FROM [InterviewProject_IgnacioJavierVenturini].[dbo].[Email_Data] as a
	   left join [InterviewProject_IgnacioJavierVenturini].[dbo].[Employee_Roster_Data] as b on  a.from_ID = b.Email_ID 
	   left join [InterviewProject_IgnacioJavierVenturini].[dbo].[Employee_Roster_Data] as c on   a.to_ID   = c.Email_ID 
Union all
SELECT c.[User_ID] as [User_ID]
	  ,'Received' as Type
	  ,CASE WHEN b.[Region] IS NULL  THEN ('EXTERNAL') ELSE (CASE when (b.Region = c.Region) then 'SAME REGION' else 'ANOTHER REGION' end) end as Email_Region
	  ,CASE WHEN b.[Office] IS NULL  THEN ('EXTERNAL') ELSE (CASE when (b.Office = c.Office) then 'SAME OFFICE' else 'ANOTHER OFFICE' end) end as Email_Office
	  ,CASE WHEN b.[Department] IS NULL THEN ('EXTERNAL') ELSE (CASE when (b.Department = c.Department) then 'SAME DEPARTMENT' else 'ANOTHER DEPARTMENT' end) end as Email_Department
FROM [InterviewProject_IgnacioJavierVenturini].[dbo].[Email_Data] as a
	   left join [InterviewProject_IgnacioJavierVenturini].[dbo].[Employee_Roster_Data] as b on  a.from_ID = b.Email_ID 
	   left join [InterviewProject_IgnacioJavierVenturini].[dbo].[Employee_Roster_Data] as c on   a.to_ID   = c.Email_ID 
) as d
where d.[User_ID] is not null
