from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Dummy authentication
    if username == 'admin' and password == 'secret':
        return jsonify({'message': 'Login successful', 'token': 'dummy-jwt-token'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
