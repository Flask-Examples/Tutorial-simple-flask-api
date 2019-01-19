"""
Flask API REST

Tutorial Python e Flask - Como Criar Uma API REST Em Minutos

Homepage and documentation:
https://www.youtube.com/watch?v=N6cZ6aHvLYs&list=PLTzsdf89Lw9wISVTaoCBwk4pRCCgddRZO


Copyright (c) 2018, Marcus Mariano.
License: MIT (see LICENSE for details)
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])    
def home():
    """Home page."""
    return 'Hello world', 200


devs = [
    {
        'id': 1,
        'name': 'Rafael Marques',
        'lang': 'python'
    }, 
    {
        'id': 2,
        'name': 'Robert T',
        'lang': 'python'    
    }, 
    {
        'id': 3,
        'name': 'John Delare',
        'lang': 'node'
    }, 
    {
        'id': 4,
        'name': 'John Doe',
        'lang': 'node'
    }
]

@app.route('/api/v1.0/devs', methods=['GET'])
def dev():
    """"""
    return jsonify(devs), 200

@app.route('/api/v1.0/devs/<string:lang>', methods=['GET'])
def dev_per_lang(lang):
    """Passando parametro e filtrando pela linguagem"""
    dev_per_lang = [dev for dev in devs if dev['lang'] == lang]
    return jsonify(dev_per_lang), 200

@app.route('/api/v1.0/devs/<int:id>', methods=['PUT'])
def change_lang(id):
    """linguagem"""
    for dev in devs:
        if dev['id'] == id:
            dev['lang'] = request.get_json().get('lang')
    
            return jsonify(dev), 200
    
    return jsonify({'error': 'dev not found'}), 404

@app.route('/api/v1.0/devs/<int:id>', methods=['GET'])
def dev_per_id(id):
    """Passando parametro e filtrando pela id"""
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200
    
    return jsonify({'error': 'not found'}), 404

@app.route('/api/v1.0/devs', methods=['POST'])
def save_dev():
    """?"""
    data = request.get_json()
    devs.append(data)

    return jsonify(data), 201


@app.route('/api/v1.0/devs/<int:id>', methods=['DELETE'])
def remove_dev(id):
    """Apagar parametro filtrando pela id"""
    index = id
    del devs[index]
    
    return jsonify({'message': 'Dev is no longer alive'}), 200


if __name__ == "__main__":
    app.run(debug=True)
