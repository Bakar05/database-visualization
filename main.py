import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ========== SALES DASHBOARD ==========
def sales_dashboard():
    conn = sqlite3.connect("sales.db")

    # Load views
    df_city = pd.read_sql_query("SELECT * FROM analysis_by_city;", conn)
    df_month = pd.read_sql_query("SELECT * FROM analysis_by_month;", conn)
    df_state = pd.read_sql_query("SELECT * FROM analysis_by_state;", conn)
    df_product = pd.read_sql_query("SELECT * FROM analysis_by_product;", conn)
    df_december = pd.read_sql_query("SELECT * FROM analysis_of_december;", conn)

    conn.close()
    sns.set_style("whitegrid")

    fig = plt.figure(figsize=(20, 15))
    gs = GridSpec(3, 2)

    ax1 = fig.add_subplot(gs[0, 0])
    sns.barplot(data=df_city, x="City", y="TotalSales", ax=ax1)
    ax1.set_title("Total Sales by City")
    plt.ticklabel_format(axis='y', style='plain')
    ax1.tick_params(axis='x', rotation=45)

    ax2 = fig.add_subplot(gs[0, 1])
    df_month["YearMonth"] = df_month["Year"].astype(str) + "-" + df_month["Month"]
    sns.lineplot(data=df_month.reset_index(), x="YearMonth", y="TotalSales", marker="o", ax=ax2)
    ax2.set_title("Monthly Sales Trend")
    plt.ticklabel_format(axis='y', style='plain')
    ax2.tick_params(axis='x', rotation=45)

    ax3 = fig.add_subplot(gs[1, 0])
    sns.barplot(data=df_product.reset_index(), x="ProductName", y="TotalSales", ax=ax3)
    ax3.set_title("Top 10 Products by Sales")
    plt.ticklabel_format(axis='y', style='plain')
    ax3.tick_params(axis='x', rotation=45)

    ax4 = fig.add_subplot(gs[1, 1])
    sns.barplot(data=df_state.reset_index(), x="State", y="TotalSales", ax=ax4)
    ax4.set_title("Total Sales by State")
    plt.ticklabel_format(axis='y', style='plain')
    ax4.tick_params(axis='x', rotation=45)

    ax5 = fig.add_subplot(gs[2, :])
    sns.lineplot(data=df_december.reset_index(), x="DayOfMonth", y="TotalSales", marker="o", ax=ax5)
    ax5.set_title("Total Sales in December")
    ax5.set_ylim(125000, 175000)

    plt.savefig('dashboard.png')
    plt.tight_layout()
    plt.show()

# ========== SALES PLOTS ==========
def sales_by_city(df):
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    sns.barplot(data=df, x="City", y="TotalSales")
    plt.title("Total Sales by City")
    plt.xticks(rotation=45)
    plt.ticklabel_format(axis='y', style='plain')
    plt.savefig('sales_by_city.png')
    plt.tight_layout()
    plt.show()

def sales_by_month(df):
    df["YearMonth"] = df["Year"].astype(str) + "-" + df["Month"]
    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    sns.lineplot(data = df, x="YearMonth", y="TotalSales", marker="o")
    plt.title("Monthly Sales Trend")
    plt.xticks(rotation=45)
    plt.ticklabel_format(axis='y', style='plain')
    plt.savefig('sales_by_month.png')
    plt.tight_layout()
    plt.show()

def sales_by_product(df):
    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    sns.barplot(data=df, x="ProductName", y="TotalSales")
    plt.title("Top 10 Products by Sales")
    plt.xticks(rotation=45)
    plt.ticklabel_format(axis='y', style='plain')
    plt.savefig('sales_by_product.png')
    plt.tight_layout()
    plt.show()

def sales_by_state(df):
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    sns.barplot(data=df, x="State", y="TotalSales")
    plt.title("Total Sales by State")
    plt.xticks(rotation=45)
    plt.ticklabel_format(axis='y', style='plain')
    plt.savefig('sales_by_state.png')
    plt.tight_layout()
    plt.show()

