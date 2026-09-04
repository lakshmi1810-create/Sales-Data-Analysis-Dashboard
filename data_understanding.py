def check_shape(df):
    print("\n=========== DATASET SHAPE ==========")
    rows,cols = df.shape
    print(f"Rows : {rows}")
    print(f"Columns : {cols}")

def show_columns(df):
    print("\n=========== COLUMN NAMES ==========")
    column_names = df.columns
    for index, column in enumerate(column_names, start=1):
        print(f"{index}. {column}")

def check_data_types(df):
    print("\n=========== DATA TYPES ==========")
    data_types = df.dtypes
    # print(data_types)
    return data_types

def dataset_info(df):
    print("\n=========== DATASET INFORMATION ==========")
    df.info()

def statistical_summary(df):
    print("\n=========== STATISTICAL SUMMARY ==========")
    return df.describe()

def check_missing_values(df):
    print("\n=========== MISSING VALUES ==========")
    missing_values = df.isnull().sum()
    return missing_values   

def check_duplicates(df):
    print("\n=========== DUPLICATE ROWS ==========")
    duplicate_rows = df.duplicated().sum()
    # print(f"Duplicate Rows : {duplicate_rows}")
    return duplicate_rows

def data_understanding_menu(df):
    while True:
        print("\n=========================================")
        print("         DATA UNDERSTANDING")
        print("=========================================")
        print("1. Check Dataset Shape")
        print("2. Show Column Names")
        print("3. Check Data Types")
        print("4. Dataset Information")
        print("5. Statistical Summary")
        print("6. Check Missing Values")
        print("7. Check Duplicates")
        print("8. Back")
        print("=========================================")
        try:
            choice = int(input("Enter Your Choice : "))
            if choice == 1:
                check_shape(df)
            elif choice == 2:
                show_columns(df)
            elif choice == 3:
                print(check_data_types(df))
            elif choice == 4:
                dataset_info(df)
            elif choice == 5:
                print(statistical_summary(df))
            elif choice == 6:
                print(check_missing_values(df))
            elif choice == 7:
                print(f"Duplicated Rows : {check_duplicates(df)}")
            elif choice == 8:
                break
            else:
                print("Invalid Choice!")
        except ValueError:
            print("Enter numbers only!")

        

    










    



