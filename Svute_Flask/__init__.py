###################### IMPORT ######################
# Update date: 07/08/2021
# Written by ngtrdai
# https://github.com/ngtrdai

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .config import Config
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flaskext.markdown import Markdown
from flask_toastr import Toastr
from flask_bcrypt import Bcrypt
from flask_ckeditor import CKEditor
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
# Khoi tao database
db = SQLAlchemy()
bcrypt = Bcrypt()
ckeditor = CKEditor()
DB_NAME = "database.db"
loginManager = LoginManager()
loginManager.login_view = 'users.login'
loginManager.login_message = 'Xin vui lòng đăng nhập!'
loginManager.login_message_category = 'info'

def Create_Database(app):
    if not path.exists('app/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

# Khoi tao Flask
def Create_App(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    loginManager.init_app(app)
    md = Markdown(app, auto_escape=False, safe_mode=True)
    toastr = Toastr(app)
    ckeditor.init_app(app)
    csrf = CSRFProtect(app)    
    admin = Admin(app,template_mode='bootstrap4')
    from Svute_Flask.users.routes import users
    from Svute_Flask.main.routes import main
    from Svute_Flask.posts.routes import posts
    from Svute_Flask.notes.routes import notes
    from Svute_Flask.models import User, Post, Note, Comments, Category
    Create_Database(app)
    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(posts)
    app.register_blueprint(notes)
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(Note, db.session))
    admin.add_view(ModelView(Comments, db.session))
    admin.add_view(ModelView(Category, db.session))
    return app
