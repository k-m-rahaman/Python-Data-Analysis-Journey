
"""
File: 04_triggers_audit_logs.py
Topic: SQL Triggers and Audit Logs

Description:
Demonstrates automatic salary-change logging
using SQLite triggers and temporary tables.

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


def create_demo_tables(conn):

    # Temporary tables keep this demonstration
    # separate from the original employee data.

    conn.execute("""
        CREATE TEMP TABLE trigger_demo_employees AS
        SELECT employee_id, name, salary
        FROM employees
    """)

    conn.execute("""
        CREATE TEMP TABLE salary_audit (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER,
            old_salary REAL,
            new_salary REAL,
            changed_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)


def create_salary_trigger(conn):

    conn.execute("""
        CREATE TEMP TRIGGER salary_update_trigger

        AFTER UPDATE OF salary
        ON trigger_demo_employees

        WHEN OLD.salary != NEW.salary

        BEGIN

            INSERT INTO salary_audit (
                employee_id,
                old_salary,
                new_salary
            )

            VALUES (
                OLD.employee_id,
                OLD.salary,
                NEW.salary
            );

        END;
    """)

    print("Salary trigger created successfully!")


def test_trigger(conn):

    employee = conn.execute("""
        SELECT employee_id, name, salary
        FROM trigger_demo_employees
        ORDER BY employee_id
        LIMIT 1
    """).fetchone()

    if employee is None:
        print("No employees available.")
        return

    employee_id, name, old_salary = employee

    print("\nBEFORE UPDATE")
    print(name, old_salary)

    conn.execute("""
        UPDATE trigger_demo_employees
        SET salary = salary + 1000
        WHERE employee_id = ?
    """, (employee_id,))

    conn.commit()

    print("\nSALARY CHANGE AUDIT LOG")

    audit = pd.read_sql_query(
        "SELECT * FROM salary_audit",
        conn
    )

    print(audit.to_string(index=False))


def main():

    conn = create_connection()

    try:
        create_demo_tables(conn)
        create_salary_trigger(conn)
        test_trigger(conn)

    finally:
        conn.close()


if __name__ == "__main__":
    main()
