import pytest
from modules.common.database import Database

# Тест на вставку продукту з некоректним типом даних
@pytest.mark.database
def test_invalid_data_type():
    db = Database()
    with pytest.raises(ValueError):  # Тепер очікуємо помилку ValueError
        db.insert_product(10, "невірний тип", "опис", "стрічка замість числа")

# Тест на спробу вставити дубльований продукт
@pytest.mark.database
def test_duplicate_entry():
    db = Database()
    db.insert_product(12, "унікальний товар", "опис продукту", 100)
    with pytest.raises(ValueError):  # Оновлено на ValueError, оскільки ID вже існує
        db.insert_product(12, "той самий товар", "новий опис", 200)

# Тест на кількість товару, яка не може бути негативною
@pytest.mark.database
def test_quantity_limit():
    db = Database()
    with pytest.raises(ValueError):  # Оновлено на ValueError, бо кількість не може бути від'ємною
        db.insert_product(13, "товар", "опис товару", -10)

# Тест на вставку продукту з правильними даними
@pytest.mark.database
def test_insert_valid_product():
    db = Database()
    db.insert_product(18, "новий товар", "опис товару", 50)
    product = db.cursor.execute("SELECT * FROM products WHERE id = 18").fetchone()
    assert product is not None, "Product should exist"
    assert product[1] == "новий товар", "Product name does not match"
    assert product[2] == "опис товару", "Product description does not match"
    assert product[3] == 50, "Product quantity does not match"

# Тест на спробу вставити продукт з від'ємною кількістю
@pytest.mark.database
def test_insert_negative_quantity():
    db = Database()
    with pytest.raises(ValueError):  # Оновлено на ValueError, бо кількість не може бути від'ємною
        db.insert_product(19, "товар з від'ємною кількістю", "опис товару", -5)

# Тест на спробу вставити продукт з неправильним типом даних для кількості
@pytest.mark.database
def test_insert_invalid_quantity_type():
    db = Database()
    with pytest.raises(ValueError):  # Оновлено на ValueError для некоректного типу
        db.insert_product(20, "товар", "опис товару", "стрічка замість числа")

# Тест на вставку товару з правильним значенням опису
@pytest.mark.database
def test_insert_product_with_description():
    db = Database()
    db.insert_product(21, "товар з описом", "деталізований опис товару", 30)
    product = db.cursor.execute("SELECT * FROM products WHERE id = 21").fetchone()
    assert product is not None, "Product should exist"
    assert product[2] == "деталізований опис товару", "Description does not match"

# Тест на вставку товару з відсутнім описом (NULL)
@pytest.mark.database
def test_insert_product_without_description():
    db = Database()
    db.insert_product(22, "товар без опису", None, 40)
    product = db.cursor.execute("SELECT * FROM products WHERE id = 22").fetchone()
    assert product is not None, "Product should exist"
    assert product[2] is None, "Description should be NULL"

# Тест на вставку товару з великою кількістю
@pytest.mark.database
def test_insert_product_with_large_quantity():
    db = Database()
    db.insert_product(23, "товар з великою кількістю", "опис товару", 10000)
    product = db.cursor.execute("SELECT * FROM products WHERE id = 23").fetchone()
    assert product is not None, "Product should exist"
    assert product[3] == 10000, "Product quantity does not match"
