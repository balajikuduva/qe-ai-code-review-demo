import sqlite3

def get_expense(expense_id):

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

  # BAD CODE: SQL injection risk
    query = "SELECT * FROM expenses WHERE id = " + expense_id

    cursor.execute(query)

    result = cursor.fetchone()

    return result