def sales_in_december(df):
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    sns.lineplot(data=df.reset_index(), x="DayOfMonth", y="TotalSales", marker="o")
    plt.title("Total Sales in December")
    plt.xticks(rotation=45)
    plt.ticklabel_format(axis='y', style='plain')
    plt.ylim(125000, 175000)
    plt.savefig('sales_by_state.png')
    plt.tight_layout()
    plt.show()
    
# ========== ORDERS DASHBOARD ==========
def orders_dashboard():
    conn = sqlite3.connect("sales.db")

    # Load views
    df_city = pd.read_sql_query("SELECT * FROM analysis_by_city;", conn)
    df_month = pd.read_sql_query("SELECT * FROM analysis_by_month;", conn)
    df_state = pd.read_sql_query("SELECT * FROM analysis_by_state;", conn)
    df_product = pd.read_sql_query("SELECT * FROM analysis_by_product;", conn)
    df_december = pd.read_sql_query("SELECT * FROM analysis_of_december;", conn)

    conn.close()
    sns.set_style("whitegrid")

    fig = plt.figure(figsize=(20, 15))
    gs = GridSpec(3, 2)

    ax1 = fig.add_subplot(gs[0, 0])
    sns.barplot(data=df_city, x="City", y="TotalOrders", ax=ax1)
    ax1.set_title("Total Orders by City")
    plt.ticklabel_format(axis='y', style='plain')
    ax1.tick_params(axis='x', rotation=45)

    ax2 = fig.add_subplot(gs[0, 1])
    df_month["YearMonth"] = df_month["Year"].astype(str) + "-" + df_month["Month"]
    sns.lineplot(data=df_month.reset_index(), x="YearMonth", y="TotalOrders", marker="o", ax=ax2)
    ax2.set_title("Monthly Orders Trend")
    plt.ticklabel_format(axis='y', style='plain')
    ax2.tick_params(axis='x', rotation=45)

    ax3 = fig.add_subplot(gs[1, 0])
    sns.barplot(data=df_product.reset_index(), x="ProductName", y="TotalOrders", ax=ax3)
    ax3.set_title("Top 10 Products by Orders")
    plt.ticklabel_format(axis='y', style='plain')
    ax3.tick_params(axis='x', rotation=45)

    ax4 = fig.add_subplot(gs[1, 1])
    sns.barplot(data=df_state.reset_index(), x="State", y="TotalOrders", ax=ax4)
    ax4.set_title("Total Orders by State")
    plt.ticklabel_format(axis='y', style='plain')
    ax4.tick_params(axis='x', rotation=45)

    ax5 = fig.add_subplot(gs[2, :])
    sns.lineplot(data=df_december.reset_index(), x="DayOfMonth", y="TotalOrders", marker="o", ax=ax5)
    ax5.set_title("Total Orders in December")
    ax5.set_ylim(125000, 175000)

    plt.savefig('Orders_dashboard.png')
    plt.tight_layout()
    plt.show()


# ========== ORDERZ PLOTS ==========
def Total_Orders_by_city(df):
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    sns.barplot(data=df, x="City", y="TotalOrders")
    plt.title("Total Orders by City")
    plt.xticks(rotation=45)
    plt.ticklabel_format(axis='y', style='plain')
    plt.savefig('Orders_by_city.png')
    plt.tight_layout()
    plt.show()

def Total_orders_by_month(df):
    df["YearMonth"] = df["Year"].astype(str) + "-" + df["Month"]
    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    sns.lineplot(data=df, x="YearMonth", y="TotalOrders", marker="o")
    plt.title("Monthly Orders Trend")
    plt.xticks(rotation=45)
    plt.ticklabel_format(axis='y', style='plain')
    plt.savefig('Orders_by_month.png')
    plt.tight_layout()
    plt.show()


