from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from model.cidade import Cidade
from model.pessoa import Pessoa
from model.prefeito import Prefeito
from model.prefeitura import Prefeitura
from model.endereco import Endereco
from model.uf import Uf


from helpers.database import db, migrate
from resources.pessoa import Pessoa_Resource, Pessoas_Resource
from resources.prefeito import Prefeito_Resource, Prefeitos_Resource
from resources.prefeitura import Prefeitura_Resource, Prefeituras_Resource
from resources.cidade import Cidade_Resource, Cidades_Resource
from resources.endereco import Endereco_Resource, Enderecos_Resource
from resources.uf import Uf_Resource, Ufs_Resource


# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:mateus@localhost:5432/aemotor"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

api = Api(app)

api.add_resource(Pessoa_Resource, '/pessoas')
api.add_resource(Pessoas_Resource, '/pessoas/<int:id>')

api.add_resource(Prefeito_Resource, '/prefeitos')
api.add_resource(Prefeitos_Resource, '/prefeitos/<int:id>')

api.add_resource(Prefeitura_Resource, '/prefeituras')
api.add_resource(Prefeituras_Resource, '/prefeituras/<int:id>')

api.add_resource(Cidade_Resource, '/cidades')
api.add_resource(Cidades_Resource, '/cidades/<int:id>')

api.add_resource(Endereco_Resource, '/enderecos')
api.add_resource(Enderecos_Resource, '/enderecos/<int:id>')

api.add_resource(Uf_Resource, '/ufs')
api.add_resource(Ufs_Resource, '/ufs/<int:id>')

if __name__ == '__main__':
    app.run(debug=False)