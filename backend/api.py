from flask import Blueprint, jsonify, request, session
from flask_restful import Api, Resource
import json
from backend.models import register_book, get_all

test_bp = Blueprint('test', __name__, url_prefix='/api/test')
class Test(Resource):
    def post(self):

        input_data = request.json

        print(input_data)
        result_data = {'body': input_data['title'] + "を登録しました"}

        register_book(input_data['title'], input_data['cover'])

        return jsonify(result_data)

    def get(self):
        books = get_all()
        # books_dict = [books.to_dict() for book in books]
        console.log(books)
        books_dict = {
            {
                'title': "book1"
            },
            {
                'title': "book2"
            }
        }
        return jsonify(books_dicts)
    

test = Api(test_bp)
test.add_resource(Test, '')