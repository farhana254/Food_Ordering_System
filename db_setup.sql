-- db_setup.sql

DROP TABLE IF EXISTS food_items;
CREATE TABLE food_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    items TEXT,
    order_time TEXT
);

-- Add sample food items
INSERT INTO food_items (name, price) VALUES ('Veg Biryani', 60);
INSERT INTO food_items (name, price) VALUES ('Chicken Curry', 80);
INSERT INTO food_items (name, price) VALUES ('Chapathi (2 pcs)', 20);

