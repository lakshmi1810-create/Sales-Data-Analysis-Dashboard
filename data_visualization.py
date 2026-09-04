import matplotlib.pyplot as plt
import seaborn as sns
import eda_analysis as ed
sns.set_style("darkgrid")

def plot_sales_by_category(df):
    result = ed.sales_by_category(df)
    plt.figure(figsize=(8,5))
    sns.barplot(x=result.index, y=result.values, palette="viridis")
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()

def plot_monthly_sales(df):
    result = ed.monthly_sales(df)
    plt.figure(figsize=(10,5))
    sns.lineplot(x=result.index, y=result.values, marker= "o")
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()

def plot_profit_by_category(df):
    result = ed.profit_by_category(df)
    plt.figure(figsize=(8,5))
    sns.barplot(x=result.index, y=result.values, palette="viridis")
    plt.title("Profit by Category")
    plt.xlabel("Category")
    plt.ylabel("Profit")
    plt.tight_layout()
    plt.show()

def plot_top_products(df):
    result = ed.top_selling_products(df)
    plt.figure(figsize=(10,6))
    sns.barplot(x=result.values,y=result.index, palette="viridis")
    plt.title("Top 10 Products by Sales")
    plt.xlabel("Sales")
    plt.ylabel("Products")
    plt.tight_layout()
    plt.show()

def plot_top_profit_products(df):
    result = ed.top_profitable_products(df)
    plt.figure(figsize=(10,6))
    sns.barplot(x=result.values, y=result.index, palette="viridis")
    plt.title("Top 10 Products by Profit")
    plt.xlabel("Profit")
    plt.ylabel("Products")
    plt.tight_layout()
    plt.show()

def plot_sales_vs_profit(df):

    result = ed.sales_vs_profit(df)

    plt.figure(figsize=(10,6))

    sns.scatterplot(
        data=result,
        x="Sales",
        y="Profit",
        hue="Status",
        palette={"Profit": "green", "Loss": "red"},
        alpha=0.7,
        s=60
    )

    plt.axhline(y=0, color="black", linestyle="--", linewidth=1)

    plt.title("Sales vs Profit")
    plt.xlabel("Sales")
    plt.ylabel("Profit")
    plt.legend(title="Order Status")
    plt.tight_layout()
    plt.show()

def visualization_menu(df):
    while True:
        print("\n=========================================")
        print("           DATA VISUALIZATION")
        print("=========================================")
        print("1. Sales by Category")
        print("2. Monthly Sales Trend")
        print("3. Profit by Category")
        print("4. Top Products by Sales")
        print("5. Top Products by Profit")
        print("6. Sales vs Profit")
        print("7. Back")
        print("=========================================")
        try:
            choice = int(input("Enter your choice : "))
            if choice == 1:
                plot_sales_by_category(df)
            elif choice == 2:
                plot_monthly_sales(df)
            elif choice == 3:
                plot_profit_by_category(df)
            elif choice == 4:
                plot_top_products(df)
            elif choice == 5:
                plot_top_profit_products(df)
            elif choice == 6:
                plot_sales_vs_profit(df)
            elif choice == 7:
                break
            else:
                print("Invalid Choice!")
        except ValueError:
            print("Enter numbers only!")