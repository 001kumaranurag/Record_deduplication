# Record_deduplication

# importing the pandas module
import pandas as pd

# Importing the Dataset
dataframe = pd.read_csv('Deduplication Problem - Sample Dataset.csv')

# Creating the function deduplication_records()

def deduplication_records(df1):
    # Creating 2 empty lists and storing the broken first names and lastnames in them
    
    list1 = []
    list2 = []
    for i in range(df1.shape[0]):
        list1.append(df1.iloc[i,0].split())
    for j in range(df1.shape[0]):
        list2.append(df1.iloc[j,3].split())
        
    #Making 2 dataframes from the above created lists containing broken down first and last names
    df2 = pd.DataFrame(list1, columns = ['ln1','ln2'])
    df3 = pd.DataFrame(list2, columns = ['fn1', 'fn2'])
    
    # concatenating the input dataframe with above created dataframes
    df1 = pd.concat([df1, df2, df3], axis = 1)
    
    # Creating 'full_name_new' column 
    df1['full_name_new'] = df1['fn1'] + ' ' + df1['ln1'] + ' ' + df1['dob']
    df4 = df1.copy()
    
    # dropping duplicate entries based on 'full_name_new' column
    df4 = df4.drop_duplicates('full_name_new')
    
    # dropping the unneccessary columns
    df4.drop(['ln1', 'ln2', 'fn1', 'fn2', 
              'full_name_new',], axis = 1, inplace = True)
              
    # getting the number of deduplicated records
    a = df4.shape[0]
    # returning the deduplicated records
    return(df4, a)
   
# creating an instance of the deduplication_records function with sample input   
deduplication_records(dataframe)
        

