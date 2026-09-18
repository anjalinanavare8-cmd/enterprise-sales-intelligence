def customer_segments(data):
    """Create simple rule-based customer segments."""

    print("\n--- CUSTOMER SEGMENTATION ---")

    customer_data = data.groupby(
        ["Customer_ID", "Customer_Name"]
    ).agg(
        Total_Orders=("Transaction_ID", "nunique"),
        Total_Sales=("Net_Sales", "sum")
    ).reset_index()

    def segment_customer(row):
        if row["Total_Sales"] >= 50000:
            return "High Value"
        elif row["Total_Orders"] > 1:
            return "Repeat Customer"
        else:
            return "One-Time Customer"

    customer_data["Customer_Segment"] = customer_data.apply(
        segment_customer,
        axis=1
    )

    print("\nCustomer Segments:")
    print(customer_data)

    print("\nSegment Count:")
    print(customer_data["Customer_Segment"].value_counts())

    return customer_data