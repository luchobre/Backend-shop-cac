from flask import Flask
from app.views import *
from app.database import init_app
from flask_cors import CORS

app = Flask(__name__)

init_app(app)
CORS(app, resources={r"/products/*": {"origins": "*"}})

app.route('/products', methods=['GET'])(get_all_products)
app.route('/products', methods=['POST'])(create_product)
app.route('/products/<int:product_id>', methods=['GET'])(get_product)
app.route('/products/<int:product_id>', methods=['PUT'])(update_product)
app.route('/products/<int:product_id>', methods=['DELETE'])(delete_product)

if __name__ == '__main__':
    app.run(debug=True)
