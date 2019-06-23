USE [InterviewProject_IgnacioJavierVenturini]
GO

DROP TABLE IF EXISTS [dbo].[Hours];
GO

CREATE TABLE [dbo].[Hours](
	[Date] [date] NULL,
	[UserId] [int] NULL,
	[AdminHrs1] [float] NULL,
	[AdminHrs2] [float] NULL,
	[AdminHrs3] [float] NULL,
	[ClientHrs1] [float] NULL,
	[ClientHrs2] [float] NULL,
	[ClientHrs3] [float] NULL,
	[TargetClientHrs] [float] NULL	
) ON [PRIMARY]
GO

DROP TABLE IF EXISTS [dbo].[Skills];
GO

CREATE TABLE [dbo].[Skills](
	[UserId] [int] NULL,
	[Fullname] [varchar](50) NULL,
	[Attribute Group] [varchar](50) NULL,
	[Attribute Sub-Group] [varchar](50) NULL,
	[Attribute Type] [varchar](50) NULL,
	[Attribute Name] [varchar](50) NULL,
	[Attribute Level] [int] NULL,
	[Attribute Verified] [bit] NULL
) ON [PRIMARY]
GO

DROP TABLE IF EXISTS [dbo].[Email_Data];
GO

CREATE TABLE [dbo].[Email_Data](
	[from_ID] [int] NULL,
	[to_ID] [int] NULL
) ON [PRIMARY]
GO

