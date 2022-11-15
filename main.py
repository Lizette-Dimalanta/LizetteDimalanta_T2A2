from flask import Flask
from init import db, ma, bc, jwt
from flask_marshmallow import Marshmallow

# Import Controllers
# from controllers.customers_controller import customers_bp
from controllers.auth_controller import auth_bp
from controllers.profiles_controller import profiles_bp
from controllers.addresses_controller import addresses_bp

import os

# Defines App
def create_app():
    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found(err):
        return {'error': str(err)}, 404

    # Disable JSON sort
    app.config['JSON_SORT_KEYS'] = False

    # Retrieve Database URL
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    # JWTManager Secret Key
    app.config['JSON_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    # Creating Objects
    db.init_app(app)
    ma.init_app(app)
    bc.init_app(app)
    jwt.init_app(app)

    # Activate Blueprints
    # app.register_blueprint(customers_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(profiles_bp)
    app.register_blueprint(addresses_bp)

    @app.route('/')
    def index():
        return 'Hello'

    return app

# Blueprint: Modularise flask application (like class)