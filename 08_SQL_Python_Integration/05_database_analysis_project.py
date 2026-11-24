
"""
File: 05_database_analysis_project.py
Topic: Employee Database Analysis Project
Author: Kazi Mustafijur Rahaman

Project:
Analyze employee data using SQLite and Pandas.
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


def run_database_analysis():

    connection = connect_database()

    try:
        print("=" * 60)
        print("EMPLOYEE DATABASE ANALYSIS PROJECT")
        print("=" * 60)

        # 1. Overall business statistics
        overview = pd.read_sql_query("""
            SELECT
                COUNT(*) AS total_employees,
                ROUND(AVG(salary), 2) AS average_salary,
                SUM(salary) AS total_salary
            FROM employees
        """, connection).iloc[0]

        print("\n1. OVERALL STATISTICS")

        print("Total Employees:", int(overview["total_employees"]))

        print(
            f"Average Salary: Rs. "
            f"{overview['average_salary']:,.2f}"
        )

        print(
            f"Total Salary Budget: Rs. "
            f"{overview['total_salary']:,.2f}"
        )

        # 2. Department-wise analysis
        department_report = pd.read_sql_query("""
            SELECT
                d.department_name,
                COUNT(e.employee_id) AS employee_count,
                ROUND(AVG(e.salary), 2) AS average_salary,
                SUM(e.salary) AS total_salary
            FROM employees e
            JOIN departments d
            ON e.department_id = d.department_id
            GROUP BY d.department_name
            ORDER BY average_salary DESC
        """, connection)

        print("\n2. DEPARTMENT ANALYSIS")

        print(department_report.to_string(index=False))

        # 3. City-wise employee analysis
        city_report = pd.read_sql_query("""
            SELECT
                city,
                COUNT(*) AS employee_count
            FROM employees
            GROUP BY city
            ORDER BY employee_count DESC, city ASC
        """, connection)

        print("\n3. CITY-WISE EMPLOYEE DISTRIBUTION")

        print(city_report.to_string(index=False))

        # 4. Highest-paid employee
        top_employee = pd.read_sql_query("""
            SELECT
                e.name,
                d.department_name,
                e.salary
            FROM employees e
            JOIN departments d
            ON e.department_id = d.department_id
            ORDER BY e.salary DESC
            LIMIT 1
        """, connection).iloc[0]

        print("\n4. HIGHEST-PAID EMPLOYEE")

        print("Name:", top_employee["name"])
        print("Department:", top_employee["department_name"])

        print(
            f"Salary: Rs. {top_employee['salary']:,.0f}"
        )

        # 5. Final business insight
        best_department = department_report.iloc[0]

        print("\n5. BUSINESS INSIGHTS")

        print(
            "Highest Average Salary Department:",
            best_department["department_name"]
        )

        print(
            "Total Departments:",
            len(department_report)
        )

        print("\nAnalysis Completed Successfully!")

    finally:
        connection.close()


if __name__ == "__main__":
    run_database_analysis()
