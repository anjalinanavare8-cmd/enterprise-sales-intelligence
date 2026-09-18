import pandas as pd


def transform_data(data):
    """Calculate sales values and add useful analysis columns."""

    print("\n--- SALES CALCULATION STARTED ---")

    # Calculate Gross Sales
    data["Gross_Sales"] = data["Quantity"] * data["Unit_Price"]

    # Calculate Discount Amount
    data["Discount_Amount"] = (
        data["Gross_Sales"] * data["Discount"] / 100
    )

    # Calculate Net Sales
    data["Net_Sales"] = (
        data["Gross_Sales"] - data["Discount_Amount"]
    )

    # Add time-based columns
    data["Year"] = data["Transaction_Date"].dt.year
    data["Month"] = data["Transaction_Date"].dt.month
    data["Month_Name"] = data["Transaction_Date"].dt.strftime("%B")
    data["Day"] = data["Transaction_Date"].dt.day
    data["Weekday"] = data["Transaction_Date"].dt.strftime("%A")

    print("Sales calculations completed!")

    return data