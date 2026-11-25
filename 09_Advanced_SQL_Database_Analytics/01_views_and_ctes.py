
"""
File: 01_views_and_ctes.py
Topic: SQL Views and Common Table Expressions

Description:
Creates reusable SQL views and performs
advanced queries using CTEs and window functions.

Author: Kazi Mustafijur Rahaman
"""

from pathlib import Path
import sqlite3
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "datasets" / "company_analysis.db"


def create_connection():
    """Connect to the existing SQLite database."""
    if not DB_PATH.exists():
        raise FileNotFoundError(
            "Database not found. Run Part 8 first."
        )

    return sqlite3.connect(DB_PATH)


def create_employee_view(conn):
    """Create a reusable employee details view."""

    conn.execute("""
        CREATE VIEW IF NOT EXISTS employee_details_view AS
        SELECT
            e.employee_id,
            e.name,
            d.department_name,
            e.salary,
            e.city,
            e.joining_date
        FROM employees e
        JOIN departments d
        ON e.department_id = d.department_id
    """)

    conn.commit()
    print("Employee view created successfully!")


def display_employee_view(conn):
    """Display employee information from the view."""

    query = """
        SELECT *
        FROM employee_details_view
        ORDER BY employee_id
    """

    df = pd.read_sql_query(query, conn)

    print("\nEMPLOYEE DETAILS VIEW")
    print(df.to_string(index=False))


def analyze_with_cte(conn):
    """Analyze departments using a CTE."""

    query = """
        WITH department_summary AS (
            SELECT
                d.department_name,
                COUNT(e.employee_id) AS total_employees,
                ROUND(AVG(e.salary), 2) AS average_salary,
                MAX(e.salary) AS highest_salary
            FROM departments d
            LEFT JOIN employees e
            ON d.department_id = e.department_id
            GROUP BY d.department_id, d.department_name
        )

        SELECT *
        FROM department_summary
        ORDER BY average_salary DESC
    """

    df = pd.read_sql_query(query, conn)

    print("\nDEPARTMENT ANALYSIS USING CTE")
    print(df.to_string(index=False))


def rank_employees(conn):
    """Rank employees within their departments."""

    query = """
        SELECT
            name,
            department_name,
            salary,
            RANK() OVER (
                PARTITION BY department_name
                ORDER BY salary DESC
            ) AS salary_rank
        FROM employee_details_view
        ORDER BY department_name, salary_rank
    """

    df = pd.read_sql_query(query, conn)

    print("\nEMPLOYEE SALARY RANKING")
    print(df.to_string(index=False))


def main():

    conn = create_connection()

    try:
        create_employee_view(conn)
        display_employee_view(conn)
        analyze_with_cte(conn)
        rank_employees(conn)

    finally:
        conn.close()


if __name__ == "__main__":
    main()
