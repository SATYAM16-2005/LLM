# database.py

import sqlite3

def execute_query(query):
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    try:
        cursor.execute(query)

        # Fetch results only for SELECT
        if query.strip().upper().startswith("SELECT"):
            results = cursor.fetchall()
        else:
            conn.commit()
            results = "Query executed successfully."

    except Exception as e:
        results = f"Error: {e}"

    conn.close()
    return results
