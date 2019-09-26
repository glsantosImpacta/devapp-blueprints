from flask import Blueprint, jsonify, request
professores_app = Blueprint('professores_app', __name__, template_folder='templates')
professores_db = []

@professores_app.route('/professores')
def listar_professores():
    return jsonify(database['PROFESSOR'])

@professores_app.route('/professores', methods=['POST'])
def cadastrar_professores():
    novo_professor = request.json
    return jsonify({'erro':'função nao implementada'}), 500

@professores_app.route('/professores/<int:id_professor>', methods=['PUT'])
def alterar_professor(id_professor):
    professor_request = request.json
    return jsonify({'erro':'função nao implementada'}), 500

@professores_app.route('/professores/<int:id_professor>', methods=['GET'])
def localizar_professor(id_professor):
    return jsonify({'erro':'função nao implementada'}), 500

@professores_app.route('/professores/<int:id_professor>', methods=['DELETE'])
def remover_professor(id_professor):
    return jsonify({'erro':'função nao implementada'}), 500