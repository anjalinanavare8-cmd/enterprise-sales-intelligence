def branch_summary(data):
    """Analyze branch performance."""

    print("\n--- BRANCH ANALYSIS ---")

    branch_analysis = data.groupby("Branch").agg(
        Total_Sales=("Net_Sales", "sum"),
        Total_Orders=("Transaction_ID", "nunique"),
        Total_Quantity=("Quantity", "sum")
    )

    branch_analysis["Average_Order_Value"] = (
        branch_analysis["Total_Sales"] /
        branch_analysis["Total_Orders"]
    )

    branch_analysis = branch_analysis.sort_values(
        "Total_Sales",
        ascending=False
    )

    print("\nBranch Performance:")
    print(branch_analysis)

    # Cancellation analysis by branch
    cancellation_analysis = data.groupby("Branch").agg(
        Total_Orders=("Transaction_ID", "nunique"),
        Cancelled_Orders=("Order_Status", lambda x: (x == "Cancelled").sum())
    )

    cancellation_analysis["Cancellation_Rate"] = (
        cancellation_analysis["Cancelled_Orders"] /
        cancellation_analysis["Total_Orders"]
    ) * 100

    print("\nCancellation Rate by Branch:")
    print(cancellation_analysis)

    return branch_analysis, cancellation_analysis