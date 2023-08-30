from flask import Flask
from flask_cors import CORS

from database import db, migrate, bcrypt, server_session
from config import Config

from apps.projects.models import Project
from apps.auth.models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db, directory='migrations', command='db')
    bcrypt.init_app(app)
    server_session.init_app(app)
    
    CORS(app)

    from apps.projects.resources import projects as projects_api
    from apps.auth.resources import auth as auth_api

    app.register_blueprint(projects_api)
    app.register_blueprint(auth_api)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=Config.FLASK_DEBUG)