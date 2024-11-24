import sqlite3
import matplotlib.pyplot as plt

def create_database():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            date TEXT,
            category TEXT,
            description TEXT,
            amount REAL
        )
    ''')
    conn.commit()
    conn.close()

def add_expense(date, category, description, amount):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)', 
                   (date, category, description, amount))
    conn.commit()
    conn.close()

def view_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    for row in cursor.fetchall():
        print(row)
    conn.close()

def delete_expense(expense_id):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM expenses WHERE id=?', (expense_id,))
    conn.commit()
    conn.close()

def summary_by_category():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
    return cursor.fetchall()

def total_expense():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(amount) FROM expenses')
    total = cursor.fetchone()[0]
    conn.close()
    return total

def plot_expenses_by_category():
    data = summary_by_category()
    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]
    
    plt.figure(figsize=(10, 5))
    plt.bar(categories, amounts, color='blue')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.title('Expenses by Category')
    plt.show()

# Example usage:
create_database()
add_expense('2023-02-10', 'Food', 'Lunch', 12.50)
add_expense('2023-02-11', 'Utilities', 'Electricity Bill', 75.00)
view_expenses()
print(f"Total Expense: {total_expense()}")
plot_expenses_by_category()