from flask import jsonify, request
from app.models import Product

def get_all_products():
    products = Product.get_all()
    return jsonify([product.serialize() for product in products])

def get_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'El producto no fue encontrado'}), 404
    return jsonify(product.serialize())

def create_product():
    data = request.json
    new_product = Product(
        title=data['title'], 
        description=data['description'], 
        images=data['images'], 
        inStock=data['inStock'], 
        price=data['price'], 
        sizes=data['sizes'], 
        slug=data['slug'], 
        tags=data['tags'], 
        type=data['type'], 
        gender=data['gender']
    )
    new_product.save()
    return jsonify(new_product.serialize()), 201

def update_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'El producto no fue encontrado'}), 404
    data = request.json
    product.title = data['title']
    product.description = data['description']
    product.images = data['images']
    product.inStock = data['inStock']
    product.price = data['price']
    product.sizes = data['sizes']
    product.slug = data['slug']
    product.tags = data['tags']
    product.type = data['type']
    product.gender = data['gender']
    product.save()
    return jsonify(product.serialize())

def delete_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'El producto no fue encontrado'}), 404
    product.delete()
    return jsonify({'message': 'El producto fue eliminado exitosamente'})
