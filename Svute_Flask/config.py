import os

DB_NAME = "database.db"
class Config:
    SECRET_KEY = '4276f752089dc811919d51b9be6dadc8'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = 'cyborg'
    TOASTR_POSITION_CLASS = 'toast-bottom-right'
    CKEDITOR_SERVE_LOCAL = True
    CKEDITOR_ENABLE_CSRF = True
    WTF_CSRF_ENABLED = True 
    CODEMIRROR_LANGUAGES = ['python', 'html']
    # optional
    CODEMIRROR_THEME = 'darcula'
    CODEMIRROR_ADDONS = (
        ('display','placeholder'),
        ('display','fullscreen'),
        ('fold','indent-fold'),
        ('comment','comment')
    )


