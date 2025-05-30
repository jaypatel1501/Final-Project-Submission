@when('the following products exist')
def step_impl(context):
    for row in context.table:
        product = Product(name=row['name'], category=row['category'],
                          price=int(row['price']), available=row['available'] == 'True')
        db.session.add(product)
    db.session.commit()
