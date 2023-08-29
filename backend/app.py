from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS
import json

api = Blueprint('api', 'api')

@api.route('/projects', methods=['GET', 'POST', 'DELETE'])
def projects():
    with open('db.json', 'r') as f:
        db = json.load(f)
    if request.method == 'GET':
        result: list = db['projects']
        result.sort(key = lambda x: x['name'])
        start_index = (int(request.args['_page']) - 1) * int(request.args['_limit'])
        return jsonify(result[start_index:start_index + int(request.args['_limit'])])

@api.route('/projects/<int:id>', methods=['PUT', 'GET'])
def update_project(id: int):
    if request.method == 'PUT':
        with open('db.json', 'r') as f:
            db = json.load(f)
            projects = db['projects']
        result = None
        for p in projects:
            if p['id'] == id:
                p['name'] = request.json['name']
                p['description'] = request.json['description']
                p['imageUrl'] = request.json['imageUrl']
                p['contractTypeId'] = request.json['contractTypeId']
                p['contractSignedOn'] = request.json['contractSignedOn']
                p['budget'] = request.json['budget']
                p['isActive'] = request.json['isActive']
                result = p
                break
        
        with open('db.json', 'w') as f:
            json.dump({'projects': projects}, f)

        return jsonify(result)
    else:
        with open('db.json', 'r') as f:
            db = json.load(f)
            projects = db['projects']
        for p in projects:
            if p['id'] == id:
                return jsonify(p)

def create_app():
    app = Flask(__name__)
    app.secret_key = 'some random key'
    CORS(app)

    app.register_blueprint(api)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)