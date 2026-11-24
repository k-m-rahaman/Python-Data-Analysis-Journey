
"""
File: 03_crud_operations.py
Topic: CRUD Operations
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


def get_employee(connection, employee_id):

    return connection.execute("""
        SELECT e.employee_id, e.name,
               d.department_name, e.salary, e.city
        FROM employees e
        JOIN departments d
        ON e.department_id = d.department_id
        WHERE e.employee_id = ?
    """, (employee_id,)).fetchone()


def demonstrate_crud():

    connection = connect_database()

    try:
        print("=" * 50)
        print("CRUD OPERATIONS")
        print("=" * 50)

        employee_id = 9999

        # Remove an old demo record if the script is rerun.
        connection.execute(
            "DELETE FROM employees WHERE employee_id = ?",
            (employee_id,)
        )
        connection.commit()

        # CREATE
        connection.execute("""
            INSERT INTO employees
            (employee_id, name, department_id,
             salary, city, joining_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            employee_id, "Demo User", 2,
            40000, "Kolkata", "2025-01-01"
        ))

        connection.commit()

        print("\nCREATE:")
        print(get_employee(connection, employee_id))

        # READ
        employee = get_employee(connection, employee_id)

        print("\nREAD:")
        print("Employee Name:", employee[1])
        print("Salary:", employee[3])

        # UPDATE
        connection.execute("""
            UPDATE employees
            SET salary = ?, city = ?
            WHERE employee_id = ?
        """, (45000, "Barasat", employee_id))

        connection.commit()

        print("\nUPDATE:")
        print(get_employee(connection, employee_id))

        # DELETE
        connection.execute(
            "DELETE FROM employees WHERE employee_id = ?",
            (employee_id,)
        )

        connection.commit()

        print("\nDELETE:")
        print("Demo employee removed successfully.")

    finally:
        connection.close()


if __name__ == "__main__":
    demonstrate_crud()
