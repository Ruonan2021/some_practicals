# 1. Tableau environment

## 1.1 Automatic fields

Measure name, measure value, count of table, lat, long

**Measure name & measure values**

Measure name is the name of measure

Measure value is the value of measure

Can be used to show measures in different dimension

![image-20220812220653612](C:%5CUsers%5CLenovo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20220812220653612.png)



## 1.2 Shelves and cards references

Page shelf: used as filter function



## 1.3 Tableau file types

![image-20220812225657068](C:%5CUsers%5CLenovo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20220812225657068.png)

![image-20220812225815019](C:%5CUsers%5CLenovo%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20220812225815019.png)

if open .twbx, save as .twb, Tableau will also create a folder, including Data folder and a .hyper file  

## 1.4 Visual cues and icons

[Details of visual cues and icons](https://help.tableau.com/current/pro/desktop/en-us/tips_visualcues.htm)

Some categories:

1. [Data sources in the Data](https://help.tableau.com/current/pro/desktop/en-us/tips_visualcues.htm#:~:text=a%20data%20view.-,Data%20sources%20in%20the%20Data%20pane,-The%20following%20table)
2. [Fields in the Data Pane](https://help.tableau.com/current/pro/desktop/en-us/tips_visualcues.htm#:~:text=to%20Tableau%20Server.-,Fields%20in%20the%20Data%20Pane,-The%20following%20table)
3. [Fields on Shelves](https://help.tableau.com/current/pro/desktop/en-us/tips_visualcues.htm#:~:text=Blend%20Your%20Data-,Fields%20on%20Shelves,-Fields%20placed%20on)
4. [Fields on the Marks card](https://help.tableau.com/current/pro/desktop/en-us/tips_visualcues.htm#:~:text=in%20the%20view.-,Fields%20on%20the%20Marks%20card,-Fields%20placed%20on)
5. [Sheets in the Dashboards and Worksheets pane](https://help.tableau.com/current/pro/desktop/en-us/tips_visualcues.htm#:~:text=drop%2Ddown%20menu.-,Sheets%20in%20the%20Dashboards%20and%20Worksheets%20pane,-The%20following%20table)
6. [Fields in the Calculation editor](https://help.tableau.com/current/pro/desktop/en-us/tips_visualcues.htm#:~:text=is%20a%20dashboard.-,Fields%20in%20the%20Calculation%20editor,-Fields%20in%20the)

# 2. Tableau concept

## 2.1 Data type

Some basic types are in the following figure. For more types could refer to [Data sources in the Data](https://help.tableau.com/current/pro/desktop/en-us/tips_visualcues.htm#:~:text=a%20data%20view.-,Data%20sources%20in%20the%20Data%20pane,-The%20following%20table) in 1.4 Visual cues and icons.

Three ways to [change the data ](https://help.tableau.com/current/pro/desktop/en-us/datafields_typesandroles_datatypes.htm#:~:text=the%20Data%20pane.-,Change%20the%20data%20type%20for%20a%20field%20in%20the%20Data%20Source%20page,-Sometimes%20Tableau%20incorrectly):

1. From data source page
2. From data pane
3. From view

![image-20221102065051084](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221102065051084.png)



## 2.2 Good dataset

1. Necessary elements
2. Both dimensions and measures(discrete and continuous)
3. Disaggregated

## 2.3 Order of operation

Very important

![image-20220814001939296](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220814001939296.png)

**！！！ Context filter**

Eg: when selecting top N in specific condition

Such as select top N sales in New York City.

1. First step is to set [City] as context, then filter 'New York'

2. Then select top N on Customer Name



# Domain 1: Connect to and Transform Data

## 1.1. Connect to data sources 

### 1.1.1. Choose an appropriate data source 

![image-20221018084419677](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221018084419677.png)

### 1.1.2. Choose between live connection or extract 

<img src="C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221016081146593.png" alt="image-20221016081146593" style="zoom:50%;" />

- **Live(default)**

  - Updated when: 1) opening a workbook or 2) manually refresh(right-click on data source)

    <img src="C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221016081711007.png" alt="image-20221016081711007" style="zoom:50%;" />

  - Note: if change column name: will occur error. Do solve it, right-click on broken field in data pane,  click [**Replace References**]

- **Extract**

  - Tableau makes a local copy of a subset of your data.

### 1.1.3. Connect to extracts 

Benefits of using extract data(.hyper format): old version is using .tde format

1. Create extraction for billions of rows of data
2. .hyper is faster
3. Efficient even for large extract

### 1.1.4. Connect to spreadsheets 

Eg: connect to excel

### 1.1.5. Connect to .hyper files (or .tde files) 

If only share .hyper file: connection information and column name changes will missing

.tdsx or .twbx file" accessible to extract data source

### 1.1.6. Connect to relational databases 

Knowing how to do is okay, haven't encountered in my exams.

### 1.1.7. Pull data from relational databases by using custom SQL queries 

Need to know basic SQL syntax such as SELECT, FROM, WHERE, GROUP BY

### 1.1.8. Connect to a data source on Tableau Server 

Connect panel -> Search for Data -> connect and log in

Data on the server could be downloaded: **Data** menu -> select data source -> select **Create Local Copy**

### 1.1.9. Replace the connected data source with another data source for an existing chart or sheet

![image-20221018203904734](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221018203904734.png)

##  1.2. Prepare data for analysis 

### 1.2.1. Assess data quality (completeness, consistency, accuracy) 

What should exam:

- Unique values
- Data type(number, string, date)
- Data role(URL, email address, zip code)
- Null, outliers, unexpected values

Tableau cares more about boniness understandings

### 1.2.2. Perform cleaning operations 

[tTableau Prep](https://help.tableau.com/current/prep/en-us/prep_clean.htm)

### 1.2.3. Organize data into folders

- Create a new folder: Select multiple fields and right click [**Folders** > **Create Folder**]
- Add to a folder: just drag

### 1.2.4.Use multiple data sources (establish relationships, create joins, union tables, blend data) 

### **Relationships**

Note: relationship(logical tables) in Tableau is different from Joins(physical tables)

**Benefits over join**

- No need join types(left, right, inner...)
- Automatic identify related fields
- Relationship will not merged into a single table
- Avoid duplications
- More refer to [Relate Your Data](https://help.tableau.com/current/pro/desktop/en-us/relate_tables.htm)

**Requirements**

- Fields mush have the same data type
- Geographic field can't define relationships
- Published data source can't define relationships

**Performance options**

<img src="C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221020075736329.png" alt="image-20221020075736329" style="zoom:80%;" />

[Exercise](https://help.tableau.com/current/pro/desktop/en-us/datasource_dont_be_scared.htm#:~:text=Analyze%20related%20data,of%20the%20scenario)



**Difference between relationship and joins**

![image-20221020073824692](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221020073824692.png )

**Difference between relationship and Blends**

[See more about blend](https://help.tableau.com/current/pro/desktop/en-us/multiple_connections.htm#step4relationships), blend is used for data in different aggregation levels



<img src="C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221020074103551.png" alt="image-20221020074103551" style="zoom:80%;" />

**Relationships, joins, and blends**

<img src="C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221020074411953.png" alt="image-20221020074411953" style="zoom:80%;" />



<img src="C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221020074444879.png" alt="image-20221020074444879" style="zoom:80%;" />





### 1.2.5. Prepare data by using Data Interpreter, pivot, and split 

[Interpreter](https://help.tableau.com/current/pro/desktop/en-us/data_interpreter.htm)

[Pivot](https://help.tableau.com/current/pro/desktop/en-us/pivot.htm)

- Automatic selection pivot 
- Customise pivot by SQL: union

[Split](https://help.tableau.com/current/pro/desktop/en-us/split.htm)

Three ways

- On the Data Source page, check the menu for **Split** and **Custom Split**.
- From the Data pane on a sheet, check the menu for **Transform** > **Split** and **Custom Split**
- Split manually using the **SPLIT function**: Split, right, left

### 1.2.6.Create extract filters 

[Link](https://help.tableau.com/current/pro/desktop/en-us/filtering_datasource.htm)

Good for data security: when published data, can specify query/modify rights for users and groups.

![image-20221025075447026](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221025075447026.png)

## 1.3. Perform data transformation in Tableau Prep 

### 1.3.1. Choose which data transformation to perform based on a business scenario 

Profile pane: summaries(type, distribution, unique counts)

- Outlier: using detail view
- Distribution: using summary view

Data grid(original data)

### 1.3.2. Combine data by using unions 

[Link](https://help.tableau.com/current/prep/en-us/prep_combine.htm)

### 1.3.3. Combine data by using joins 

[Link](https://help.tableau.com/current/prep/en-us/prep_combine.htm)

### 1.3.4. Shape data by using aggregations 

[Link](https://help.tableau.com/current/prep/en-us/prep_combine.htm)

### 1.3.5. Perform filtering 

When selecting a distribution bar or an individual value in the profile pane:

- The related values in the profile cards are highlighted in blue
- The data grid at the bottom is filtered

### 1.3.6.Shape data by using pivots 

[Link](https://help.tableau.com/current/prep/en-us/prep_pivot.htm)

## 1.4. Customize fields 

### 1.4.0 .tds

Tableau preserves the customizations you make, but it does **not change the underlying source data.**

**Benefits of  Tableau data source(.tds)**

1. Time-saving: you can reuse the .tds file in different workbooks.
2. Collaborative: you can share the .tds file with other users. 

**Tableau data source(.tds) includes:**

- Folder structure(Folder, groups, sets)
- Measure and dimension conversions
- Attributes (e.g., field names, calculated fields)
- Field data types (e.g., strings, integers, dates)
- Field properties (e.g., how a field is displayed or aggregated)

**Tableau data source(.tds) not includes:**

- Login information 
- Vizzes created with the data

**Save a Tableau data source (.tds) file locally**

Remember that saving the .tds to the **Datasources** folder under **My Tableau Repository** makes the .tds available from the **Connect** page under **Saved Data Sources**

<img src="C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221016070603243.png" alt="image-20221016070603243" style="zoom:50%;" />

**Open a locally saved Tableau data source (.tds) file** 

In connect page

<img src="C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221016082505030.png" alt="image-20221016082505030" style="zoom:50%;" />



**Folder structure**

<img src="C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221016064619184.png" alt="image-20221016064619184" style="zoom:50%;" />

**Measure and dimension conversions**

<img src="C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221016064746011.png" alt="image-20221016064746011" style="zoom:50%;" />

**Attributes**

1. Right-click to rename
2. Create an alias
   1. Only discrete dimension could create alias
   2. Right-click: Aliases...

**Field properties**

Dimensions: Comment, Colour, shape, sorted

Measures: Comment, Colour, Number Format, Aggregation, Total using



### 1.4.1. Change default field properties (types, sorting, etc.) 

Right click on the field

### 1.4.2.Rename columns 

Right click on the field

### 1.4.3.Choose when to convert between discrete and continuous 

Right click on the field

### 1.4.4.Choose when to convert between dimension and measure 

Right click on the field/drag

### 1.4.5.Create aliases

Right click on the field



# Domain 2: Explore and Analyse Data

##  2.1. Create calculated fields

###  2.1.1. Write date calculations (DATEPARSE, DATENAME…)

| Function                                           | What return                                                  | Example                                                      |
| -------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| DATEADD(date_part, interval, date)                 | Date, adds an increment to the specified date                | DATEADD('week', 1, [due date]); DATEADD('day', 280, #2/20/21#) = #November 27, 2021# |
| DATEDIFF(date_part, date1, date2, [start_of_week]) | Integer, returns the difference between date1 and date2 expressed in units of date_part | DATEDIFF('day', #3/25/1986#, #2/20/2021#) = 12,751           |
| DATENAME(date_part, date, [start_of_week])         | **String**, returns date_part of date as a string.           | DATENAME('year', #3/25/1986#) = "1986"; DATENAME('month', #1986-03-25#) = "March" |
| DATEPART(date_part, date, [start_of_week])         | **Integer**, returns date_part of date as an integer.        | DATEPART('year', #1986-03-25#) = 1986; DATEPART('month', #1986-03-25#) = 3 |
| DATEPARSE(date_format, [date_string])              | Date,                                                        | DATEPARSE('yyyy-MM-dd', "1986-03-25") = #March 25, 1986#     |
| DATETRUNC(date_part, date, [start_of_week])        | Date, the first [date_part] day of the [date]                | DATETRUNC(month, #9/22/2018#) = #9/1/2018#   I'm wondering Tableau made mistake on the last example of this function |
| DAY(date)                                          | Integer, 1-31                                                | Also WEEK, MONTH, QUARTER, YEAR, and the ISO equivalents     |
| ISDATE(string)                                     | Boolean                                                      | ISDATE(09/22/2018) = true                                    |
| MAKEDATE(year, month, day)                         | Date                                                         | MAKEDATE(1986,3,25) = #1986-03-25#                           |
| MAKEDATETIME(date, time)                           | Datetime                                                     | MAKEDATETIME("1899-12-30", #07:59:00#) = #12/30/1899 7:59:00 AM# |
| MAKETIME(hour, minute, second)                     | Datetime                                                     | MAKETIME(14, 52, 40) = #1/1/1899 14:52:40#                   |
| NOW()                                              | Datetime                                                     |                                                              |
| TODAY()                                            | Date                                                         |                                                              |

#### The date_part argument

![image-20221025225924239](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221025225924239.png)

###  2.1.2. Write string functions

[Link](https://help.tableau.com/current/pro/desktop/en-us/functions_functions_string.htm)



| Function                                         | Return                                                       | Definition                                                   |
| ------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ASCII(string)/ CHAR(number)                      |                                                              | ASCII('A') = 65/ CHAR(65) = 'A'                              |
| CONTAINS/ ENDSWITH/STARTSWITH(string, substring) | Boolean                                                      | CONTAINS(“Calculation”, “alcu”) = true; ENDSWITH(“Tableau”, “leau”) = true |
| FIND(string, substring, [start])                 | Index/ 0(if not found)                                       | FIND("Calculation", "alcu") = 2;` `FIND("Calculation", "Computer") = 0 |
| FINDNTH(string, substring, occurrence)           | Returns the position of the nth occurrence of substring within the specified string | FINDNTH("Calculation", "a", 2) = 7                           |
| LEFT(string, number);  RIGHT(string, number)     | Returns the left/right-most number of characters in the string. | LEFT("Matador", 4) = "Mata"; RIGHT("Calculation", 4) = "tion" |
| (MID(string, start, [length])                    | Returns the string starting at index position `start`        | MID("Calculation", 2) = "alculation"; MID("Calculation", 2, 5) ="alcul" |
| LTRIM/RTRIM/TRIM                                 |                                                              |                                                              |
| MAX/MIN(a, b)                                    |                                                              |                                                              |
| LOWER/UPPER                                      |                                                              |                                                              |
| SPLIT                                            | Returns a substring from a string, using a delimiter character to divide the string into a sequence of tokens | SPLIT (‘a-b-c-d’, ‘-‘, 2) = ‘b’; `SPLIT (‘a\|b\|c\|d’, ‘\|‘, -2) = ‘c’ |



###  2.1.3. Write logical and Boolean expressions (If, case, nested, etc.)

[Link](https://help.tableau.com/current/pro/desktop/en-us/functions_functions_logical.htm)

| Function                 | Description                                                  | Example                       |
| ------------------------ | ------------------------------------------------------------ | ----------------------------- |
| IN                       | <expr1> IN <expr2>                                           | SUM([Cost]) IN (1000, 15, 200 |
| IF/ELSEIF/ELSE/ENDAND/OR | IF <expr1> OR/AND <expr2> THEN <then> END                    |                               |
| CASE...END               | CASE <expression> WHEN <value1> THEN <return1> WHEN <value2> THEN <return2> ... ELSE <default return> END |                               |
| IIF                      | IIF(test, then, else, [unknown])                             |                               |
| IFNULL                   | IIF(test, then, else, [unknown]), Returns <expr1> if it is not null, otherwise returns <expr2> |                               |
| ZN                       | ZN(expression), Returns <expression> if it is not null, otherwise returns zero. |                               |



###  2.1.4. Write number functions

[Link](https://help.tableau.com/current/pro/desktop/en-us/functions_functions_number.htm), here only list function I'm not familiar

| Function | Description                                                  | Example                          |
| -------- | ------------------------------------------------------------ | -------------------------------- |
| DIV      | DIV(integer1, integer2)                                      | DIV(11,2) = 5                    |
| HEXBINX  | HEXBINX(number, number); Maps an x, y coordinate to the x-coordinate of the nearest hexagonal bin. | HEXBINX([Longitude], [Latitude]) |
| HEXBINY  | HEXBINY(number, number); Maps an x, y coordinate to the y-coordinate of the nearest hexagonal bin. | HEXBINY([Longitude], [Latitude]) |
| ZN       | ZN(expression); Returns <expression> if it is not null, otherwise returns zero. |                                  |



###  2.1.5. Write type conversion functions

[Link](https://help.tableau.com/current/pro/desktop/en-us/functions_functions_typeconversion.htm)

| Function used for | Functions                 | Example |
| ----------------- | ------------------------- | ------- |
| Date              | DATE/ DATETIME/ DATEPARSE |         |
| Number            | FLOAT/ INT                |         |
| String            | STR                       |         |



###  2.1.6. Write aggregate functions

[Link](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_aggregate_create.htm)

| Function                        | Syntax           | Definition                                                   |
| ------------------------------- | ---------------- | ------------------------------------------------------------ |
| ATTR                            | ATTR(expression) | If expression has a single value for all rows: return the value of the expression; Else return * |
| AVG/ MEDIAN/STDDEV/VAR/COVAR... |                  |                                                              |
| COUNT/ COUNTD                   |                  |                                                              |



### 2.1.7. Write FIXED LOD calculations 

[FIXED, INCLUDE, EXCLUDE](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod_exclude.htm)

A mixed use of exclude and fixed

![image-20221026220631032](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221026220631032.png)

## 2.2. Create quick table calculations 

Table(across): row

Table(down: column)

### 2.2.1. Moving average 

![image-20221026224350531](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221026224350531.png)

You can see the average sales over time. For example, the value listed for December 2011 is the average sales for October, November, and December, 2011. The value listed for January, 2012 is the average sales for November and December, 2011, and January, 2012



Or could using WINDOW_AVG() function



### 2.2.2. Percent of total 

Pane

![image-20221026230226624](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221026230226624.png)

Table

![image-20221026230315067](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221026230315067.png)

### 2.2.3. Running total

- Aggregates values cumulatively in a partition
- Could be

| Option  | Meaning                                                      |
| ------- | ------------------------------------------------------------ |
| Sum     | Cumulatively add                                             |
| Average | Average of the current and all the previous                  |
| Minimum | All values are replace by the lowest value in the original partition before the current |
| Maximum | All values are replace by the lowest value in the original partition before the current |



### 2.2.4. Difference and percent of difference 

![image-20221026223616335](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221026223616335.png)

![image-20221026223630070](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221026223630070.png)

With a **Difference From**, **Percent Difference From**, or **Percent From**:

Check **relative to**

![image-20221026225851362](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221026225851362.png)



### 2.2.5. Percentile 

 **Percentile** table calculation computes a **percentile rank** for each value in a partition.

![image-20221026230517082](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221026230517082.png)

Since February made a very small amount of sales in 2012 compared to the overall total, it is ranked as 0.0% (or number 1 out of 12, since this example is Ascending, and therefore ranked from least to most). Sales in January, 2012 were a bit higher and were therefore ranked as 9.1% (or number 2 out of 12 months). Since November made the most sales in 2012, it is ranked as 100% (or number 12 out of 12)

### 2.2.6. Compound growth rate

Could adjust "Relative to"

![image-20221027204247826](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221027204247826.png)



### 2.2.7 Add Second Calculation

Only with **Running Total** and **Moving Calculation**

##  2.3. Create custom table calculations

I prefer to understanding these concepts by creating a dashboard, one on the left is table calculation sheet; one on the right is the original sheet. In this way, any calculation can be compared between these two.



Also, [Show calculation assistance] is also helpful, highlighting the calculation areas.

![image-20221027213548227](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221027213548227.png)

### 2.3.1. Year to date 

### 2.3.2. Month to date 

### 2.3.3. Year over year 

### 2.3.4. Index 

- Need to know the difference between : Index, first, last

### 2.3.5. Ranking 

If a series = (23, 45, 45, 67), 

There are four types of ranking:

- Competition: results in (1, 2, 2, 4)
- Modified Competition: results in (1, 3, 3, 4)
- Dense: results in (1, 2, 2, 3)
- Unique: results in (1, 2, 3, 4)

### 2.3.6. First-last 

Explained in 2.3.4

Need to note here is 

- The logic of using index, ranking, first, last in table calculation is the same of the functions used in filed calculation
- Need to know how these are combine used with LOOKUP function

## 2.4. Create and use filters 

### 2.4.1. Apply filters to dimensions and measures 

By dragging a dimension/measure in to filter shelf, the the following window will pop out.

**Filter dimensions(categorical)**

![image-20221027214043140](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221027214043140.png)

**General**: select/deselect from the list or search(Custom value list)

**Wildcard**: include XXX  contains/starts with/ ends with/ exactly matches

​					exclude XXX NOT contains/starts with/ ends with/ exactly matches

**Condition**

<img src="C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221027214519767.png" alt="image-20221027214519767" style="zoom:80%;" />

**TOP**(like condition, add top/bottom N)

<img src="C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221027214556874.png" alt="image-20221027214556874" style="zoom:80%;" />

**Filter measures(quantitative data)**

For example, by dragging profit into filter shelf

**Step 1**: to choose a calculation method

![image-20221027214920014](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221027214920014.png)

**Step 2**: set range

![image-20221027215149367](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221027215149367.png)

**Filter date: similar to measures**



### 2.4.2. Configure filter settings including Top N, Bottom N, include, exclude, wildcard, and conditional 

Mentioned in 2.4.1

### 2.4.3. Add filters to extract, data sources, context

**Extract filter**: In Data Source pane, click [Edit] after selecting [Extract], will be similar as dimension/measure

**Data Source filter**: Next to [Extract Filter], click [Add], will be similar as dimension/measure

![image-20221027222250320](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221027222250320.png)

**Context filter**

Select [Add to Context] in from the dimension/measure filter shelf

Some characteristics:

- Appear at the top pf the filter shelf
- Grey colour
- Can't be rearranged



### 2.4.4. Apply filters to multiple sheets and data sources 

[Official link](https://help.tableau.com/current/pro/desktop/en-us/filter_across_datasources.htm)

Could also refer to e-learning: Create Dashboards and Stories/ Filtering Across Data

Or [Three methods step by step practical](https://resources.useready.com/blog/filter-across-multiple-data-sources-in-tableau-3-methods/):

1. Edit data source relationship, filter apply to related data source
2. Create calculation field
3. Add dashboard actions

## 2.5. Create parameters to enable interactivity 

[Official link include why parameter and how to creat it](https://help.tableau.com/current/pro/desktop/en-us/changing-views-using-parameters.htm)

[YouTube video](https://www.youtube.com/watch?v=Xk9HnpmWtsU&ab_channel=Tableau)

Parameters won't work by itself, need to combine with the following three ways

### 2.5.1. In calculations 

Table table could insert parameter to dynamically change the name

In Edit filters, Edit Set(dynamically select top N)

### 2.5.2. With filters 

In edit filter window

**Condition**: using by formula, could say this is parameter in calculation

**Top N**: by field or by formula

### 2.5.3. With reference lines 

Analytics pane, drag and choose, direct

## 2.6. Structure the data 

### 2.6.1. Sets 

[One example: parameter, top N sets, calulated field, ](https://help.tableau.com/current/pro/desktop/en-us/sortgroup_sets_topn.htm)

Sets are costumed field used to hold the subset of data based on a given condition

- Dynamic Sets
  - The members of a dynamic set change when the underlying data changes.
  - Dynamic sets can only be based on a single dimension.
  - **How**: Data pane, right-click a dimension and select **Create** > **Set**. Could use General, condition or Top
- Fixed Sets
  - The members of a dynamic set change when the underlying data changes.
  - Dynamic sets can only be based on a single dimension.
  - **How**: Right-click the mark(s) and select **Create Set**.
- Combine Sets

### 2.6.2. Bins 

Can I say Bins is for measure, Sets is for dimensions? Bins can be more than 2, while sets only 2(in/out)

### 2.6.3. Hierarchies 

By dragging to the top of another filed

### 2.6.4. Groups 

Right click on dimension/measure

## 2.7. Map data geographically 

[Mapping Concepts in Tableau](https://help.tableau.com/current/pro/desktop/en-us/maps_build.htm)(Some useful links are listed on the bottom within this hyper link)

### 2.7.1. Create symbol maps 

Proportional symbol maps: **showing quantitative data for individual locations**. Eg: plot earthquakes around the world and size them by magnitude

![image-20221030074922644](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221030074922644.png)

### 2.7.2. Create heat maps 

Heatmaps, or density maps, can be used when you want to **show a trend for visual clusters of data**.

### 2.7.3. Create density maps 

[Tableau](https://help.tableau.com/current/pro/desktop/en-us/maps_build.htm#Proportional:~:text=.-,Heatmaps%20(density%20maps),-Heatmaps%2C%20or%20density) put Heatmaps and density maps together, don't know why distinct these two here in exam guideline. 

- Could adjust colour, intensity, opacity, size

![image-20221030075735653](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221030075735653.png)

### 2.7.4. Create choropleth maps (filled maps)

![image-20221030074946000](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221030074946000.png)

Some other types of maps not required in exams: 

- Flow maps(path maps)
- Spider maps (origin-destination maps)



## 2.8. Summarize, model, and customize data by using the Analytics feature 

This part won't be difficult, some shares the sample pattern of operation.

### 2.8.1. Totals and subtotals 

[Official hellp](https://help.tableau.com/current/pro/desktop/en-us/calculations_totals_grandtotal_turnon.htm)

Could do both from **Analytic pane(Drag Total)** or **Analysis menu(Select total)**

Mostly use this window(even drag)

![image-20221030090334657](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221030090334657.png)

### 2.8.2. Reference lines 

Same in the window

### 2.8.3. Reference bands 

Same in the window

### 2.8.4. Average lines 

Feels like the same as the reference line. Same in the window

### 2.8.5. Trend lines 

Five types

![image-20221030091252798](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221030091252798.png)

### 2.8.6. Distribution bands 

Same in the window

### 2.8.7. Forecast by using default settings 

Only available in Tableau Desktop

To remove, edit, or read a description of the current forecast, go to the Analysis menu and choose **Forecast**. Other lines and bands can be removed by dragging

Forecasting is not supported for views based on multidimensional data sources. In addition, the view cannot contain any of the following:

- Table calculations
- Disaggregated measures
- Percent calculations
- Grand Totals or Subtotals
- Date values with aggregation set to Exact Date

### 2.8.8. Customize a data forecasting model

Enhance Forecast

1. Drag the same measure into detail
2. Right-click -  [Forecast Result](https://help.tableau.com/current/pro/desktop/en-us/forecast_field_results.htm): could see the forecast precision of the tooltip

### 2.8.9. Create a predictive model

MODEL_PERCENTILE

MODEL_QUANTILE



# Domain 3: Create Content 

## 3.1. Create charts 

### 3.1.1. Create basic charts from scratch (bar, line, pie, highlight table, scatter plot, histogram, tree map, bubbles, data tables, Gantt, box plots, area, dual axis, combo) 

Remind me: highlight table is using "Square"

[Official Link](https://help.tableau.com/current/pro/desktop/en-us/dataview_examples.htm)

### 3.1.2. Sort data (including custom sort) 

Ways of sorting

1. From header
2. From a field label
3. From toolbar

Could sort dimension filed based on Data source/ alphabetic, field(measure), manual, nested(independent sort within a pane)

## 3.2. Create dashboards and stories 

### 3.2.1. Combine sheets into a dashboard by using containers and layout options 

No need explore, all based on needs

### 3.2.2. Add objects 

![image-20221030105753446](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20221030105753446.png)

### 3.2.3. Create stories 

Creating stories itself is not difficult, but I found interesting on [The seven types of data stories](https://help.tableau.com/current/pro/desktop/en-us/story_best_practices.htm#:~:text=with%20your%20sequence.-,The%20seven%20types%20of%20data%20stories,-When%20you%20use)

1. **Change over time**: Uses a chronology to illustrate a trend.
2. **Drill down**: Sets context so that your audience better understands what's going on in a particular category.
3. **Zoom out**: Describes how something your audience cares about relates to the bigger picture.
4. **Contrast**: Shows how two or more subjects differ.
5. **Intersections**: Highlights important shifts when one category overtakes another.
6. **Factors**: Explains a subject by dividing it into types or categories.
7. **Outliers**: Shows anomalies or where things are exceptionally different.

## 3.3. Add interactivity to dashboards 

### 3.3.1. Apply a filter to a view 

**!! In Exam**

First select a sheet: use as filter

Right-click on the field to select **show Filter**

### 3.3.2. Add filter, URL, and highlight actions 

**Show Highlighter** is below Show Filter

### 3.3.3. Swap sheets by using parameters or sheet selector 

**!! In Exam**

[Swap by using parameter](https://medium.com/tableau-simplified/how-to-swap-sheets-in-tableau-using-parameter-option-543b9fafb2b2) note: need to set as floating for the swap effect

Another way is two click swap button

### 3.3.4. Add navigation buttons 

**!! In Exam**: how to click on the navigation button and redirect to a sheet

### 3.3.5. Implement user guiding sentences (click…, hover…, menu options) 

## 3.4. Format dashboards 

More practice and play around would be helpful

### 3.4.1. Apply color, font, shapes, styling 

### 3.4.2. Add custom shapes and color palettes 

### 3.4.3. Add annotations

### 3.4.4. Add tooltips 

### 3.4.5. Apply padding 

### 3.4.6. Remove gridlines, row-level and column-level bands, and shading 

### 3.4.7. Apply responsive design for specific device layouts



# Domain 4: Publish and Manage Content on Tableau Server and Tableau Online 

9% of the Exam, I didn't spend much time here

## 4.1. Publish Content

To understand a workbook's structure

1. Original data([credentials](https://help.tableau.com/current/pro/desktop/en-us/publishing_sharing_authentication.htm) )
2. Tableau data source(how to access the original data, calculations, extraction period)
3. Selecting views

To decide how to connect data and keep it up-to-date

### 4.1.1. Publish a workbook 

Need to know

1. The name of server
2. How to sign in

### 4.1.2. Publish a data source 

- If wish refresh extracted data source: must select Embed password or Allow refresh access
- If workbook connects to Tableau data source: embedding password

### 4.1.3. Print content 

### 4.1.4. Export content 

## 4.2. Schedule data updates 

### 4.2.1. Schedule data extract refreshes 

**!!! In exam**

### 4.2.2. Schedule a Tableau Prep workflow 

## 4.3. Manage Published workbooks 

### 4.3.1. Create alerts 

**!!! In exam**

### 4.3.2. Create subscriptions