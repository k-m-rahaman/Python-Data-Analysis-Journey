
"""
File: 04_sql_queries_pandas.py
Topic: SQL Queries with Pandas
Author: Kazi Mustafijur Rahaman
"""

from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "datasets" / "company_analysis.db"

DEPARTMENTS = [
    (1, "Engineering"), (2, "Sales"),
    (3, "Finance"), (4, "Human Resources")
]

EMPLOYEES = [
    (101, "Asha", 1, 72000, "Kolkata", "2022-04-11"),
    (102, "Ravi", 2, 52000, "Durgapur", "2023-01-15"),
    (103, "Mira", 1, 85000, "Kolkata", "2021-08-20"),
    (104, "Neha", 3, 68000, "Suri", "2022-11-03"),
    (105, "Kabir", 2, 58000, "Kolkata", "2024-02-19"),
    (106, "Isha", 4, 61000, "Barasat", "2023-06-12"),
    (107, "Arjun", 1, 90000, "Durgapur", "2020-09-05"),
    (108, "Zoya", 3, 75000, "Kolkata", "2021-12-01"),
    (109, "Dev", 2, 48000, "Suri", "2024-05-25"),
    (110, "Priya", 4, 64000, "Barasat", "2022-07-17")
]


def connect_database():

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_PATH)
    connection.execute("PRAGMA foreign_keys = ON")

    connection.executescript("""
        CREATE TABLE IF NOT EXISTS departments (
            department_id INTEGER PRIMARY KEY,
            department_name TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department_id INTEGER NOT NULL,
            salary REAL NOT NULL CHECK(salary >= 0),
            city TEXT NOT NULL,
            joining_date TEXT NOT NULL,
            FOREIGN KEY(department_id)
            REFERENCES departments(department_id)
        );
    """)

    connection.executemany(
        "INSERT OR IGNORE INTO departments VALUES (?, ?)",
        DEPARTMENTS
    )

    connection.executemany(
        "INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?, ?, ?)",
        EMPLOYEES
    )

    connection.commit()

    return connection


def analyze_with_pandas():

    connection = connect_database()

    try:
        print("=" * 55)
        print("SQL QUERIES WITH PANDAS")
        print("=" * 55)

        # Retrieve SQL data into a DataFrame
        employee_df = pd.read_sql_query("""
            SELECT e.employee_id,
                   e.name,
                   d.department_name,
                   e.salary,
                   e.city
            FROM employees e
            JOIN departments d
            ON e.department_id = d.department_id
            ORDER BY e.employee_id
        """, connection)

        print("\nEMPLOYEE DATAFRAME:")
        print(employee_df.head().to_string(index=False))

        # Department-wise analysis
        department_summary = pd.read_sql_query("""
            SELECT
                d.department_name,
                COUNT(*) AS employee_count,
                ROUND(AVG(e.salary), 2) AS average_salary,
                SUM(e.salary) AS total_salary
            FROM employees e
            JOIN departments d
            ON e.department_id = d.department_id
            GROUP BY d.department_name
            ORDER BY average_salary DESC
        """, connection)

        print("\nDEPARTMENT SUMMARY:")
        print(department_summary.to_string(index=False))

        # Pandas filtering
        high_earners = employee_df[
            employee_df["salary"] >= 70000
        ].sort_values("salary", ascending=False)

        print("\nEMPLOYEES EARNING 70000 OR MORE:")
        print(
            high_earners[["name", "salary"]]
            .to_string(index=False)
        )

    finally:
        connection.close()


if __name__ == "__main__":
    analyze_with_pandas()
