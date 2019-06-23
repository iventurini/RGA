USE [InterviewProject_IgnacioJavierVenturini]
GO

ALTER TABLE [dbo].[Hours]
	DROP COLUMN IF EXISTS [Total Working hours by Employee]
GO
ALTER TABLE [dbo].[Hours]
	DROP COLUMN IF EXISTS [Utilization]
GO
ALTER TABLE [dbo].[Hours]
	DROP COLUMN IF EXISTS [Client Time]
GO
ALTER TABLE [dbo].[Hours]
	DROP COLUMN IF EXISTS [Admin Time]
GO
ALTER TABLE [dbo].[Skills]
	DROP COLUMN IF EXISTS [Skills Level]
GO
ALTER TABLE [dbo].[Hours]
	ADD [Total Working hours by Employee] [float] NULL
GO
ALTER TABLE [dbo].[Hours]
	ADD [Utilization] [float] NULL
GO
ALTER TABLE [dbo].[Hours]
	ADD [Client Time] [float] NULL
GO
ALTER TABLE [dbo].[Hours]
	ADD [Admin Time] [float] NULL
GO
ALTER TABLE [dbo].[Skills]
	ADD [Skills Level] [varchar](50) NULL
GO



UPDATE
    [dbo].[Hours]
SET
    /*[Total Working hours by Employee] = 8*((DATEDIFF(dd, [Date], DATEADD (dd, -1, DATEADD(mm, DATEDIFF(mm, 0, [Date]) + 1, 0))) + 1)-(DATEDIFF(wk, [Date], DATEADD (dd, -1, DATEADD(mm, DATEDIFF(mm, 0, [Date]) + 1, 0))) * 2)-(CASE WHEN DATEPART(dw, [Date]) = 1 THEN 1 ELSE 0 END)-(CASE WHEN DATEPART(dw, DATEADD (dd, -1, DATEADD(mm, DATEDIFF(mm, 0, [Date]) + 1, 0))) = 7 THEN 1 ELSE 0 END))*/
	[Total Working hours by Employee] = 160
FROM
    [dbo].[Hours];

UPDATE
    [dbo].[Hours]
SET
    [Utilization] = (CASE WHEN ([Total Working hours by Employee]-(ISNULL([AdminHrs1],0)+ISNULL([AdminHrs2],0)+ISNULL([AdminHrs3],0))) = 0 THEN 0 ELSE ((ISNULL([ClientHrs1],0)+ISNULL([ClientHrs2],0)+ISNULL([ClientHrs3],0))/([Total Working hours by Employee]-(ISNULL([AdminHrs1],0)+ISNULL([AdminHrs2],0)+ISNULL([AdminHrs3],0)))) END),
	[Client Time] = ((ISNULL([ClientHrs1],0)+ISNULL([ClientHrs2],0)+ISNULL([ClientHrs3],0))/([Total Working hours by Employee])),
	[Admin Time] = ((ISNULL([AdminHrs1],0)+ISNULL([AdminHrs2],0)+ISNULL([AdminHrs3],0))/([Total Working hours by Employee]))
FROM
    [dbo].[Hours];

UPDATE
    [dbo].[Skills]
SET
    [Skills Level] = (CASE WHEN ([Attribute Level] = 0) THEN '0: wants to learn.' WHEN  ([Attribute Level] = 1 or [Attribute Level] = 2) THEN '1-2: Heavy supervision' WHEN ([Attribute Level] = 3 or [Attribute Level] = 4) THEN '3-4: Light supervision' ELSE '5: Expert' END)
FROM
    [dbo].[Hours];