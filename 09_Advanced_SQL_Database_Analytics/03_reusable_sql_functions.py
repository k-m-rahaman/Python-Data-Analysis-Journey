
"""
File: 03_reusable_sql_functions.py
Topic: Reusable SQL Functions with Python

Description:
Demonstrates reusable Python functions
for executing SQL queries and database analysis.

Author: Kazi Mustafijur Rahaman
"""

from pathlib import Path
import sqlite3
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "datasets" / "company_analysis.db"


def create_connection():

    if not DB_PATH.exists():
        raise FileNotFoundError("Database not found. Run Part 8 first.")

    return sqlite3.connect(DB_PATH)


def get_employees_by_department(conn, department):

    query = """
        SELECT
            e.employee_id,
            e.name,
            d.department_name,
            e.salary
        FROM employees e
        JOIN departments d
        ON e.department_id = d.department_id
        WHERE d.department_name = ?
        ORDER BY e.salary DESC
    """

    return pd.read_sql_query(
        query,
        conn,
        params=(department,)
    )


def get_department_payroll(conn):

    query = """
        SELECT
            d.department_name,
            COUNT(e.employee_id) AS total_employees,
            SUM(e.salary) AS total_payroll,
            ROUND(AVG(e.salary), 2) AS average_salary
        FROM departments d
        LEFT JOIN employees e
        ON d.department_id = e.department_id
        GROUP BY d.department_id, d.department_name
        ORDER BY total_payroll DESC
    """

    return pd.read_sql_query(query, conn)


def get_employees_by_city(conn, city):

    query = """
        SELECT
            employee_id,
            name,
            city,
            salary
        FROM employees
        WHERE city = ?
        ORDER BY salary DESC
    """

    return pd.read_sql_query(
        query,
        conn,
        params=(city,)
    )


def main():

    conn = create_connection()

    try:

        print("\nENGINEERING DEPARTMENT")

        engineering = get_employees_by_department(
            conn, "Engineering"
        )

        print(engineering.to_string(index=False))

        print("\nDEPARTMENT PAYROLL")

        payroll = get_department_payroll(conn)

        print(payroll.to_string(index=False))

        print("\nEMPLOYEES FROM KOLKATA")

        kolkata = get_employees_by_city(
            conn, "Kolkata"
        )

        print(kolkata.to_string(index=False))

    finally:
        conn.close()


if __name__ == "__main__":
    main()
