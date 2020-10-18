from flask import Blueprint, jsonify, request, session
from flask_restful import Api, Resource
import json
from backend.models import register_mybook

# test_bp = Blueprint('test', __name__, url_prefix='/api/test')
# class Test(Resource):
#     def post(self):

#         input_data = request.json

#         print(input_data)
#         result_data = {'body': "Hello, " + input_data['name']}

#         return jsonify(result_data)

# test = Api(test_bp)
# test.add_resource(Test, '')

# bookregister
book_regist_bp = Blueprint('book_regist', __name__, url_prefix='/api/test')
class BookRegist(Resource):
    def regist():
        '''
        ISBNに対応する書籍情報を取得して、Elasticsearchに登録
        '''
        # パラメータからISBNコードと本のタイトルを取得
        # isbn = request.json['isbn']
        # title = request.json['title']
        input_data = request.json
        # print(isbn)
        # print(title)

        name1 = {'body': "Hello, " + input_data['name']}
        return jsonify(name1)#'本が見つかりませんでした'

        # if isbn is None:
        #     name1 = {'body': "Hello, " + name}
        #     return jsonify(name1)#'本が見つかりませんでした'
        # if isbn is True:

        #     # dict型をJSON型のレスポンスに変換
        #     response = jsonify(title)
        #     return response

        register_mybook(input_data['name'])

        return jsonify(result_data)

book_regist = Api(book_regist_bp)
book_regist.add_resource(BookRegist, '')