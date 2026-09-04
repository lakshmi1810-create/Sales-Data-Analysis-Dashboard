import pandas as pd
from data_understanding import check_missing_values, check_data_types, check_duplicates
def handle_missing_values(df):
    result = check_missing_values(df)
    missing_columns = result[result > 0]
    if len(missing_columns) > 0:
        print("Missing values exist")
        print(missing_columns)
        response = input("Want to remove rows(Y/N) : ").lower().strip()            
        if response == "y":
              before_rows = df.shape[0]
              print("Rows before cleaning : ", before_rows)
              df.dropna(subset=missing_columns.index, inplace = True)
              after_rows = df.shape[0]
              deleted_rows = before_rows - after_rows
              print("Rows deleted : ", deleted_rows)
              print("Rows remaining : ", after_rows) 
              print("Missing values handled sucessfully!")             
        elif response == "n":
             print("Missing values not removed!")
        else:
             print("Invalid choice!")       
    else:
        print("No missing values found!") 
    return df

def handle_duplicates(df):
     duplicate_count = check_duplicates(df)
     print("Duplicate rows found : ", duplicate_count)
     if duplicate_count > 0:
          print("Duplicate rows exist")
          response = input("Want to remove duplicate rows(y/n) : ").lower().strip()
          if response == "y":
               before_rows = df.shape[0]
               print("Rows before cleaning : ", before_rows)
               df.drop_duplicates(inplace = True)
               after_rows = df.shape[0]
               deleted_rows = before_rows - after_rows
               print("Duplicate rows removed : ", deleted_rows)
               print("Rows remaining : ", after_rows)
               print("Duplicate rows handled successfully!")
          elif response == "n":
               print("Duplicate rows not removed!")
          else:
               print("Invalid choice!")
     else:
          print("No duplicate rows found!")
     return df

def handle_data_types(df):
     data_types = check_data_types(df)
     print(data_types) 
     df['Order Date']  = pd.to_datetime(df['Order Date'], format='mixed')
     df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='mixed')
     df['Postal Code'] = df['Postal Code'].astype(str)
     new_data_types = check_data_types(df)
     print(new_data_types)
     print("Data type conversion completed successfully!")
     return df

def data_cleaning_menu(df):
    datatype_ready = False

    while True:
        print("\n=========================================")
        print("              DATA CLEANING")
        print("=========================================")
        print("1. Handle Missing Values")
        print("2. Handle Duplicates")
        print("3. Handle Data Types")
        print("4. Back")
        print("=========================================")

        try:
            choice = int(input("Enter your choice : "))

            if choice == 1:
                df = handle_missing_values(df)

            elif choice == 2:
                df = handle_duplicates(df)

            elif choice == 3:
                df = handle_data_types(df)
                datatype_ready = True

            elif choice == 4:
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Enter numbers only!")

    return df, datatype_ready





    