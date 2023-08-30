from flask import Blueprint, request, jsonify
from .models import Project
from database import db

projects = Blueprint('projects', __name__, url_prefix='/projects')

@projects.route('/')
def index():
    result: list[Project] = Project.query.all()
    result.sort(key = lambda x: x.name)
    
    page = int(request.args['_page']) - 1
    limit = int(request.args['_limit'])
    start_index = page * limit

    result_json = [{
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'imageUrl': p.imageUrl,
        'contractTypeId': p.contractTypeId,
        'contractSignedOn': p.contractSignedOn,
        'budget': p.budget,
        'isActive': p.isActive
    } for p in result[start_index:start_index+limit]]

    return jsonify(result_json)

@projects.route('/<int:id>', methods=['GET', 'PUT'])
def project_by_id(id: int):
    p: Project = Project.query.get(id)

    if request.method == 'GET':
        return jsonify({
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'imageUrl': p.imageUrl,
            'contractTypeId': p.contractTypeId,
            'contractSignedOn': p.contractSignedOn,
            'budget': p.budget,
            'isActive': p.isActive
        })
    
    # PUT
    p.name = request.json['name']
    p.description = request.json['description']
    p.imageUrl = request.json['imageUrl']
    p.contractTypeId = request.json['contractTypeId']
    p.contractSignedOn = request.json['contractSignedOn']
    p.budget = request.json['budget']
    p.isActive = request.json['isActive']

    db.session.commit()
    return jsonify(p)