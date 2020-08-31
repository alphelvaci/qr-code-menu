from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, fields
from flask_restful import Api, Resource
from os import getenv

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)
ma = Marshmallow(application)
api = Api(application)

### Database table models ###

class Products(db.Model):
    __tablename__ = 'products'
    idx = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    category = db.Column(db.String(50))
    imageUrl = db.Column(db.String(150))

    def __repr__(self):
        return f'<User {self.title}>'

### Data serialization schemes ###

class ProductSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = (
            'idx', 'name', 'description', 'price', 'category',
            'imageUrl')

product_schema = ProductSchema()
multiple_products_schema = ProductSchema(many=True)

### Api Resources ###

class AllProductsResource(Resource):
    def get(self):
        products = Products.query.all()
        return multiple_products_schema.dump(products)

class ProductsResource(Resource):
    def get(self, idx):
        product = Products.query.get_or_404(idx)
        return product_schema.dump(product)

api.add_resource(AllProductsResource, '/api/v1/products')
api.add_resource(ProductsResource, '/api/v1/products/<int:idx>')

if __name__ == '__main__':
    application.run()