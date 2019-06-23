USE [InterviewProject_IgnacioJavierVenturini]
GO
DROP TABLE IF EXISTS [dbo].[Employee_Roster_Data];
GO

CREATE TABLE [dbo].[Employee_Roster_Data](
	[User_ID] [int] NULL,
	[Email_ID] [int] NULL,
	[Title] [int] NULL,
	[Fullname] [varchar](50) NULL,
	[Department] [varchar](50) NULL,
	[Gender] [varchar](50) NULL,
	[Office] [int] NULL,
	[Region] [int] NULL,
	[Tenure_Yrs] [float] NULL,
	[Seniority] [int] NULL,
	[Salary] [float] NULL,
	[Currency] [varchar](3) NULL,
	[Rating] [int] NULL,
	[Survey_Score] [float] NULL,
	[Promotion] [int] NULL,
	[Avg_Hrs] [float] NULL,
	[ER_TO_USD] [float] NULL,
	[Salary_USD] [float] NULL
) ON [PRIMARY]
GO


