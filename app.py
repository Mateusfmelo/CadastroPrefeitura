from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from model.endereco import Endereco
from model.prefeitura import Prefeitura

from helpers.database import db, migrate
from resources.endereco import Endereco_Resource, Enderecos_Resource
from resources.prefeitura import Prefeitura_Resource, Prefeituras_Resource

# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:mateus@localhost:5432/aemotor"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

api = Api(app)
api.add_resource(Endereco_Resource, '/enderecos')
api.add_resource(Enderecos_Resource, '/enderecos/<int:id>')

api.add_resource(Prefeitura_Resource, '/prefeituras')
api.add_resource(Prefeituras_Resource, '/prefeituras/<int:id>')

if __name__ == '__main__':
    app.run(debug=False)