def Total_orders_by_product(df):
    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    sns.barplot(data=df, x="ProductName", y="TotalOrders")
    plt.title("Top 10 Products by Orders")
    plt.xticks(rotation=45)
    plt.ticklabel_format(axis='y', style='plain')
    plt.savefig('Orders_by_product.png')
    plt.tight_layout()
    plt.show()


def Total_orders_by_state(df):
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    sns.barplot(data=df, x="State", y="TotalOrders")
    plt.title("Total Orders by State")
    plt.xticks(rotation=45)
    plt.ticklabel_format(axis='y', style='plain')
    plt.savefig('Orders_by_state.png')
    plt.tight_layout()
    plt.show()


def Total_orders_in_december(df):
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    sns.lineplot(data=df.reset_index(), x="DayOfMonth", y="TotalOrders", marker="o")
    plt.title("Total Orders in December")
    plt.xticks(rotation=45)
    plt.ticklabel_format(axis='y', style='plain')
    plt.ylim(125000, 175000)
    plt.savefig('Orders_by_state.png')
    plt.tight_layout()
    plt.show()

# ========== MENU ==========
def main():
    conn = sqlite3.connect("sales.db")

    while True:
        print("\nChoose a report:")
        print("1. Order Details")
        print("2. Order Details(PLOTS)")
        print("3. Sales Details")
        print("4. Exit")

        choice_1 = int(input("Enter your choice (1-4): "))

        if choice_1 == 1:
            query = "SELECT * FROM order_details;"
            df = pd.read_sql_query(query, conn)
            print(df.head())

        elif choice_1 == 2:
            print("2. Total orders by City")
            print("3. Total orders by month")
            print("4. Total orders by State")
            print("5. Total orders by Product")
            print("6. Total orders in December")
            print("7. Total orders Dashboard")

            choice = int(input("Enter your choice (2-7): "))

            if choice == 1:
                df = pd.read_sql_query("SELECT * FROM analysis_by_city;", conn)
                Total_Orders_by_city(df)

            elif choice == 2:
                df = pd.read_sql_query("SELECT * FROM analysis_by_month;", conn)
                Total_orders_by_month(df)

            elif choice == 3:
                df = pd.read_sql_query("SELECT * FROM analysis_by_state;", conn)
                Total_orders_by_state(df)

            elif choice == 4:
                df = pd.read_sql_query("SELECT * FROM analysis_by_product;", conn)
                Total_orders_by_product(df)

            elif choice == 5:
                df = pd.read_sql_query("SELECT * FROM analysis_of_december;", conn)
                Total_orders_in_december(df)

            elif choice == 6:
                orders_dashboard()

        elif choice_1 == 3:
            print("1. Sales by City")
            print("2. Sales by month")
            print("3. Sales by State")
            print("4. Sales by Product")
            print("5. Sales in December")
            print("6. Sales Dashboard")

            choice = int(input("Enter your choice (2-7): "))

            if choice == 1:
                df = pd.read_sql_query("SELECT * FROM analysis_by_city;", conn)
                Total_Orders_by_city(df)

            elif choice == 2:
                df = pd.read_sql_query("SELECT * FROM analysis_by_month;", conn)
                Total_orders_by_month(df)

            elif choice == 3:
                df = pd.read_sql_query("SELECT * FROM analysis_by_state;", conn)
                Total_orders_by_state(df)

            elif choice == 4:
                df = pd.read_sql_query("SELECT * FROM analysis_by_product;", conn)
                Total_orders_by_product(df)

            elif choice == 5:
                df = pd.read_sql_query("SELECT * FROM analysis_of_december;", conn)
                Total_orders_in_december(df)

            elif choice == 6:
                orders_dashboard()


        elif choice_1 == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")

    conn.close()

# Run the program
if __name__ == "__main__":
    main()
