from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({'message': 'Bienvenue sur l API Flask!'})

@main.route('/hello/<name>')
def hello(name):
    return jsonify({'message': f'Bonjour {name}!'})

@main.route('/add/<int:a>/<int:b>')
def add(a, b):
    return jsonify({'result': a + b})

@main.route('/api/data')
def get_data():
    return jsonify({'data': [1, 2, 3, 4, 5]})
