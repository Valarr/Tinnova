from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#conmfigurar para os parametros locais no formato: dialect+driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3310/veiculos'
db = SQLAlchemy(app)

class Veiculos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    veiculo = db.Column(db.String(50))
    marca = db.Column(db.String(50))
    ano = db.Column(db.Integer)
    descricao = db.Column(db.String(150))
    vendido = db.Column(db.Boolean)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)

db.create_all()

