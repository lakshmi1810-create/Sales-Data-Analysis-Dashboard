from data_loader import load_data
import data_understanding as du
import data_cleaning as dc
import eda_analysis as ed
import data_visualization as dv


def main_menu():
    df = load_data("Superstore.csv")
    if df is None:
        print("Program terminated.")
        return

    datatype_ready = False

    while True:
        print("\n=================================================")
        print("               SALES DATA ANALYSIS")
        print("=================================================")
        print("1. Data Understanding")
        print("2. Data Cleaning")
        print("3. EDA Analysis")
        print("4. Visualization")
        print("5. Exit")
        print("=================================================")

        try:
            choice = int(input("Enter your choice : "))

            if choice == 1:
                du.data_understanding_menu(df)

            elif choice == 2:
                df, datatype_ready = dc.data_cleaning_menu(df)

            elif choice == 3:
                if datatype_ready:
                    ed.eda_analysis_menu(df)
                else:
                    print("Please handle data types before EDA!")

            elif choice == 4:
                if datatype_ready:
                    dv.visualization_menu(df)
                else:
                    print("Please handle data types before Visualization!")

            elif choice == 5:
                print("Thank you for using Sales Data Analysis!")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Enter numbers only!")


if __name__ == "__main__":
    main_menu()