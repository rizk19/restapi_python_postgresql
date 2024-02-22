from flask import Blueprint, jsonify, request
# import uuid

# Entities
# from models.entities.Product import Product
# Models
from models.ProductModel import ProductModel

main = Blueprint('product_blueprint', __name__)


@main.route('/')
def get_products():
    try:
        dataproducts = ProductModel.get_products()
        return jsonify(dataproducts)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_product(id):
    try:
        dataproduct = ProductModel.get_product(id)
        if dataproduct != None:
            return jsonify(dataproduct)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


# @main.route('/add', methods=['POST'])
# def add_movie():
#     try:
#         title = request.json['title']
#         duration = int(request.json['duration'])
#         released = request.json['released']
#         id = uuid.uuid4()
#         movie = Product(str(id), title, duration, released)

#         affected_rows = ProductModel.add_movie(movie)

#         if affected_rows == 1:
#             return jsonify(movie.id)
#         else:
#             return jsonify({'message': "Error on insert"}), 500

#     except Exception as ex:
#         return jsonify({'message': str(ex)}), 500


# @main.route('/update/<id>', methods=['PUT'])
# def update_movie(id):
#     try:
#         title = request.json['title']
#         duration = int(request.json['duration'])
#         released = request.json['released']
#         movie = Product(id, title, duration, released)

#         affected_rows = ProductModel.update_movie(movie)

#         if affected_rows == 1:
#             return jsonify(movie.id)
#         else:
#             return jsonify({'message': "No movie updated"}), 404

#     except Exception as ex:
#         return jsonify({'message': str(ex)}), 500


# @main.route('/delete/<id>', methods=['DELETE'])
# def delete_movie(id):
#     try:
#         movie = Product(id)

#         affected_rows = ProductModel.delete_movie(movie)

#         if affected_rows == 1:
#             return jsonify(movie.id)
#         else:
#             return jsonify({'message': "No movie deleted"}), 404

#     except Exception as ex:
#         return jsonify({'message': str(ex)}), 500
