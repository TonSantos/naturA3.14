from flask import jsonify, abort
from flask.views import MethodView

from . import app

from .client import SemaceApiClient

@app.route("/")
def about():
    description = {
        "name": "NaturA3.14",
        "version": "0.0.1",
        "about":"Translates public information from the Natuur system into JSON, more access: http://natuur.semace.ce.gov.br",
        "license": "MIT"
    }
    return jsonify(description)

@app.route("/login")
def login():
    client = SemaceApiClient()
    data, status = client.login_page()
    return jsonify(data) ,status

@app.route("/processos")
def processos():
    client = SemaceApiClient()
    data, status = client.list_processos()
    return jsonify(data), status

@app.route("/grupos-de-atividades")
def grupos_de_atividades():
    client = SemaceApiClient()
    data, status = client.list_grupos()
    return jsonify(data), status