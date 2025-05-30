@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.serialize()), 200

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    product.name = data.get("name", product.name)
    db.session.commit()
    return jsonify(product.serialize()), 200

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return "", 204

@app.route("/products", methods=["GET"])
def list_products():
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")

    query = Product.query
    if name:
        query = query.filter_by(name=name)
    if category:
        query = query.filter_by(category=category)
    if available is not None:
        query = query.filter_by(available=available.lower() == "true")

    products = query.all()
    return jsonify([p.serialize() for p in products]), 200
