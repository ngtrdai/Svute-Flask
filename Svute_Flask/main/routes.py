
from flask import render_template, request, Blueprint
from flask_login import login_required,current_user
from flask import flash, url_for, redirect,abort
from Svute_Flask.models import Note, Post, User, Calendar
from Svute_Flask import db, app
main = Blueprint('main', __name__)




@main.route("/")
@main.route("/trangchu")
def home():
    page = request.args.get('trang', 1, type=int)
    post = Post.query.order_by(Post.post_id.desc()).paginate(page=page,per_page=5)
    note = ""
    calendars =""
    if current_user.is_authenticated:
        calendars = Calendar.query.filter_by(user_id = current_user.id).all()
    try:
        note = Note.query.filter_by(user_id = current_user.id).order_by(Note.date.desc())
    except:
        pass

    return render_template('home.html', posts=post,notes=note ,user=current_user, title='Trang chủ', calendars = calendars)

@main.route("/thongtin")
def about():
    return render_template("about.html", user=current_user)


@main.route('/ads.txt')
def ads():
    return "google.com, pub-9154558574445919, DIRECT, f08c47fec0942fa0"