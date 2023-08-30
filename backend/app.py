from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS
import json

from database import db, migrate
from config import Config

from apps.projects.models import Project

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
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI
    app.config['SECRET_KEY'] = Config.SECRET_KEY

    db.init_app(app)
    migrate.init_app(app, db, directory='migrations', command='db')

    CORS(app)

    from apps.projects.resources import projects as projects_api
    app.register_blueprint(projects_api)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=Config.FLASK_DEBUG)