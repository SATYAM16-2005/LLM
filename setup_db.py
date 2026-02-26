# setup_db.py

import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    salary INTEGER,
    department TEXT,
    age INTEGER
)
""")

# Insert sample data
employees = [
    ("Alice", 60000, "IT", 30),
    ("Bob", 45000, "HR", 28),
    ("Charlie", 70000, "IT", 35),
    ("David", 40000, "Finance", 25)
]

cursor.executemany("""
INSERT INTO employees (name, salary, department, age)
VALUES (?, ?, ?, ?)
""", employees)

conn.commit()
conn.close()

print("Database created successfully!")
