import pandas as pd
import os


def validate_data(data):
    """Check the sales data for common data-quality problems."""

    print("\n--- DATA QUALITY REPORT ---")

    os.makedirs("reports", exist_ok=True)

    report = []

    # Missing values
    missing_values = data.isnull().sum()
    print("\nMissing Values:")
    print(missing_values)

    report.append("DATA QUALITY REPORT")
    report.append("=" * 30)
    report.append("\nMissing Values:")
    report.append(str(missing_values))

    # Duplicate transactions
    duplicates = data["Transaction_ID"].duplicated().sum()
    print(f"\nDuplicate Transactions: {duplicates}")
    report.append(f"\nDuplicate Transactions: {duplicates}")

    # Invalid quantities
    invalid_quantity = (data["Quantity"] <= 0).sum()
    print(f"Invalid Quantity Records: {invalid_quantity}")
    report.append(f"Invalid Quantity Records: {invalid_quantity}")

    # Invalid prices
    invalid_price = (data["Unit_Price"] <= 0).sum()
    print(f"Invalid Price Records: {invalid_price}")
    report.append(f"Invalid Price Records: {invalid_price}")

    # Invalid discounts
    invalid_discount = (
        (data["Discount"] < 0) |
        (data["Discount"] > 1)
    ).sum()

    print(f"Invalid Discount Records: {invalid_discount}")
    report.append(f"Invalid Discount Records: {invalid_discount}")

    # Invalid dates
    dates = pd.to_datetime(
        data["Transaction_Date"],
        errors="coerce"
    )

    invalid_dates = dates.isnull().sum()

    print(f"Invalid Date Records: {invalid_dates}")
    report.append(f"Invalid Date Records: {invalid_dates}")

    # Save report
    with open(
        "reports/data_quality_report.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write("\n".join(report))

    print("\nData quality report saved successfully!")

    return data


if __name__ == "__main__":
    file_path = "data/raw/sales_branch1.csv"
    data = pd.read_csv(file_path)
    validate_data(data)