import matplotlib.pyplot as plt


def monthly_sales_chart(data):
    monthly_sales = data.groupby("Month_Name")["Net_Sales"].sum()

    monthly_sales.plot(kind="bar", figsize=(8, 5))

    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Net Sales")
    plt.tight_layout()

    plt.savefig("visualizations/monthly_sales.png")
    plt.show()

    print("Monthly sales chart saved successfully!")


def branch_sales_chart(data):
    branch_sales = (
        data.groupby("Branch")["Net_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    branch_sales.plot(kind="bar", figsize=(8, 5))

    plt.title("Sales by Branch")
    plt.xlabel("Branch")
    plt.ylabel("Net Sales")
    plt.tight_layout()

    plt.savefig("visualizations/branch_sales.png")
    plt.show()

    print("Branch sales chart saved successfully!")


def top_products_chart(data):
    product_sales = (
        data.groupby("Product_Name")["Net_Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    product_sales.plot(kind="bar", figsize=(10, 5))

    plt.title("Top 10 Products by Revenue")
    plt.xlabel("Product")
    plt.ylabel("Net Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("visualizations/top_products.png")
    plt.show()

    print("Top products chart saved successfully!")


def payment_method_chart(data):
    payment_sales = (
        data.groupby("Payment_Method")["Net_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    payment_sales.plot(kind="bar", figsize=(8, 5))

    plt.title("Sales by Payment Method")
    plt.xlabel("Payment Method")
    plt.ylabel("Net Sales")
    plt.tight_layout()

    plt.savefig("visualizations/payment_methods.png")
    plt.show()

    print("Payment method chart saved successfully!")


def category_sales_chart(data):
    category_sales = (
        data.groupby("Category")["Net_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    category_sales.plot(kind="bar", figsize=(8, 5))

    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Net Sales")
    plt.tight_layout()

    plt.savefig("visualizations/category_sales.png")
    plt.show()

    print("Category sales chart saved successfully!")


def cancellation_rate_chart(cancellation_data):
    cancellation_rate = cancellation_data["Cancellation_Rate"]

    cancellation_rate.plot(kind="bar", figsize=(8, 5))

    plt.title("Cancellation Rate by Branch")
    plt.xlabel("Branch")
    plt.ylabel("Cancellation Rate (%)")
    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.savefig("visualizations/cancellation_rate_by_branch.png")
    plt.show()

    print("Cancellation rate chart saved successfully!")


def discount_vs_sales_chart(data):
    plt.figure(figsize=(8, 5))

    plt.scatter(
        data["Discount"] * 100,
        data["Net_Sales"]
    )

    plt.title("Discount vs Sales")
    plt.xlabel("Discount (%)")
    plt.ylabel("Net Sales (₹)")
    plt.tight_layout()

    plt.savefig("visualizations/discount_vs_sales.png")
    plt.show()

    print("Discount vs Sales chart saved successfully!")

