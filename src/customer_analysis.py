def customer_summary(data):
    """Analyze customer performance."""

    print("\n--- CUSTOMER ANALYSIS ---")

    customer_analysis = data.groupby(
        ["Customer_ID", "Customer_Name"]
    ).agg(
        Total_Orders=("Transaction_ID", "nunique"),
        Total_Sales=("Net_Sales", "sum"),
        Total_Quantity=("Quantity", "sum")
    )

    customer_analysis["Average_Spend"] = (
        customer_analysis["Total_Sales"] /
        customer_analysis["Total_Orders"]
    )

    print("\nCustomer Performance:")
    print(customer_analysis)

    repeat_customers = (
        customer_analysis["Total_Orders"] > 1
    ).sum()

    one_time_customers = (
        customer_analysis["Total_Orders"] == 1
    ).sum()

    print(f"\nRepeat Customers: {repeat_customers}")
    print(f"One-Time Customers: {one_time_customers}")

    return customer_analysis