import sqlite3


def save_to_database(data, database_name="sales.db"):
    """Save processed sales data into SQLite database."""

    print("\n--- DATABASE STORAGE ---")

    try:
        connection = sqlite3.connect(database_name)

        data.to_sql(
            "transactions",
            connection,
            if_exists="replace",
            index=False
        )

        cursor = connection.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM transactions"
        )

        total_records = cursor.fetchone()[0]

        print("Data saved successfully to SQLite database!")
        print(f"Records stored in database: {total_records}")

        cursor.execute(
            "SELECT Transaction_ID, Product_Name, Net_Sales "
            "FROM transactions LIMIT 5"
        )

        records = cursor.fetchall()

        print("\nSample records from database:")

        for record in records:
            print(record)

        connection.close()

    except Exception as error:
        print(f"Database error: {error}")


def show_branch_sales(database_name="sales.db"):
    """Show branch-wise sales using SQL."""

    print("\n--- SQL BRANCH SALES QUERY ---")

    try:
        connection = sqlite3.connect(database_name)

        query = """
        SELECT Branch,
               SUM(Net_Sales) AS Total_Sales
        FROM transactions
        GROUP BY Branch
        ORDER BY Total_Sales DESC;
        """

        result = connection.execute(query).fetchall()

        print("\nBranch-wise Sales:")

        for row in result:
            print(f"Branch: {row[0]} | Sales: ₹{row[1]:,.2f}")

        connection.close()

    except Exception as error:
        print(f"SQL query error: {error}")


def show_top_products(database_name="sales.db"):
    """Show top products by revenue using SQL."""

    print("\n--- SQL TOP PRODUCTS QUERY ---")

    try:
        connection = sqlite3.connect(database_name)

        query = """
        SELECT Product_Name,
               SUM(Net_Sales) AS Total_Sales
        FROM transactions
        GROUP BY Product_Name
        ORDER BY Total_Sales DESC
        LIMIT 5;
        """

        result = connection.execute(query).fetchall()

        print("\nTop 5 Products by Revenue:")

        for row in result:
            print(f"Product: {row[0]} | Sales: ₹{row[1]:,.2f}")

        connection.close()

    except Exception as error:
        print(f"SQL query error: {error}")