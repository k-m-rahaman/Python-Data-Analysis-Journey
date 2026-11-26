
"""
File: 05_transactions.py
Topic: SQL Transactions and Transaction Management

Description:
Demonstrates transaction control using
COMMIT, ROLLBACK, and SAVEPOINT.

Author: Kazi Mustafijur Rahaman
"""

from pathlib import Path
import sqlite3


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "datasets" / "company_analysis.db"


def create_connection():

    if not DB_PATH.exists():
        raise FileNotFoundError("Database not found. Run Part 8 first.")

    return sqlite3.connect(DB_PATH)


def create_demo_table(conn):

    conn.execute("""
        CREATE TEMP TABLE transaction_demo AS
        SELECT employee_id, name, salary
        FROM employees
    """)

    conn.commit()


def get_salary(conn, employee_id):

    result = conn.execute("""
        SELECT salary
        FROM transaction_demo
        WHERE employee_id = ?
    """, (employee_id,)).fetchone()

    return result[0]


def demonstrate_rollback(conn, employee_id):

    print("\nROLLBACK DEMONSTRATION")

    original_salary = get_salary(conn, employee_id)

    conn.execute("BEGIN")

    conn.execute("""
        UPDATE transaction_demo
        SET salary = salary + 5000
        WHERE employee_id = ?
    """, (employee_id,))

    print("Salary during transaction:",
          get_salary(conn, employee_id))

    conn.rollback()

    print("Salary after rollback:",
          get_salary(conn, employee_id))

    print("Original salary:", original_salary)


def demonstrate_commit_and_savepoint(conn, employee_id):

    print("\nCOMMIT AND SAVEPOINT DEMONSTRATION")

    conn.execute("BEGIN")

    # First update
    conn.execute("""
        UPDATE transaction_demo
        SET salary = salary + 1000
        WHERE employee_id = ?
    """, (employee_id,))

    # Create savepoint
    conn.execute("SAVEPOINT bonus_change")

    # Second update
    conn.execute("""
        UPDATE transaction_demo
        SET salary = salary + 5000
        WHERE employee_id = ?
    """, (employee_id,))

    print("Salary after second update:",
          get_salary(conn, employee_id))

    # Undo only the second update
    conn.execute("ROLLBACK TO SAVEPOINT bonus_change")

    conn.execute("RELEASE SAVEPOINT bonus_change")

    # Save the first update
    conn.commit()

    print("Salary after commit:",
          get_salary(conn, employee_id))


def main():

    conn = create_connection()

    try:

        create_demo_table(conn)

        employee = conn.execute("""
            SELECT employee_id, name
            FROM transaction_demo
            ORDER BY employee_id
            LIMIT 1
        """).fetchone()

        if employee is None:
            print("No employees available.")
            return

        employee_id, name = employee

        print("Employee:", name)

        demonstrate_rollback(conn, employee_id)

        demonstrate_commit_and_savepoint(
            conn, employee_id
        )

    finally:
        conn.close()


if __name__ == "__main__":
    main()
