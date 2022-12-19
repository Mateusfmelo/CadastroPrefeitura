from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc
from helpers.database import db
from model.error import Error, error_campos
from model.uf import Uf, uf_fields

parser = reqparse.RequestParser()
parser.add_argument('nome', required=True, location= 'json')
parser.add_argument('sigla', required=True, location= 'json')

class Uf_Resource(Resource):
    
    @marshal_with(uf_fields)
    def get(self):
        current_app.logger.info("Get - UF")
        uf = Uf.query\
            .all()
        return uf, 200
    
    def post(self):
        current_app.logger.info("Post - UF")
        try:
            # JSON
            args = parser.parse_args()
            nome = args['nome']
            sigla = args['sigla']
            
            # UF
            nome = args['nome']
            sigla = args['sigla']

            # UF
            uf = Uf(nome, sigla)
            
            # Criação da UF.
            db.session.add(uf)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204
    
class Ufs_Resource(Resource):
    def put(self, id):
        current_app.logger.info("Put - UF")
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("UF: %s:" % args)
            
            # Evento
            nome = args['nome']
            sigla = args['sigla']

            Uf.query \
                .filter_by(id = id) \
                .update(dict(nome = nome, sigla = sigla))
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204 
    
    def delete(self, id):
        current_app.logger.info("Delete - UF: %s:" % id)
        try:
            Uf.query.filter_by(id=id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 204