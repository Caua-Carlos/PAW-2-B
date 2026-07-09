from db import db
from datetime import date, datetime
from sqlalchemy import Column, Integer, String, Date, DateTime, func

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))
    
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self):
        return "<Usuario {}>".format(self.nome)
    
class Pizza(db.Model):
    __tablename__ = 'pizza'
    id = db.Column(db.Integer, primary_key = True)
    sabor = db.Column(db.String(100))
    preco = db.Column(db.String(100))
    
    def __init__(self, sabor, preco):
        self.sabor = sabor
        self.preco = preco


    def __repr__(self):
        return "<Pizza {}>".format(self.sabor)

class Pedido(db.Model):
    __tablename__ = 'pedido'
    id = db.Column(db.Integer, primary_key = True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable = False)
    id_pizza = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable = False)
    data = db.Column(db.DateTime, default = func.now())

    def __init__(self, id_usuario, id_pizza):
        self.id_usuario = id_usuario
        self.id_pizza = id_pizza
        