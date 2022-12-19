from helpers.database import db
from flask_restful import fields
from model.prefeito import prefeito_fields

prefeitura_fields = {
    'id': fields.Integer(attribute='id'),
    'secretarios': fields.String(attribute='secretarios'),
    'email': fields.String(attribute='email'),
    'telefone': fields.String(attribute='telefone'),
    'prefeito': fields.Nested(prefeito_fields)
}

class Prefeitura(db.Model):
    
    __tablename__ = "tb_prefeitura"

    id = db.Column(db.Integer, primary_key=True)
    secretarios = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(100), unique=True, nullable=False)
    prefeito = db.relationship("Prefeito", uselist=False)
    prefeito_id = db.Column(db.Integer, db.ForeignKey("tb_prefeito.id"))

    def __init__(self, email, telefone, secretarios):
        self.secretarios = secretarios
        self.email = email
        self.telefone= telefone

    def __repr__(self):
        return '<Nome: {}, Nascimento: {}, Nome do Prefeito: {}>'.format(self.secretarios, self.email, self.telefone)