from helpers.database import db
from flask_restful import fields

prefeitura_fields = {
    'id': fields.Integer(attribute='id'),
    'cidade': fields.String(attribute='cidade'),
    'prefeito': fields.String(attribute='prefeito'),
    'email': fields.String(attribute='email'),
    'telefone': fields.String(attribute='telefone')
}

class Prefeitura(db.Model):
    
    __tablename__ = "tb_prefeitura"

    id = db.Column(db.Integer, primary_key=True)
    cidade = db.Column(db.String(120), unique=True, nullable=False)
    prefeito = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, cidade, prefeito, email, telefone):
        self.cidade = cidade
        self.prefeito= prefeito
        self.email = email
        self.telefone= telefone

    def __repr__(self):
        return '<Cidade: {}, Prefeito: {}, Email: {}>, Email: {}'.format(self.cidade, self.prefeito, self.email, self.telefone)