import os
import pandas as pd

from src.logger import log_error
from src.validator import validate_data
from src.cleaner import clean_data
from src.transformer import transform_data
from src.sales_analysis import sales_summary
from src.product_analysis import product_summary
from src.branch_analysis import branch_summary
from src.customer_analysis import customer_summary
from src.payment_analysis import payment_summary
from src.anomaly_detector import detect_anomalies
from src.time_analysis import time_summary
from src.database import save_to_database, show_branch_sales, show_top_products
from src.visualizations import (
    monthly_sales_chart,
    branch_sales_chart,
    top_products_chart,
    payment_method_chart,
    category_sales_chart,
    cancellation_rate_chart,
    discount_vs_sales_chart
)
from src.discount_analysis import discount_summary
from src.customer_segmentation import customer_segments
from src.report_generator import generate_management_report


def load_csv(file_path):
    """Load a CSV file and return a DataFrame."""
    try:
        data = pd.read_csv(file_path)
        print(f"Loaded successfully: {file_path}")
        return data

    except Exception as error:
        print(f"Error loading file: {error}")
        log_error(error)
        return None


def run_pipeline():
    """Run the complete sales processing pipeline."""

    # Find CSV files automatically
    raw_folder = "data/raw"

    csv_files = [
        file for file in os.listdir(raw_folder)
        if file.lower().endswith(".csv")
    ]

    if not csv_files:
        print("No CSV file found in data/raw")
        return

    elif len(csv_files) == 1:
        file_path = os.path.join(raw_folder, csv_files[0])
        print(f"CSV file detected: {file_path}")

    else:
        print("\nMultiple CSV files found:")

        for index, file in enumerate(csv_files, start=1):
            print(f"{index}. {file}")

        choice = int(input("\nEnter the CSV file number: "))

        selected_file = csv_files[choice - 1]
        file_path = os.path.join(raw_folder, selected_file)

        print(f"\nSelected CSV file: {file_path}")

    sales_data = load_csv(file_path)

    if sales_data is None:
        return

    print("\nSales Data:")
    print(sales_data)

    # Validate the data
    validate_data(sales_data)

    # Clean the data
    cleaned_data = clean_data(sales_data)
    cleaned_data = transform_data(cleaned_data)

    # Sales analysis
    sales_summary(cleaned_data)

    # Product analysis
    product_summary(cleaned_data)

    # Branch analysis
    branch_result, cancellation_result = branch_summary(cleaned_data)

    # Customer analysis
    customer_summary(cleaned_data)
    customer_segments(cleaned_data)

    # Payment analysis
    payment_summary(cleaned_data)

    # Anomaly detection
    detect_anomalies(cleaned_data)

    # Time analysis
    time_summary(cleaned_data)

    # Database
    save_to_database(cleaned_data)
    show_branch_sales()
    show_top_products()

    # Visualizations
    monthly_sales_chart(cleaned_data)
    branch_sales_chart(cleaned_data)
    top_products_chart(cleaned_data)
    payment_method_chart(cleaned_data)
    category_sales_chart(cleaned_data)
    cancellation_rate_chart(cancellation_result)
    discount_vs_sales_chart(cleaned_data)

    # Discount analysis
    discount_summary(cleaned_data)

    # Management report
    generate_management_report(cleaned_data)

    print("\nCleaned Data:")
    print(cleaned_data)

    # Save cleaned data
    cleaned_data.to_csv(
        "data/processed/cleaned_sales.csv",
        index=False
    )

    print("\nCleaned data saved successfully!")


if __name__ == "__main__":
    run_pipeline()