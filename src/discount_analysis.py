def discount_summary(data):
    """Analyze discount performance."""

    print("\n--- DISCOUNT ANALYSIS ---")

    total_discount = data["Discount_Amount"].sum()

    # Discount is stored as decimal (0.05 = 5%)
    average_discount = data["Discount"].mean() * 100

    high_discount_orders = (
        data[data["Discount"] > 0.20]["Transaction_ID"].nunique()
    )

    print(f"Total Discount Given: ₹{total_discount:,.2f}")
    print(f"Average Discount: {average_discount:.2f}%")
    print(f"High Discount Orders (>20%): {high_discount_orders}")

    return {
        "total_discount": total_discount,
        "average_discount": average_discount,
        "high_discount_orders": high_discount_orders
    }