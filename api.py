from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class products(Resource):
    def get(self):
        data = { 'message' : 'Hello World' }
        return { 'data' : data }, 200



api.add_resource(products, '/products')

if __name__ == '__main__':
    app.run()
