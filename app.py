import os
import logging
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask("MyBookList") 
api = Api(app)

# Hardcoded database
data = {}

# Request parser
parser = reqparse.RequestParser()
parser.add_argument('data', type=str, help='Data to be stored')

# GET, PUT, and DELETE operations
class DataResource(Resource):
    def get(self, key):
        if key in data:
            return {key: data[key]}
        else:
            abort(404, message="Data not found")


    def put(self, key):
        args = parser.parse_args()
        data[key] = args['data']
        return {key: data[key]}, 201

    def delete(self, key):
        if key not in data:
            abort(404, message="Data not found")
        del data[key]
        return '', 204

# POST service
class DataListResource(Resource):
    def post(self):
        args = parser.parse_args()
        key = str(len(data) + 1)
        data[key] = args['data']
        return {key: data[key]}, 201

api.add_resource(DataResource, '/data/<string:key>')
api.add_resource(DataListResource, '/data')

# Config service
class ConfigResource(Resource):
    def get(self):
        config_data =  {key:value for key, value in os.environ.items()}
        logger.info(f"Environment variables: {config_data}")
        return config_data
    
api.add_resource(ConfigResource, '/config')

logger = logging.getLogger(__name__)

class FibonacciResource(Resource):
    def get(self):
        length = int(request.args.get('length', 0))
        if length <= 0:
            abort(400, message="Invalid length parameter")
        fib_sequence = [fibonacci(n) for n in range(length)]
        return fib_sequence

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

api.add_resource(FibonacciResource, '/fib')

# Swagger configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Flask RESTful Example"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5002)
