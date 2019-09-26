from flask import Blueprint, jsonify, request
alunos_app = Blueprint('alunos_app', __name__, template_folder='templates')
alunos_db = []

@alunos_app.route('/alunos')
def listar_alunos():
    return jsonify(database['ALUNO'])

@alunos_app.route('/alunos', methods=['POST'])
def cadastrar_alunos():
    novo_aluno = request.json
    return jsonify({'erro':'função nao implementada'}), 500

@alunos_app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def alterar_alunos(id_aluno):
    return jsonify({'erro':'função nao implementada'}), 500

@alunos_app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localizar_aluno(id_aluno):
    return jsonify({'erro':'função nao implementada'}), 500

@alunos_app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def remover_aluno(id_aluno):
    return jsonify({'erro':'função nao implementada'}), 500