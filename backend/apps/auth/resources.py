from flask import Blueprint, jsonify, request, session
import re

from .models import User
from database import db, bcrypt

auth = Blueprint('auth', __name__, url_prefix='/auth')

def validate_auth_payload(payload: dict) -> bool:
    username: str = payload.get('username')
    password: str = payload.get('password')

    if not username or re.search('[^a-zA-Z0-9s]', username) or username.count(' ') or len(username) < 6 or username[0].isdecimal():
        return False
    if not password or len(password) < 8:
        return False
    
    return True

@auth.route('/@me')
def get_current_user():
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'msg': 'Unauthorized'}), 401
    
    u = User.query.filter_by(id=user_id).first()
    return jsonify({
        'id': u.id,
        'username': u.username
    })

@auth.route('/login', methods=['POST'])
def login():
    payload: dict = request.get_json()
    if not validate_auth_payload(payload):
        return {'msg': 'Username or password contains invalid characters'}, 400
    
    u = User.query.filter_by(username=payload['username']).first()
    if u is None:
        # TODO: change error code
        return {'msg': 'User does not exist'}, 401
    if not bcrypt.check_password_hash(u.password, payload['password']):
        return {'msg': 'Invalid username or password'}, 401
    
    session['user_id'] = u.id

    return jsonify({
        'id': u.id,
        'username': u.username
    })

@auth.route('/register', methods=['POST'])
def register():
    # Validate the payload
    payload: dict = request.get_json()
    if not validate_auth_payload(payload):
        return {'msg': 'Username or password contains invalid characters'}, 400
    
    # Check for uniqueness
    if User.query.filter(User.username == payload['username']).first() is not None:
        return {'msg': 'User already exists'}, 409

    hashed_password = bcrypt.generate_password_hash(payload['password'])
    u = User(username = payload['username'], password = hashed_password)
    db.session.add(u)
    db.session.commit()

    return {'msg': 'ok'}, 200

@auth.route('/change_password', methods=['POST'])
def change_password():
    return {}
