def sales_summary(data):
    """Generate overall sales summary."""

    print("\n--- SALES SUMMARY ---")

    total_sales = data["Net_Sales"].sum()
    total_orders = data["Transaction_ID"].nunique()
    total_quantity = data["Quantity"].sum()
    total_discount = data["Discount_Amount"].sum()

    if total_orders > 0:
        average_order_value = total_sales / total_orders
    else:
        average_order_value = 0

    completed_orders = (
        data["Order_Status"] == "Completed"
    ).sum()

    cancelled_orders = (
        data["Order_Status"] == "Cancelled"
    ).sum()

    print(f"Total Sales: ₹{total_sales:,.2f}")
    print(f"Total Orders: {total_orders}")
    print(f"Total Quantity Sold: {total_quantity}")
    print(f"Total Discount: ₹{total_discount:,.2f}")
    print(f"Average Order Value: ₹{average_order_value:,.2f}")
    print(f"Completed Orders: {completed_orders}")
    print(f"Cancelled Orders: {cancelled_orders}")

    return {
        "total_sales": total_sales,
        "total_orders": total_orders,
        "total_quantity": total_quantity,
        "total_discount": total_discount,
        "average_order_value": average_order_value,
        "completed_orders": completed_orders,
        "cancelled_orders": cancelled_orders
    }