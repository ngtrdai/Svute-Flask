import os

DB_NAME = "database.db"
class Config:
    SECRET_KEY = '4276f752089dc811919d51b9be6dadc8'
    SQLALCHEMY_DATABASE_URI = f'postgresql://svute:b13yfcqd2xh86nf4@app-7aca48f8-5789-40a7-845a-c1845bd02701-do-user-8840902-0.b.db.ondigitalocean.com:25060/svute?sslmode=require'
    #SQLALCHEMY_DATABASE_URI = f'mongodb://ngtrdai:nguyendai5901@cluster0-shard-00-00.2rman.mongodb.net:27017,cluster0-shard-00-01.2rman.mongodb.net:27017,cluster0-shard-00-02.2rman.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-9i5zbp-shard-0&authSource=admin&retryWrites=true&w=majority'
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "hotro@svute.com"
    MAIL_PASSWORD = "22HXHE84GinG2eL"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SEND_FILE_MAX_AGE_DEFAULT = -1
    FLASK_ADMIN_SWATCH = 'cyborg'
    TOASTR_POSITION_CLASS = 'toast-bottom-right'
    CKEDITOR_SERVE_LOCAL = True
    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_LANGUAGE = 'vi'
    CKEDITOR_ENABLE_CODESNIPPET = True
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


