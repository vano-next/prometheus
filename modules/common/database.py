import sqlite3

class Database:
    def __init__(self, db_path=":memory:"):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_tables()  # Створення таблиць при ініціалізації

    def create_tables(self):
        # Створення таблиці customers
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            postalCode TEXT NOT NULL,
            country TEXT NOT NULL
        );
        """)

        # Створення таблиці products (дозволяється NULL для description)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,  -- Дозволяється NULL
            quantity INTEGER NOT NULL
        );
        """)

        # Створення таблиці orders
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            product_id INTEGER,
            date TEXT,
            FOREIGN KEY(customer_id) REFERENCES customers(id),
            FOREIGN KEY(product_id) REFERENCES products(id)
        );
        """)

        self.connection.commit()

        # Вставка тестових даних
        self.insert_test_data()

    def insert_test_data(self):
        # Вставка тестових даних у таблицю customers
        self.cursor.execute("""
        INSERT OR IGNORE INTO customers (name, address, city, postalCode, country) 
        VALUES
        ('Sergii', 'Maydan Nezalezhnosti 1', 'Kyiv', '3127', 'Ukraine');
        """)
        
        # Вставка тестових даних у таблицю products
        self.cursor.execute("""
        INSERT OR IGNORE INTO products (id, name, description, quantity) 
        VALUES
        (1, 'солодка вода', 'з цукром', 10),
        (2, 'печиво', 'солодке', 50);
        """)

        # Вставка тестових даних у таблицю orders
        self.cursor.execute("""
        INSERT OR IGNORE INTO orders (customer_id, product_id, date)
        VALUES
        (1, 1, '2023-01-01');
        """)

        self.connection.commit()

    def test_connection(self):
        self.cursor.execute("SELECT sqlite_version();")
        version = self.cursor.fetchone()[0]
        print(f"SQLite version: {version}")
        return version

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_user_address_by_name(self, name):
        query = """
        SELECT address, city, postalCode, country
        FROM customers
        WHERE name = ?;
        """
        self.cursor.execute(query, (name,))
        return self.cursor.fetchone()

    def update_product_qnt_by_id(self, product_id, qnt):
        query = """
        UPDATE products
        SET quantity = ?
        WHERE id = ?;
        """
        self.cursor.execute(query, (qnt, product_id))
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = "SELECT quantity FROM products WHERE id = ?;"
        self.cursor.execute(query, (product_id,))
        return self.cursor.fetchone()[0]

    def insert_product(self, product_id, name, description, qnt):
        # Перевірка на тип кількості
        if not isinstance(qnt, int) or qnt < 0:
            raise ValueError("Quantity must be a non-negative integer")

        # Перевірка на наявність продукту з таким ID
        self.cursor.execute("SELECT COUNT(*) FROM products WHERE id = ?", (product_id,))
        if self.cursor.fetchone()[0] > 0:
            raise ValueError("Product with this ID already exists")
        
        # Вставка товару
        query = """
        INSERT INTO products (id, name, description, quantity)
        VALUES (?, ?, ?, ?);
        """
        self.cursor.execute(query, (product_id, name, description, qnt))
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = "DELETE FROM products WHERE id = ?;"
        self.cursor.execute(query, (product_id,))
        self.connection.commit()

    def get_detailed_orders(self):
        query = """
        SELECT
            orders.id AS order_id,
            customers.name AS customer_name,
            products.name AS product_name,
            products.description AS product_description,
            orders.date AS order_date
        FROM orders
        INNER JOIN customers ON orders.customer_id = customers.id
        INNER JOIN products ON orders.product_id = products.id;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
