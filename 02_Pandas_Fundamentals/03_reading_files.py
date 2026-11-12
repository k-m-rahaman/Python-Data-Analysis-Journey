"""
Topic: Reading and Writing CSV and JSON Files with Pandas

Generate reproducible example orders, save them in a temporary
folder, load both formats, and verify data integrity.
"""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd


REQUIRED_COLUMNS = {
    "order_id",
    "product",
    "quantity",
    "unit_price",
    "order_date",
}


def create_sample_orders() -> pd.DataFrame:
    """Build sample order records with zero-padded identifiers."""
    return pd.DataFrame(
        {
            "order_id": ["001", "002", "003"],
            "product": ["Notebook", "Headphones", "USB Cable"],
            "quantity": [3, 1, 4],
            "unit_price": [50.0, 1200.0, 150.0],
            "order_date": [
                "2026-10-01",
                "2026-10-02",
                "2026-10-03",
            ],
        }
    )


def write_sample_files(
    orders: pd.DataFrame,
    directory: Path,
) -> tuple[Path, Path]:
    """Export sample orders to CSV and JSON files."""
    csv_path = directory / "sample_orders.csv"
    json_path = directory / "sample_orders.json"

    # Save CSV.
    orders.to_csv(csv_path, index=False, encoding="utf-8")

    # Save JSON.
    with json_path.open("w", encoding="utf-8") as file:
        json.dump(
            orders.to_dict(orient="records"),
            file,
            indent=2,
        )

    return csv_path, json_path


def read_and_validate(
    csv_path: Path,
    json_path: Path,
) -> None:
    """Load the files, validate structure, and compute revenue."""

    # Import the CSV dataset.
    csv_orders = pd.read_csv(
        csv_path,
        dtype={"order_id": "string"},
        parse_dates=["order_date"],
    )

    # Import the JSON dataset.
    json_orders = pd.read_json(
        json_path,
        orient="records",
        dtype={"order_id": "string"},
        convert_dates=["order_date"],
    )

    # Validate expected columns.
    for label, frame in [
        ("CSV", csv_orders),
        ("JSON", json_orders),
    ]:
        missing_columns = REQUIRED_COLUMNS - set(frame.columns)

        if missing_columns:
            raise ValueError(
                f"{label} missing columns: {sorted(missing_columns)}"
            )

        if frame["order_id"].isna().any():
            raise ValueError(
                f"{label} contains missing order IDs."
            )

    # Calculate revenue.
    csv_orders["revenue"] = (
        csv_orders["quantity"] * csv_orders["unit_price"]
    )

    print("=== Reading CSV ===")
    print(csv_orders.to_string(index=False))

    print(
        "Order ID preserved:",
        csv_orders.loc[0, "order_id"]
    )

    print(
        "Date column type:",
        csv_orders["order_date"].dtype
    )

    print(
        "Total revenue:",
        csv_orders["revenue"].sum()
    )

    print("\n=== Reading JSON ===")

    selected_columns = [
        "order_id",
        "product",
        "quantity",
    ]

    print(
        json_orders[selected_columns].to_string(index=False)
    )

    print(
        "JSON rows loaded:",
        len(json_orders)
    )

    print(
        "Both formats have same order IDs:",
        csv_orders["order_id"].tolist()
        == json_orders["order_id"].tolist()
    )


def main() -> None:
    """Create sample files and demonstrate reading them."""
    sample_orders = create_sample_orders()

    # Temporary files are automatically deleted afterward.
    with TemporaryDirectory(
        prefix="pandas_files_"
    ) as temp_dir:

        csv_path, json_path = write_sample_files(
            sample_orders,
            Path(temp_dir),
        )

        read_and_validate(csv_path, json_path)

    print(
        "\nTemporary sample files cleaned up automatically."
    )


if __name__ == "__main__":
    main()