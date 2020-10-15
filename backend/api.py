from flask import Blueprint, jsonify, request, session
from flask_restful import Api, Resource
import json

test_bp = Blueprint('test', __name__, url_prefix='/api/test')
class Test(Resource):
    def post(self):

        input_data = request.json

        print(input_data)
        result_data = {'body': "Hello, " + input_data['name']}

        return jsonify(result_data)

test = Api(test_bp)
test.add_resource(Test, '')
