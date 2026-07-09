from flask import Flask, render_template
from db import db
import os
from flask_migrate import Migrate
from models import Usuario, Pizza, Pedido
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_usuario = os.getenv('DB_USERNAME')
db_senha = os.getenv('DB_PASSWORD')
db_database = os.getenv('DB_DATABASE')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

conexao = f"mysql+pymysql://{db_usuario}:{db_senha}@{db_host}:{db_port}/{db_database}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

@app.route('/avaliacoes')
def avaliacoes():
    return render_template('avaliacoes.html')

@app.route('/faleconosco')
def fale():
    return render_template('fale.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/teste_insert')
def testes_insert():
    user = Usuario('Cauã Carlos', 'cauaC12@gmail.com', '123456789')
    db.session.add(user) #Insert Into Usuario(nome, email, senha) values ('...', '...', '...')
    user = Usuario('Pedro', 'pedro12@gmail.com', '12345789')
    db.session.add(user) #Insert Into Usuario(nome, email, senha) values ('...', '...', '...')
    user = Usuario('Antonio', 'antonio12@gmail.com', '12345789')
    db.session.add(user) #Insert Into Usuario(nome, email, senha) values ('...', '...', '...')
    db.session.commit()
    return 'Dados inseridos com sucesso!'

@app.route('/teste_select')
def teste_select():
    users = Usuario.query.all()
    for u in users:
        print(u.nome)

    user = Usuario.query.get(3)
    print(f'O usuario de id 2 é {user.nome}')
    return 'Dados recuperados'

@app.route('/teste_update')
def teste_update():
    u = Usuario.query.get(1)
    u.nome = "Cauã Carlos S. de Oliveira"
    db.session.add(u)
    db.session.commit()
    return 'Dados alterados com sucesso!'

@app.route('/teste_delete')
def teste_delete():
    u = Usuario.query.get(2)
    db.session.delete(u)
    db.session.commit()
    return 'Dados excluídos com sucesso!'

@app.route('/teste_insert_pizza')
def teste_insert_pizza():
    pizza = Pizza('Quatro queijos', '60')
    db.session.add(pizza)
    pizza = Pizza('Portuguesa', '70')
    db.session.add(pizza)
    pizza = Pizza('Calabresa', '73.45')
    db.session.add(pizza)
    db.session.commit()
    return 'Pizzas inseridas na tabela'

@app.route('/teste_insert_pedido')
def teste_inser_pedido():
    pedido = Pedido(3, 5)
    db.session.add(pedido)
    db.session.commit()
    return 'Pedidos realizados com sucesso'

@app.route('/teste_select_pedido')
def teste_select_pedido():
    todos = Pedido.query.all()
    pedidos = []
    for pedido in todos:
        u = {
            'Id do cliente' : pedido.id_usuario,
            'id da pizza' : pedido.id_pizza,
            'Horario do pedido' : pedido.data
        }
        pedidos.append(u)

    return pedidos

@app.route('/teste_update_pedido')
def teste_update_pedido():
    pedido = Pedido.query.get(1)
    pedido.id_pizza = '5'
    db.session.add(pedido)
    db.session.commit()
    return 'Dados alterados com sucesso'

@app.route('/teste_delete_pedido')
def teste_delete_pedido():
    p = Pedido.query.get(16)
    db.session.delete(p)
    db.session.commit()
    return 'Delete realizado com sucesso'