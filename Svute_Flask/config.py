import os

DB_NAME = "database.db"
class Config:
    SECRET_KEY = '4276f752089dc811919d51b9be6dadc8'
    SQLALCHEMY_DATABASE_URI = f'postgresql://db:y9ddcj8ji7tvukpe@app-b4f55ee8-703a-4d47-b70e-7c18a5bcce17-do-user-8840902-0.b.db.ondigitalocean.com:25060/db'
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


