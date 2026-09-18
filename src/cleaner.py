import pandas as pd
import os


def clean_data(data):
    """Clean sales data and save rejected records separately."""

    print("\n--- DATA CLEANING STARTED ---")

    # Create rejected records folder
    os.makedirs("data/rejected", exist_ok=True)

    # Make a copy so the original data is not modified
    data = data.copy()

    rejected_records = []

    # --------------------------------------------------
    # Check duplicate transactions
    # --------------------------------------------------
    duplicate_mask = data["Transaction_ID"].duplicated(keep="first")

    if duplicate_mask.any():
        duplicate_data = data[duplicate_mask].copy()
        duplicate_data["Rejection_Reason"] = "Duplicate Transaction ID"
        rejected_records.append(duplicate_data)

    # --------------------------------------------------
    # Convert dates
    # --------------------------------------------------
    converted_dates = pd.to_datetime(
        data["Transaction_Date"],
        errors="coerce"
    )

    invalid_date_mask = converted_dates.isna()

    if invalid_date_mask.any():
        invalid_dates = data[invalid_date_mask].copy()
        invalid_dates["Rejection_Reason"] = "Invalid Date"
        rejected_records.append(invalid_dates)

    data["Transaction_Date"] = converted_dates

    # --------------------------------------------------
    # Invalid quantity
    # --------------------------------------------------
    invalid_quantity_mask = data["Quantity"] <= 0

    if invalid_quantity_mask.any():
        invalid_quantity = data[invalid_quantity_mask].copy()
        invalid_quantity["Rejection_Reason"] = "Invalid Quantity"
        rejected_records.append(invalid_quantity)

    # --------------------------------------------------
    # Invalid price
    # --------------------------------------------------
    invalid_price_mask = data["Unit_Price"] <= 0

    if invalid_price_mask.any():
        invalid_price = data[invalid_price_mask].copy()
        invalid_price["Rejection_Reason"] = "Invalid Unit Price"
        rejected_records.append(invalid_price)

    # --------------------------------------------------
    # Invalid discount
    # --------------------------------------------------
    invalid_discount_mask = (
        (data["Discount"] < 0) |
        (data["Discount"] > 1)
    )

    if invalid_discount_mask.any():
        invalid_discount = data[invalid_discount_mask].copy()
        invalid_discount["Rejection_Reason"] = "Invalid Discount"
        rejected_records.append(invalid_discount)

    # --------------------------------------------------
    # Save rejected records
    # --------------------------------------------------
    if rejected_records:

        rejected_data = pd.concat(
            rejected_records,
            ignore_index=True
        )

        # Remove duplicate rejected rows
        rejected_data = rejected_data.drop_duplicates(
            subset=["Transaction_ID", "Rejection_Reason"]
        )

        rejected_data.to_csv(
            "data/rejected/rejected_records.csv",
            index=False
        )

        print(
            f"Rejected records saved: {len(rejected_data)}"
        )

    else:

        # Create an empty rejected-record file
        empty_rejected = data.head(0).copy()
        empty_rejected["Rejection_Reason"] = ""

        empty_rejected.to_csv(
            "data/rejected/rejected_records.csv",
            index=False
        )

        print("No rejected records found.")

    # --------------------------------------------------
    # Remove invalid records from clean dataset
    # --------------------------------------------------

    valid_mask = (
        ~duplicate_mask &
        ~invalid_date_mask &
        (data["Quantity"] > 0) &
        (data["Unit_Price"] > 0) &
        (data["Discount"] >= 0) &
        (data["Discount"] <= 1)
    )

    data = data[valid_mask].copy()

    # --------------------------------------------------
    # Clean text columns
    # --------------------------------------------------

    data["Branch"] = (
        data["Branch"]
        .str.strip()
        .str.title()
    )

    data["Payment_Method"] = (
        data["Payment_Method"]
        .str.strip()
        .str.title()
    )

    data["Order_Status"] = (
        data["Order_Status"]
        .str.strip()
        .str.title()
    )

    print(f"Records after cleaning: {len(data)}")

    return data