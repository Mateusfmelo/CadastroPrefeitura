from helpers.database import db
from flask_restful import fields
from model.pessoa import Pessoa
from model.endereco import endereco_fields
from sqlalchemy import ForeignKey

prefeito_fields = {
    'id': fields.Integer(attribute='id'),
    'nome': fields.String(attribute='nome'),
    'nascimento': fields.String(attribute='nascimento'),
    'email': fields.String(attribute='email'),
    'senha': fields.String(attribute='senha'),
    'telefone': fields.String(attribute='telefone'),
    'endereco': fields.Nested(endereco_fields)
}

class Prefeito(Pessoa, db.Model):
    
    __tablename__ = "tb_prefeito"
    __mapper_args__ = {'polymorphic_identity': 'prefeito'}
    
    id = db.Column(ForeignKey ("tb_pessoa.id"), primary_key=True)

    def __init__(self, nome, nascimento, email, senha, telefone, endereco):
        super().__init__(nome, nascimento, email, senha, telefone, endereco)

    def __repr__(self):
        return '<Nome: {}, Nascimento: {}, Email: {}>, Senha: {}, Telefone: {}, Endereço: {}'.format(self.nome, self.nascimento, self.email, self.senha, self.telefone, self.endereco)
