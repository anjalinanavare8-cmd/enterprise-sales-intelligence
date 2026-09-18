import os


def detect_anomalies(data):
    """Detect unusual sales records and save an anomaly report."""

    print("\n--- ANOMALY DETECTION ---")

    anomalies = data[
        (data["Quantity"] > 100) |
        (data["Discount"] > 50) |
        (data["Net_Sales"] > 500000)
    ].copy()

    print(f"\nAnomalies Found: {len(anomalies)}")

    os.makedirs("reports", exist_ok=True)

    if len(anomalies) > 0:
        print("\nAnomalous Records:")
        print(anomalies[
            [
                "Transaction_ID",
                "Customer_Name",
                "Product_Name",
                "Quantity",
                "Discount",
                "Net_Sales"
            ]
        ])

        anomalies.to_csv(
            "reports/anomaly_report.csv",
            index=False
        )

        print("Anomaly report saved successfully!")

    else:
        print("No anomalies detected.")

        anomalies.to_csv(
            "reports/anomaly_report.csv",
            index=False
        )

        print("Empty anomaly report saved successfully!")

    return anomalies