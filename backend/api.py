from flask import Blueprint, jsonify, request, session
from flask_restful import Api, Resource
import json
from backend.models import register_book

test_bp = Blueprint('test', __name__, url_prefix='/api/test')
class Test(Resource):
    def post(self):

        input_data = request.json

        print(input_data)
        result_data = {'body': input_data['title'] + "を登録しました"}

        register_book(input_data['title'], input_data['cover'])

        return jsonify(result_data)

test = Api(test_bp)
test.add_resource(Test, '')