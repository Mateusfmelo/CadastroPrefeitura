from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc
from helpers.database import db
from model.error import Error, error_campos
from model.prefeito import Prefeito, prefeito_fields

parser = reqparse.RequestParser()
parser.add_argument('nome', required=True, location= 'json')
parser.add_argument('nascimento', required=True, location= 'json')
parser.add_argument('email', required=True, location= 'json')
parser.add_argument('senha', required=True, location= 'json')
parser.add_argument('telefone', required=True, location= 'json')
parser.add_argument('endereco', required=True, location= 'json')

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
            endereco = args['endereco']            

            # Prefeito
            prefeito = Prefeito(nome, nascimento, email, senha, telefone, endereco)
            
            # Criação de Prefeito.
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
            
            # Evento
            nome = args['nome']
            nascimento = args['nascimento']
            email = args['email']
            senha = args['senha']
            telefone = args['telefone']
            endereco = args['endereco']   

            Prefeito.query \
                .filter_by(id = id) \
                .update(dict(nome = nome, nascimento = nascimento, email = email, senha = senha, telefone = telefone, endereco = endereco ) )
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
