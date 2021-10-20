from flask import Flask, Response, request,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime
import mysql.connector
import json


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#conmfigurar para os parametros locais no formato: dialect+driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3310/veiculos'

db = SQLAlchemy(app)

#modelo do banco
class Veiculos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    veiculo = db.Column(db.String(50))
    marca = db.Column(db.String(50))
    ano = db.Column(db.Integer)
    descricao = db.Column(db.String(150))
    vendido = db.Column(db.Boolean)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)

    #converte para json
    def to_json(self):
        return {"id":self.id,
                "veiculo":self.veiculo,
                "marca":self.marca,
                "ano":self.ano,
                "descricao":self.descricao,
                "vendido":self.vendido,
                "created":self.created,
                "updated":self.updated}

#cria o banco de dados no esquema acima
#db.create_all()

@app.route('/')
def Index():
    veiculo = Veiculos.query.all()
    return render_template("index.html",veiculo=veiculo)


#CRUD
#seleciona tudo
@app.route("/veiculos", methods=["GET"])
def seleciona_veiuclos():
    #retorna com todos os valores da tabela
    veiculos_obj = Veiculos.query.all()
    #converte para json todos os objetos
    veiculos_json = [Veiculos.to_json() for Veiculos in veiculos_obj]
    #retorna o json para a requisicao
    return response_gen(200,"veiculos",veiculos_json,"ok")

#seleciona por id
@app.route("/veiculos/<id>", methods=["GET"])
def seleciona_veiculo(id):
    #retorna o valor que coresponde ao mesmo id passado
    veiculo_obj = Veiculos.query.filter_by(id=id).first()
    #converte para json
    veiuclo_json = veiculo_obj.to_json()
    #retorna o json para a requisicao
    return response_gen(200,"veiculo",veiuclo_json)

#adiciona um novo veiculo
@app.route("/veiculos", methods=["POST"])
def adiciona_veiculo():
    body = request.get_json()
    #validar se veio os parametros
    try:
        #cria um veiculo
        date_now = datetime.now().isoformat()[:-7]
        veiculo = Veiculos( veiculo=body["veiculo"],
                            marca=body["marca"],
                            ano=int(body["ano"]),
                            descricao=body["descricao"],
                            vendido=False,
                            created=date_now,
                            updated=date_now)
        #abre uma secao e adicionou a classe
        db.session.add(veiculo)
        db.session.commit()
        return response_gen(201,"veiculo",veiculo.to_json,"Adicionado")
    except Exception as e:
        print(e)
        return response_gen(400,"veiculo",{},"Erro ao adicionar")

#atualiza
@app.route("/veiculos/<id>", methods=["PUT"])
def atualiza_veiculo(id):
    #pega o veiculo
    veiculo_obj = Veiculos.query.filter_by(id=id).first()
    #pega as modificacoes
    body = request.get_json()
    try:
        if('id' in body):
            veiculo_obj.id = body["id"]
        if('veiculo' in body):
            veiculo_obj.veiculo = body["veiculo"]
        if('marca' in body):
            veiculo_obj.marca = body["marca"]
        if('ano' in body):
            veiculo_obj.ano = body["ano"]
        if('descricao' in body):
            veiculo_obj.descricao = body["descricao"]
        if('vendido' in body):
            veiculo_obj.vendido = body["vendido"]
        if('updated' in body):
            veiculo_obj.updated = datetime.now().strftime('‘%d-%m-%Y %M:%S:%f')[:-4]
        db.session.add(veiculo_obj)
        db.session.commit()
        return response_gen(200,"veiculo",veiculo_obj.to_json(),"Atualizado")
    except Exception as e:
        print('Erro', e)
        return response_gen(400,"veiculo",{},"Erro ao atualizar")

#deletar
@app.route("/veiculos/<id>", methods=["DELETE"])
def deleta_veiculo(id):
    veiculo_obj = Veiculos.query.filter_by(id=id).first()

    try:
        db.session.delete(veiculo_obj)
        db.session.commit()
        return response_gen(200,"veiculo",veiculo_obj.to_json(),"Deletado")
    except Exception as e:
        print('Erro', e)
        return response_gen(400,"veiculo",{},"Erro ao deletar")


#find
@app.route("/veiculos/find/<q>", methods=["GET"])
def acha_veiculo(q):
    try:
        veiculo_obj = Veiculos.query.filter(Veiculos.veiculo.like('%'+q+'%')).first()
        return response_gen(200,"veiculo",veiculo_obj.to_json(),"Achou")
    except Exception as e:
        print('Erro', e)
        return response_gen(400,"veiculo",{},"Erro ao procurar")

#padronizando os retornos
def response_gen(status, content_name, content,message=False):
    body = {}
    body[content_name] = content
    if(message):
        body["message"] = message
    return Response(json.dumps(body),status=status, mimetype="application/json")
app.run()

