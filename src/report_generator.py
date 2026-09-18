from datetime import datetime


def generate_management_report(data):
    """Generate an automated management report from cleaned sales data."""

    total_sales = data["Net_Sales"].sum()
    total_orders = data["Transaction_ID"].nunique()
    total_quantity = data["Quantity"].sum()
    total_discount = data["Discount_Amount"].sum()

    average_order_value = total_sales / total_orders

    completed_orders = (
        data[data["Order_Status"] == "Completed"]["Transaction_ID"]
        .nunique()
    )

    cancelled_orders = (
        data[data["Order_Status"] == "Cancelled"]["Transaction_ID"]
        .nunique()
    )

    # Top product
    product_sales = (
        data.groupby("Product_Name")["Net_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    top_product = product_sales.index[0]
    top_product_sales = product_sales.iloc[0]

    # Top branch
    branch_sales = (
        data.groupby("Branch")["Net_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    top_branch = branch_sales.index[0]
    top_branch_sales = branch_sales.iloc[0]

    # Top payment method
    payment_sales = (
        data.groupby("Payment_Method")["Net_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    top_payment_method = payment_sales.index[0]

    # Cancellation rate
    cancellation_rate = (
        cancelled_orders / total_orders
    ) * 100

    # Create report
    report = f"""
============================================================
       ENTERPRISE SALES MANAGEMENT REPORT
============================================================

Generated On: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

------------------------------------------------------------
EXECUTIVE SUMMARY
------------------------------------------------------------

Total Sales          : ₹{total_sales:,.2f}
Total Orders         : {total_orders}
Total Quantity Sold  : {total_quantity}
Total Discount       : ₹{total_discount:,.2f}
Average Order Value  : ₹{average_order_value:,.2f}

Completed Orders     : {completed_orders}
Cancelled Orders     : {cancelled_orders}
Cancellation Rate    : {cancellation_rate:.2f}%

------------------------------------------------------------
KEY FINDINGS
------------------------------------------------------------

1. Top Performing Product
   Product: {top_product}
   Revenue: ₹{top_product_sales:,.2f}

2. Top Performing Branch
   Branch: {top_branch}
   Revenue: ₹{top_branch_sales:,.2f}

3. Most Used Payment Method
   Payment Method: {top_payment_method}

4. Discount Performance
   Total Discount Given: ₹{total_discount:,.2f}

------------------------------------------------------------
RECOMMENDATIONS
------------------------------------------------------------

1. Monitor the performance of the highest-revenue products
   and maintain sufficient stock.

2. Analyze the sales practices of high-performing branches
   and identify useful practices that can be applied elsewhere.

3. Monitor payment-method usage to improve customer
   payment convenience.

4. Review cancelled transactions regularly and identify
   possible reasons for cancellations.

5. Monitor discount usage to ensure that discounts support
   sales without unnecessarily reducing revenue.

------------------------------------------------------------
REPORT END
------------------------------------------------------------
"""

    # Save report
    with open(
        "reports/management_report.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report)

    print("\nManagement report generated successfully!")
    print("Saved to: reports/management_report.txt")

    return report

