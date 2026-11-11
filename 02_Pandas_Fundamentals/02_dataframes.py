"""
Topic: Pandas DataFrame Fundamentals

Build structured employee records, inspect columns and data types,
create calculated fields, and summarize tabular information.
"""

import pandas as pd


def create_employee_data() -> pd.DataFrame:
    """Return a small, realistic employee DataFrame."""
    return pd.DataFrame(
        {
            "employee_id": [101, 102, 103, 104, 105],
            "name": ["Asha", "Ravi", "Mira", "Neha", "Kabir"],
            "department": [
                "Engineering", "Sales", "Engineering",
                "Finance", "Sales"
            ],
            "monthly_salary": [42000, 50000, 48000, 62000, 55000],
            "experience_years": [1, 3, 2, 5, 4],
        }
    )


def inspect_dataframe(employees: pd.DataFrame) -> None:
    """Explore the DataFrame's structure and selected columns."""
    print("=== DataFrame Basics ===")
    print(employees.to_string(index=False))
    print("\nShape (rows, columns):", employees.shape)
    print("Column names:", employees.columns.tolist())
    print("Data types:\n", employees.dtypes.to_string(), sep="")

    print(
        "\nFirst two rows:\n",
        employees.head(2).to_string(index=False),
        sep="",
    )

    print("\nEmployee names:", employees["name"].tolist())

    engineering = employees.loc[
        employees["department"] == "Engineering",
        ["name", "monthly_salary"],
    ]

    print(
        "\nEngineering employees:\n",
        engineering.to_string(index=False),
        sep="",
    )


def calculate_employee_metrics(employees: pd.DataFrame) -> None:
    """Create derived columns and summarize employee salaries."""
    updated = employees.copy()

    # Create calculated columns.
    updated["annual_salary"] = updated["monthly_salary"] * 12
    updated["annual_bonus"] = (
        updated["annual_salary"] * 0.10
    ).round(2)

    print("\n=== Calculated Columns ===")

    columns = [
        "name",
        "annual_salary",
        "annual_bonus",
    ]

    print(updated[columns].to_string(index=False))

    print(
        "Average monthly salary:",
        updated["monthly_salary"].mean()
    )

    print(
        "Total monthly payroll:",
        updated["monthly_salary"].sum()
    )

    print(
        "Unique departments:",
        sorted(updated["department"].unique().tolist())
    )

    department_summary = updated.groupby(
        "department"
    )["monthly_salary"].mean()

    print(
        "\nAverage monthly salary by department:\n",
        department_summary.to_string(),
        sep="",
    )


def main() -> None:
    """Run the DataFrame examples."""
    employees = create_employee_data()
    inspect_dataframe(employees)
    calculate_employee_metrics(employees)


if __name__ == "__main__":
    main()