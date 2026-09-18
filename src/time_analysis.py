def time_summary(data):
    """Analyze sales based on time."""

    print("\n--- TIME ANALYSIS ---")

    monthly_sales = (
        data.groupby(["Year", "Month", "Month_Name"])["Net_Sales"]
        .sum()
        .reset_index()
        .sort_values(["Year", "Month"])
    )

    print("\nMonthly Sales:")
    print(monthly_sales)

    weekday_sales = (
        data.groupby("Weekday")["Net_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nSales by Weekday:")
    print(weekday_sales)

    return monthly_sales, weekday_sales