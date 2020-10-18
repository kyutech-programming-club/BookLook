from flask import Blueprint, jsonify, request, session
from flask_restful import Api, Resource
import json
from backend.models import register_mybook

test_bp = Blueprint('test', __name__, url_prefix='/api/test')
class Test(Resource):
    def post(self):

        input_data = request.json

        print(input_data)
        result_data = {'body': "Hello, " + input_data['name']}

        register_mybook(input_data['name'])

        return jsonify(result_data)

test = Api(test_bp)
test.add_resource(Test, '')
