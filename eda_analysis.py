def sales_summary(df):
    total_sales = df["Sales"].sum()
    average_sales = df["Sales"].mean()
    highest_sales = df["Sales"].max()
    lowest_sales = df["Sales"].min()
    return total_sales, average_sales, highest_sales, lowest_sales

def sales_by_category(df):
    sales_data = df[['Category', 'Sales']]
    result = sales_data.groupby("Category")["Sales"].sum()
    sorted_result_category = result.sort_values(ascending = False)
    return sorted_result_category

def sales_by_subcategory(df):
    sales_data = df[['Sub-Category', 'Sales']]
    result = sales_data.groupby("Sub-Category")["Sales"].sum()
    sorted_result_subcategory = result.sort_values(ascending = False)
    return sorted_result_subcategory

def top_selling_products(df):
    sales_data = df[['Product Name', 'Sales']]
    result = sales_data.groupby("Product Name")["Sales"].sum()
    sorted_result_products = result.sort_values(ascending = False)
    top_products = sorted_result_products.head(10)
    return top_products

def sales_by_segment(df):
    sales_data = df[['Segment', 'Sales']]
    result = sales_data.groupby("Segment")["Sales"].sum()
    sorted_result_segment = result.sort_values(ascending = False)
    return sorted_result_segment

def sales_by_state(df):
    sales_data = df[['State', 'Sales']]
    result = sales_data.groupby("State")["Sales"].sum()
    sorted_result_state = result.sort_values(ascending = False)
    top_states = sorted_result_state.head(10)
    return top_states

def profit_summary(df):
    total_profit = df["Profit"].sum()
    average_profit = df["Profit"].mean()
    highest_profit = df["Profit"].max()
    lowest_profit = df["Profit"].min()
    return total_profit, average_profit, highest_profit, lowest_profit

def profit_by_category(df):
    profit_data = df[['Category', 'Profit']]
    result = profit_data.groupby("Category")["Profit"].sum()
    sorted_result_category = result.sort_values(ascending = False)
    return sorted_result_category

def profit_by_state(df):
    profit_data = df[['State', 'Profit']]
    result = profit_data.groupby("State")["Profit"].sum()
    sorted_result_state = result.sort_values(ascending = False)
    top_states_profit = sorted_result_state.head(10)
    return top_states_profit

def top_profitable_products(df):
    profit_data = df[['Product Name', 'Profit']]
    result = profit_data.groupby("Product Name")["Profit"].sum()
    sorted_result_products = result.sort_values(ascending = False)
    top_products_profit = sorted_result_products.head(10)
    return top_products_profit

def monthly_sales(df):
    monthly_data = df[['Order Date', 'Sales']].copy()
    monthly_data['Month'] = monthly_data['Order Date'].dt.to_period('M')
    result = monthly_data.groupby('Month')['Sales'].sum()
    sorted_result = result.sort_index()

    sorted_result.index = sorted_result.index.to_timestamp()

    return sorted_result

def sales_vs_profit(df):
    sales_profit = df[['Sales', 'Profit']].copy()

    sales_profit["Status"] = sales_profit["Profit"].apply(
        lambda x: "Profit" if x >= 0 else "Loss"
    )

    return sales_profit

def eda_analysis_menu(df):
    while True:
        print("\n=========================================")
        print("              DATA ANALYSIS")
        print("=========================================")
        print("1. Sales Summary")
        print("2. Sales by Category")
        print("3. Sales by Sub-Category")
        print("4. Top Selling Products")
        print("5. Sales by Segment")
        print("6. Sales by State")
        print("7. Profit Summary")
        print("8. Profit by Category")
        print("9. Profit by State")
        print("10. Top Profitable Products")
        print("11. Monthly Sales Trend")
        print("12. Back")
        print("=========================================")
        try:
            choice = int(input("Enter your choice : "))
            if choice == 1:
                total_sales, average_sales, highest_sales, lowest_sales = sales_summary(df)
                print("Total Sale : ", total_sales)
                print("Average Sale : ", average_sales)
                print("Highest Sale : ", highest_sales)
                print("Lowest Sale : ", lowest_sales)

            elif choice == 2:
                print("\nSales by Category : ")
                print(sales_by_category(df))

            elif choice == 3:
                print("\nSales by Sub-Category : ")
                print(sales_by_subcategory(df))

            elif choice == 4:
                print("\nTop Selling Products : ")
                print(top_selling_products(df))

            elif choice == 5:
                print("\nSales by Segment : ")
                print(sales_by_segment(df))

            elif choice == 6:
                print("\nSales by State : ")
                print(sales_by_state(df))

            elif choice == 7:
                total_profit, average_profit, highest_profit, lowest_profit = profit_summary(df)
                print("Total Profit : ", total_profit)
                print("Average Profit : ", average_profit)
                print("Highest Profit : ", highest_profit)
                print("Lowest Profit : ", lowest_profit)

            elif choice == 8:
                print("\nProfit by Category : ")
                print(profit_by_category(df))

            elif choice == 9:
                print("\nProfit by State : ")
                print(profit_by_state(df))

            elif choice == 10:
                print("\nTop Profitable Products : ")
                print(top_profitable_products(df))

            elif choice == 11:
                print("\nMonthly Sales : ")
                print(monthly_sales(df))

            elif choice == 12:
                break

            else:
                print("Invalid Choice!")

        except ValueError:
            print("Enter numbers only!")


                



        


            

    
