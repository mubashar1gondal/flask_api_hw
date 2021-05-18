from app import app
from flask import jsonify
from app.models import User
from app import db
from flask.globals import request

@app.route('/user', methods=['GET'])
def get_user():
    
    return jsonify([u.to_dict() for u in User.query.all()])

@app.route('/user/<int:id>', methods=['GET'])
def get_users(id):
   
    return jsonify(User.query.get(id).to_dict())


@app.route('/user', methods=['POST'])
def create_user():
    
    u = User()
    data = {
        'name': request.get_json()['name'],
        'email': request.get_json()['email']
    }
    u.from_dict(data)
    u.save()
    return jsonify(u.to_dict()), 201

@app.route('/user/<int:id>', methods=['PUT'])
def update_users(id):

    u = User.query.get(id)
    data = {
        'name': request.get_json()['name'],
        'email': request.get_json()['email']
    }
    u.from_dict(data)
    db.session.commit()
    return jsonify(u.to_dict())


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):

    u = User.query.get(id)
    db.session.delete(u)
    db.session.commit()
    return jsonify([u.to_dict() for u in User.query.all()])