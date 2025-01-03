import pytest
from modules.common.database import Database

@pytest.mark.database
def test_database_connection():
    db = Database()
    version = db.test_connection()
    assert version is not None, "Database connection failed."

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
    print(users)
    assert len(users) > 0, "No users found in the database."

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user_data = db.get_user_address_by_name("Sergii")
    expected_data = ("Maydan Nezalezhnosti 1", "Kyiv", "3127", "Ukraine")
    assert user_data == expected_data, f"Expected {expected_data}, got {user_data}"

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    updated_qnt = db.select_product_qnt_by_id(1)
    assert updated_qnt == 25, f"Expected quantity 25, got {updated_qnt}"

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, "печиво", "солодке", 30)
    qnt = db.select_product_qnt_by_id(4)
    assert qnt == 30, f"Expected quantity 30, got {qnt}"

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, "тестові", "дані", 999)
    db.delete_product_by_id(99)

    # Перевіряємо, що продукт з id 99 більше не існує
    result = db.select_product_qnt_by_id(99)
    
    # Переконуємось, що продукт не знайдений
    assert result is None, f"Product with id 99 should not exist after deletion, got {result}"

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print(orders)
    expected_data = [(1, "Sergii", "солодка вода", "з цукром", '2023-01-01')]  # Додано дату
    assert len(orders) == 1, f"Expected 1 order, got {len(orders)}"
    assert orders[0] == expected_data[0], f"Expected {expected_data[0]}, got {orders[0]}"
