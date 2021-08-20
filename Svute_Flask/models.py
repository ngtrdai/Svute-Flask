from flask_admin.base import expose
from Svute_Flask import db, loginManager
from flask import current_app, redirect, url_for, request, flash,abort
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from slugify import slugify
from flask_login import current_user, UserMixin,login_required
from flask_security import RoleMixin
from flask_admin.contrib.sqla import ModelView

@loginManager.user_loader
def load_user(id):
    return User.query.get(int(id))

class Note(db.Model):
    note_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, default="Không có tiêu đề")
    note = db.Column(db.String(200000), nullable=False)
    image_file = db.Column(db.String(20))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self) -> str:
        return f"Note('{self.title}', '{self.date}')"

roles_users = db.Table('roles_users',
                        db.Column('user_id', db.Integer,
                        db.ForeignKey('user.id')),
                        db.Column('role_id', db.Integer,
                        db.ForeignKey('role.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200), nullable=False)
    fullname = db.Column(db.String(200))
    about = db.Column(db.Text, default='')
    fb_link = db.Column(db.String(100), default='#')
    tw_link = db.Column(db.String(100), default='#')
    git_link = db.Column(db.String(100), default='#')
    web_link = db.Column(db.String(100), default='#')
    active = db.Column(db.Boolean(), default=False)
    image_file = db.Column(db.String(200), nullable=False, default='../static/profile_pics/avatar.svg')
    notes = db.relationship('Note', backref='author', lazy=True)
    posts = db.relationship('Post', backref='author', lazy=True)
    calendar = db.relationship('Calendar', backref='author', lazy=True)
    comments = db.relationship('Comments', backref='author', lazy=True)
    codes = db.relationship('Code', backref='author', lazy=True)
    roles = db.Column(db.Integer, db.ForeignKey('role.id'))
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    title = db.Column(db.String(300), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    content = db.Column(db.Text, nullable=False)
    brief = db.Column(db.String(300), default='Vào xem thì biết!')
    comments = db.Column(db.Integer,default=0)
    views = db.Column(db.Integer, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    image_cover = db.Column(db.String(500), default='cover_post')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tags = db.Column(db.String(200), default='khongco')
    like = db.Column(db.Integer, default=0)
    dislike = db.Column(db.Integer, default=0)
    def __repr__(self):
        return f"Post('{self.title}', '{self.date}')"
    @staticmethod
    def generate_slug(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)
db.event.listen(Post.title, 'set',Post.generate_slug, retval=False)

class Comments(db.Model):
    commnet_id = db.Column(db.Integer, primary_key=True)
    like = db.Column(db.Integer, default=0)
    dislike = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    username = db.Column(db.String(50), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id', ondelete='CASCADE'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    post = db.relationship('Post', backref=db.backref('posts', lazy=True, passive_deletes=True))
    date_comment = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return '<Post %r' % self.username

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    posts = db.relationship('Post', backref='category', lazy=True)
    def __repr__(self):
        return f"Category('{self.name}')"

class Code(db.Model):
    code_id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    def __repr__(self) -> str:
        return f"Code('{self.code_id}', '{self.date}')"

class Category_calendar(db.Model):
    category_calendar_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    calendar = db.relationship('Calendar', backref='category', lazy=True)
    def __repr__(self):
        return f"Category_Calendar('{self.name}')"

class Calendar(db.Model):
    calendar_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category_calendar.category_calendar_id'))
    start = db.Column(db.String(20), nullable=False)
    end = db.Column(db.String(20), nullable=False)
    def __repr__(self) -> str:
        return f"Calendar('{self.calendar_id}', '{self.content}')"

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(20), unique=True, nullable=False)
    user = db.relationship('User', backref='role', lazy=True)


class MyModelView(ModelView):

    def is_accessible(self):
        if not current_user.is_authenticated:
            return False

        if current_user.role.name == 'admin':
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('users.login', next=request.url))

    edit_modal = True
    create_modal = True    
    can_export = True
    can_view_details = True
    details_modal = True
