from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc
from helpers.database import db
from model.error import Error, error_campos
from model.prefeitura import Prefeitura, prefeitura_fields

parser = reqparse.RequestParser()
parser.add_argument('cidade', required=True, location= 'json')
parser.add_argument('prefeito', required=True, location= 'json')
parser.add_argument('email', required=True, location= 'json')
parser.add_argument('telefone', required=True, location= 'json')

class Prefeitura_Resource(Resource):
    
    @marshal_with(prefeitura_fields)
    def get(self):
        current_app.logger.info("Get - Prefeitura")
        prefeitura = Prefeitura.query\
            .all()
        return prefeitura, 200
    
    def post(self):
        current_app.logger.info("Post - Prefeitura")
        try:
            # JSON
            args = parser.parse_args()
            cidade = args['cidade']
            prefeito = args['prefeito']
            email = args['email']
            telefone = args['telefone']

            # Prefeitura
            prefeitura = Prefeitura(cidade, prefeito, email, telefone)
            
            # Criação do Prefeitura.
            db.session.add(prefeitura)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204
    
class Prefeituras_Resource(Resource):
    def put(self, id):
        current_app.logger.info("Put - Prefeitura")
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Prefeitura: %s:" % args)
            
            # Evento
            cidade = args['cidade']
            prefeito = args['prefeito']
            email = args['email']
            telefone = args['telefone']

            Prefeitura.query \
                .filter_by(id = id) \
                .update(dict(cidade = cidade, prefeito = prefeito, email = email, telefone = telefone))
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204 
    
    def delete(self, id):
        current_app.logger.info("Delete - Prefeitura: %s:" % id)
        try:
            Prefeitura.query.filter_by(id=id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 204