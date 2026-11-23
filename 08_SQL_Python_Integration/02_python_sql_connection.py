
"""
File: 02_python_sql_connection.py
Topic: Connecting Python with SQL
Author: Kazi Mustafijur Rahaman
"""

from pathlib import Path
import sqlite3

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


def demonstrate_connection():

    connection = connect_database()
    connection.row_factory = sqlite3.Row

    try:
        print("=" * 50)
        print("PYTHON AND SQL CONNECTION")
        print("=" * 50)

        print("\nDatabase Connected Successfully!")

        department = "Engineering"

        query = """
            SELECT e.employee_id, e.name,
                   d.department_name, e.salary
            FROM employees e
            JOIN departments d
            ON e.department_id = d.department_id
            WHERE d.department_name = ?
            ORDER BY e.salary DESC
        """

        records = connection.execute(
            query, (department,)
        ).fetchall()

        print(f"\nEmployees in {department}:")

        for record in records:
            print(
                f"{record['employee_id']} | "
                f"{record['name']} | "
                f"{record['department_name']} | "
                f"Rs. {record['salary']:,.0f}"
            )

        total = connection.execute(
            "SELECT COUNT(*) FROM employees"
        ).fetchone()[0]

        print("\nTotal Database Records:", total)

    finally:
        connection.close()
        print("\nDatabase Connection Closed.")


if __name__ == "__main__":
    demonstrate_connection()
