from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc
from helpers.database import db
from model.error import Error, error_campos
from model.cidade import Cidade, cidade_fields

parser = reqparse.RequestParser()
parser.add_argument('nome', required=True, location= 'json')
parser.add_argument('sigla', required=True, location= 'json')
parser.add_argument('uf', required=True, location= 'json')

class Cidade_Resource(Resource):
    
    @marshal_with(cidade_fields)
    def get(self):
        current_app.logger.info("Get - Cidade")
        cidade = Cidade.query\
            .all()
        return cidade, 200
    
    def post(self):
        current_app.logger.info("Post - Cidade")
        try:
            # JSON
            args = parser.parse_args()
            nome = args['nome']
            sigla = args['sigla']
            uf = args['uf']
            
            # Cidade
            nome = args['nome']
            sigla = args['sigla']
            uf = args['uf']

            # Cidade
            cidade = Cidade(nome, sigla, uf)
            
            # Criação da Cidade.
            db.session.add(cidade)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204
    
class Cidades_Resource(Resource):
    def put(self, id):
        current_app.logger.info("Put - Cidade")
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Cidade: %s:" % args)
            
            # Evento
            nome = args['nome']
            sigla = args['sigla']
            uf = args['uf']

            Cidade.query \
                .filter_by(id = id) \
                .update(dict(nome = nome, sigla = sigla, uf = uf))
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204 
    
    def delete(self, id):
        current_app.logger.info("Delete - Cidade: %s:" % id)
        try:
            Cidade.query.filter_by(id=id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 204