# table_genie
Smart functions for reading PDF tables and creating csvs

# Instructions for use
Place contiguous pages of tables in the "tables" directory.
Run tableGenie.py
A new file is created with "cleansed" appended to it in the tables directory
Only contiguous tables can be run simultaneously, at this time.

# Future considerations
## Properties that define if two tabels belong together:
The first section of the table before a page break will have row index names.
The following sections of the tables will not
Column headers will be of a similar format (regex?)

## Control flows
If the first table has a fully empy row, remove that row
If any following table has a fully empty row, remove that row

If the table defined as the first section of a table spanning pages has 100% empty columns after the row name, add that row index to a list
The blank row list can be used to add blank rows to the following tables

After the table is built, check the variance, std dev, mean of each row as a safety check.