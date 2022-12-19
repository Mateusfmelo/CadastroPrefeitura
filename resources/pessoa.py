from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc

from helpers.database import db
from model.pessoa import Pessoa, pessoa_fields
from model.endereco import Endereco
from model.cidade import Cidade
from model.uf import Uf
from model.error import Error, error_campos

parser = reqparse.RequestParser()
parser.add_argument('nome', required=True)
parser.add_argument('nascimento', required=True)
parser.add_argument('email', required=True)
parser.add_argument('senha', required=True,
                    help="Senha é campo obrigatório.")
parser.add_argument('telefone', required=True)
parser.add_argument('endereco', type=dict, required=True)

class Pessoa_Resource(Resource):

    @marshal_with(pessoa_fields)
    def get(self):
        current_app.logger.info("Get - Pessoas")
        pessoa = Pessoa.query\
            .all()
        return pessoa, 200

    def post(self):
        current_app.logger.info("Post - Funcionario")
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
            # Pessoa
            pessoa = Pessoa(
                nome, nascimento, email, senha, telefone, endereco)

            # Criação do Pessoa.
            db.session.add(pessoa)
            db.session.commit()

        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204
    
class Pessoas_Resource(Resource):
    
    def put(self, id):
        current_app.logger.info("Put - Pessoas")
        try:
         # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Pessoa: %s:" % args)
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
            uf = cidade['uf']
            nomeUf = uf['nome']
            siglaUf = uf['sigla']

            cidade = Cidade(nomeCidade, siglaCidade, Uf(nomeUf, siglaUf))
            endereco = Endereco(cep, numero, complemento,
                                referencia, logradouro, cidade)
            # Pessoa
            pessoa = Pessoa(
                nome, nascimento, email, senha, telefone, endereco)

            pessoa =Pessoa.query \
                .filter_by(id=id) \
                .first()

            pessoa.nome = nome
            pessoa.nascimento = nascimento
            pessoa.email = email
            pessoa.senha = senha
            pessoa.telefone = telefone
            pessoa.endereco.cep = cep
            pessoa.endereco.numero = numero
            pessoa.endereco.complemento = complemento
            pessoa.endereco.referencia = referencia
            pessoa.endereco.logradouro = logradouro
            pessoa.endereco.cidade.nome = nomeCidade
            pessoa.endereco.cidade.sigla = siglaCidade
            pessoa.endereco.cidade.uf.nome = nomeUf
            pessoa.endereco.cidade.uf.sigla = siglaUf

            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204
    
    def delete(self, id):
        current_app.logger.info("Delete - Pessoa: %s:" % id)
        try:
            Pessoa.query.filter_by(id=id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 204