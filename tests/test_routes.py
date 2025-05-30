def test_get_product(client, product):
    response = client.get(f"/products/{product.id}")
    assert response.status_code == 200

def test_update_product(client, product):
    response = client.put(f"/products/{product.id}", json={"name": "Updated Name"})
    assert response.status_code == 200

def test_delete_product(client, product):
    response = client.delete(f"/products/{product.id}")
    assert response.status_code == 204

def test_list_all_products(client):
    response = client.get("/products")
    assert response.status_code == 200

def test_list_by_name(client):
    response = client.get("/products?name=Camera")
    assert response.status_code == 200

def test_list_by_category(client):
    response = client.get("/products?category=Electronics")
    assert response.status_code == 200

def test_list_by_availability(client):
    response = client.get("/products?available=true")
    assert response.status_code == 200
