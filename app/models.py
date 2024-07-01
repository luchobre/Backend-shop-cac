from app.database import get_db

class Product:

    def __init__(self, id=None, title=None, description=None, images=None, inStock=None, price=None, sizes=None, slug=None, tags=None, type=None, gender=None):
        self.id = id
        self.title = title
        self.description = description
        self.images = images if images else []
        self.inStock = inStock
        self.price = price
        self.sizes = sizes if sizes else []
        self.slug = slug
        self.tags = tags if tags else []
        self.type = type
        self.gender = gender

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'images': self.images,
            'inStock': self.inStock,
            'price': self.price,
            'sizes': self.sizes,
            'slug': self.slug,
            'tags': self.tags,
            'type': self.type,
            'gender': self.gender
        }

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM products"
        cursor.execute(query)
        rows = cursor.fetchall()
        products = [Product(id=row[0], title=row[1], description=row[2], images=row[3].split(','), inStock=row[4], price=row[5], sizes=row[6].split(','), slug=row[7], tags=row[8].split(','), type=row[9], gender=row[10]) for row in rows]
        cursor.close()
        return products

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id:
            cursor.execute("""
                UPDATE products SET title = %s, description = %s, images = %s, inStock = %s, price = %s, sizes = %s, slug = %s, tags = %s, type = %s, gender = %s
                WHERE id = %s
            """, (self.title, self.description, ','.join(self.images), self.inStock, self.price, ','.join(self.sizes), self.slug, ','.join(self.tags), self.type, self.gender, self.id))
        else:
            cursor.execute("""
                INSERT INTO products (title, description, images, inStock, price, sizes, slug, tags, type, gender) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (self.title, self.description, ','.join(self.images), self.inStock, self.price, ','.join(self.sizes), self.slug, ','.join(self.tags), self.type, self.gender))
            self.id = cursor.lastrowid
        db.commit()
        cursor.close()

    @staticmethod
    def get_by_id(product_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Product(id=row[0], title=row[1], description=row[2], images=row[3].split(','), inStock=row[4], price=row[5], sizes=row[6].split(','), slug=row[7], tags=row[8].split(','), type=row[9], gender=row[10])
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s", (self.id,))
        db.commit()
        cursor.close()
