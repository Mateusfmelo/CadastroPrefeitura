from helpers.database import db
from flask_restful import fields

endereco_fields = {
    'id': fields.Integer(attribute='id'),
    'cep': fields.String(attribute='cep'),
    'numero': fields.String(attribute='numero'),
    'complemento': fields.String(attribute='complemento'),
    'referencia': fields.String(attribute='referencia'),
    'logradouro': fields.String(attribute='logradouro')
}

class Endereco(db.Model):

    __tablename__ = "tb_endereco"

    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(9), nullable=False)
    numero = db.Column(db.String(9), nullable=False)
    complemento = db.Column(db.String, nullable=False)
    referencia = db.Column(db.String, nullable=False)
    logradouro = db.Column(db.String, nullable=False)

    prefeitura_id = db.Column(db.Integer, db.ForeignKey("tb_prefeitura.id"))

    def __init__(self, cep, numero, complemento, referencia, logradouro):
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        self.referencia = referencia
        self.logradouro = logradouro

    def __repr__(self):
        return '<Cep: {}\n Numero: {}\n Complemento: {}\n Referencia: {}\n Logradouro: {}>'.format(self.cep, self.numero, self.complemento, self.referencia, self.logradouro)
