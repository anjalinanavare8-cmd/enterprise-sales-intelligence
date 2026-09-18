def product_summary(data):
    """Analyze product performance."""

    print("\n--- PRODUCT ANALYSIS ---")

    product_sales = (
        data.groupby("Product_Name")["Net_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    product_quantity = (
        data.groupby("Product_Name")["Quantity"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nTop 10 Products by Revenue:")
    print(product_sales.head(10))

    print("\nTop 10 Products by Quantity Sold:")
    print(product_quantity.head(10))

    return product_sales, product_quantity