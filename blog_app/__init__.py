from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from blog_app.config import Config
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from blog_app.main.routes import main
    from blog_app.users.routes import users
    from blog_app.posts.routes import posts
    from blog_app.errors.handlers import errors

    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(errors)
    return app
