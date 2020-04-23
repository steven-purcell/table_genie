import pandas as pd
import glob
import numpy as np

row_value = ""
in_path = r'/Users/stevenpurcell/repos/table_genie/tables' # use your path
out_path = ""
all_files = glob.glob(in_path + "/*.csv")
all_files.sort()
li = []
rowAdj = []

# Function to insert row in the dataframe 
def insert_row(row_number, df, row_value): 
    # Starting value of upper half 
    start_upper = 0
    # End value of upper half 
    end_upper = row_number 
    # Start value of lower half 
    start_lower = row_number 
    # End value of lower half 
    end_lower = df.shape[0] 
    # Create a list of upper_half index 
    upper_half = [*range(start_upper, end_upper, 1)] 
    # Create a list of lower_half index 
    lower_half = [*range(start_lower, end_lower, 1)] 
    # Increment the value of lower half by 1 
    lower_half = [x.__add__(1) for x in lower_half] 
    # Combine the two lists 
    index_ = upper_half + lower_half 
    # Update the index of the dataframe 
    df.index = index_ 
    # Insert a row at the end 
    df.loc[row_number] = row_value 
    # Sort the index labels 
    df = df.sort_index() 
    # return the dataframe 
    return df 
   

df = pd.read_csv(all_files[0], index_col=None, header=1)
df.dropna(axis=0, how='all', inplace=True)
df = df.reset_index()
rec = df[df.iloc[:,2:].isnull().all(axis=1)]
rec = rec[rec==True]
rowAdj = rec.index.to_list()


for table in all_files[1:]:
    df_temp = pd.read_csv(table, index_col=None, header=1)
    df_temp.dropna(axis = 0, how='all', inplace = True)

    for row_number in rowAdj:
        df_temp = insert_row(row_number, df_temp, row_value)
        
    df = pd.concat([df, df_temp], axis=1)
    df_final = df.drop('index', axis=1)
df_final = df_final.replace('NaN', '', regex=True)
df_final = df_final.fillna('')
df_final.to_csv(all_files[0].strip('.csv')+'_cleansed.csv', index=False)
