﻿##################### IMPORT #####################
from flask.templating import render_template_string
from Svute_Flask.models import User, Post
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from Svute_Flask import db, bcrypt
from Svute_Flask.users.forms import Update_Account_Form, Login_Form, Register_Form, RequestResetForm, ResetPasswordForm
from Svute_Flask.users.func import SaveImage, Send_Reset_Email

users = Blueprint('users', __name__)

@users.route('/dang-nhap', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form  = Login_Form()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash("Đăng nhập thành công!", 'success')
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.home'))
        else:
            flash('Đăng nhập thất bại, kiểm tra lại mật khẩu hoặc tên đăng nhập', 'error')
    return render_template('login.html', user=current_user, title="Đăng nhập", form = form  )

@users.route('/dang-xuat')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route('/dang-ky', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = Register_Form()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data ,fullname = form.fullname.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Tạo tài khoản thành công!', 'success')
        return redirect(url_for('users.login'))

    return render_template("register.html", user = current_user, title = 'Đăng ký', form = form)

@users.route('/caidat', methods=['POST', 'GET'])
@login_required
def settings():
    form = Update_Account_Form()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = SaveImage(form.picture.data, False)
            current_user.image_file = picture_file
        if form.password.data:
            current_user.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.fb_link = form.fb_link.data
        current_user.tw_link = form.tw_link.data
        current_user.web_link = form.web_link.data
        current_user.about = form.about.data
        db.session.commit()
        flash('Cập nhật thông tin thành công', category='success')
        return redirect(url_for('users.settings'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        if current_user.about != '#':
            form.about.data = current_user.about
        if current_user.fb_link != '#':
            form.fb_link.data = current_user.fb_link
        if current_user.tw_link != '#':
            form.tw_link.data = current_user.tw_link
        if current_user.web_link != '#':
            form.web_link.data = current_user.web_link
    return render_template("/settings/settings.html", user=current_user,title='Tài khoản', form=form)

@users.route('/quenmatkhau', methods=['POST', 'GET'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        Send_Reset_Email(user)
        flash('Chúng tôi đã gửi cho bạn một email có chưa đường link đổi mật khẩu!', category='success')
        return redirect(url_for('users.login'))

    return render_template('reset_password.html', user=current_user, title='Đặt lại mật khẩu', form = form)

@users.route('/quenmatkhau/<token>', methods=['POST', 'GET'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('Ơ token của bạn không đúng rồi!', category='error')
        return redirect(url_for('auth.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Đã cập nhật tài khoản thành công!', category='success')
        return redirect(url_for('users.login'))
    return render_template('reset_password_token.html', title='Đặt lại mật khẩu', user=current_user, form = form)

@users.route('/nguoidung/<string:username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    post = Post.query.filter_by(author =user)\
        .order_by(Post.date.desc())\
        .paginate(page=page,per_page=5)
    return render_template('user_post.html', posts=post, user=user)

@users.route('/bangdieukhien')
def uDashboard():

    return render_template('/settings/dashboard.html', user=current_user, title="Bảng điều khiển")    