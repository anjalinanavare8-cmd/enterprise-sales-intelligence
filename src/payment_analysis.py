def payment_summary(data):
    """Analyze payment method performance."""

    print("\n--- PAYMENT ANALYSIS ---")

    payment_analysis = data.groupby("Payment_Method").agg(
        Total_Sales=("Net_Sales", "sum"),
        Total_Orders=("Transaction_ID", "nunique"),
        Total_Quantity=("Quantity", "sum")
    )

    payment_analysis = payment_analysis.sort_values(
        "Total_Sales",
        ascending=False
    )

    print("\nPayment Method Performance:")
    print(payment_analysis)

    return payment_analysis