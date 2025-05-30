def test_create_product(app):
    product = Product(name="Laptop", category="Electronics", price=999, available=True)
    db.session.add(product)
    db.session.commit()
    assert product.id is not None

def test_read_product(app):
    product = Product(name="Book", category="Books", price=20, available=True)
    db.session.add(product)
    db.session.commit()
    found = Product.query.get(product.id)
    assert found.name == "Book"

def test_update_product(app):
    product = Product(name="Toy", category="Toys", price=25, available=True)
    db.session.add(product)
    db.session.commit()
    product.price = 30
    db.session.commit()
    assert product.price == 30

def test_delete_product(app):
    product = Product(name="TV", category="Electronics", price=300, available=False)
    db.session.add(product)
    db.session.commit()
    db.session.delete(product)
    db.session.commit()
    assert Product.query.get(product.id) is None

def test_list_all_products(app):
    products = Product.query.all()
    assert isinstance(products, list)

def test_find_by_name(app):
    Product(name="Camera", category="Electronics", price=150, available=True).create()
    results = Product.find_by_name("Camera")
    assert len(results) > 0

def test_find_by_category(app):
    Product(name="Tablet", category="Electronics", price=200, available=True).create()
    results = Product.find_by_category("Electronics")
    assert all(p.category == "Electronics" for p in results)

def test_find_by_availability(app):
    Product(name="Fan", category="Electronics", price=50, available=True).create()
    results = Product.find_by_availability(True)
    assert all(p.available for p in results)
