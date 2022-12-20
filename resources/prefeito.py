from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc

from helpers.database import db
from model.error import Error, error_campos
from model.prefeito import Prefeito, prefeito_fields
from model.endereco import Endereco
from model.cidade import Cidade
from model.uf import Uf

parser = reqparse.RequestParser()
parser.add_argument('nome', required=True)
parser.add_argument('nascimento', required=True)
parser.add_argument('email', required=True)
parser.add_argument('senha', required=True,
                    help="Senha é campo obrigatório.")
parser.add_argument('telefone', required=True)
parser.add_argument('endereco', type=dict, required=True)

class Prefeito_Resource(Resource):
    
    @marshal_with(prefeito_fields)
    def get(self):
        current_app.logger.info("Get - Prefeito")
        prefeito = Prefeito.query\
            .all()
        return prefeito, 200

    def post(self):
        current_app.logger.info("Post - Prefeito")
        try:
            # JSON
            args = parser.parse_args()
            nome = args['nome']
            nascimento = args['nascimento']
            email = args['email']
            senha = args['senha']
            telefone = args['telefone']

            # Endereco
            enderecoArgs = args['endereco']
            cep = enderecoArgs['cep']
            numero = enderecoArgs['numero']
            complemento = enderecoArgs['complemento']
            referencia = enderecoArgs['referencia']
            logradouro = enderecoArgs['logradouro']

            # Cidade
            cidade = enderecoArgs['cidade']
            nomeCidade = cidade['nome']
            siglaCidade = cidade['sigla']
            
            # UF
            uf = cidade['uf']
            nomeUf = uf['nome']
            siglaUf = uf['sigla']

            cidade = Cidade(nomeCidade, siglaCidade, Uf(nomeUf, siglaUf))
            endereco = Endereco(cep, numero, complemento,
                                referencia, logradouro, cidade)
            # Prefeito
            prefeito = Prefeito(
                nome, nascimento, email, senha, telefone, endereco)

            # Criação do Prefeito.
            db.session.add(prefeito)
            db.session.commit()

        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204

class Prefeitos_Resource(Resource):
    
    def put(self, id):
        current_app.logger.info("Put - Prefeito")
        try:
         # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Prefeito: %s:" % args)
            # JSON
            args = parser.parse_args()
            nome = args['nome']
            nascimento = args['nascimento']
            email = args['email']
            senha = args['senha']
            telefone = args['telefone']

            # Endereco
            enderecoArgs = args['endereco']
            cep = enderecoArgs['cep']
            numero = enderecoArgs['numero']
            complemento = enderecoArgs['complemento']
            referencia = enderecoArgs['referencia']
            logradouro = enderecoArgs['logradouro']
            
            # Cidade
            cidadeArgs = enderecoArgs['cidade']
            nomeCidade = cidadeArgs['nome']
            siglaCidade = cidadeArgs['sigla']

            # UF
            ufArgs = cidadeArgs['uf']
            nomeUf = ufArgs['nome']
            siglaUf = ufArgs['sigla']

            cidade = Cidade(nomeCidade, siglaCidade, Uf(nomeUf, siglaUf))
            endereco = Endereco(cep, numero, complemento,
                                referencia, logradouro, cidade)
            # Prefeito
            prefeito = Prefeito(
                nome, nascimento, email, senha, telefone, endereco)

            prefeito =Prefeito.query \
                .filter_by(id=id) \
                .first()

            prefeito.nome = nome
            prefeito.nascimento = nascimento
            prefeito.email = email
            prefeito.senha = senha
            prefeito.telefone = telefone
            prefeito.endereco.cep = cep
            prefeito.endereco.numero = numero
            prefeito.endereco.complemento = complemento
            prefeito.endereco.referencia = referencia
            prefeito.endereco.logradouro = logradouro
            prefeito.endereco.cidade.nome = nomeCidade
            prefeito.endereco.cidade.sigla = siglaCidade
            prefeito.endereco.cidade.uf.nome = nomeUf
            prefeito.endereco.cidade.uf.sigla = siglaUf

            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204

    def delete(self, id):
        current_app.logger.info("Delete - Prefeito: %s:" % id)
        try:
            Prefeito.query.filter_by(id=id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 204