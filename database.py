import sqlite3

DB_NAME = "campusfood.db"

def get_food_items():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM food_items")
    rows = cursor.fetchall()
    conn.close()
    return [{'id': r[0], 'name': r[1], 'price': r[2]}for r in rows]


def get_item_by_id(item_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM food_items WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    conn.close()
    return item

def save_order(items, order_time):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (items, order_time) VALUES (?, ?)", (items, order_time))
    conn.commit()
    conn.close()

def get_all_orders():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, items, order_time FROM orders ORDER BY id DESC")
    orders = cursor.fetchall()
    conn.close()
    return orders
