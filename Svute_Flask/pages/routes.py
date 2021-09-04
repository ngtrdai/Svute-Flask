from Svute_Flask.users.func import SaveImage
from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from sqlalchemy.sql.expression import null
from Svute_Flask.models import Category, Post, Pages
from flask_login import current_user, login_required
from Svute_Flask.pages.forms import NewPage, UnlockPage, EditPage
from Svute_Flask import db
pages = Blueprint('pages', __name__)

@pages.route('/chuyenmuc/<string:slug>', methods=['POST','GET'])
def category(slug):
    topPosts = Post.query.order_by(Post.views.desc()).limit(3).all()
    lastPosts = Post.query.order_by(Post.post_id.desc()).limit(3).all()
    page = request.args.get('trang', 1, type=int)
    category = Category.query.filter_by(slug=slug).first()
    hasPost = False if len(category.posts) == 0 else True
    posts = Post.query.filter_by(category_id=category.category_id).order_by(Post.post_id.desc()).paginate(page=page,per_page=5)
    return render_template('pages/categorys.html', user=current_user, posts = posts, title=category.name, hasPost = hasPost, topPosts = topPosts, lastPosts = lastPosts)

@pages.route('/trang/moi', methods=['POST', 'GET'])
@login_required
def newPage():
    if current_user.is_authenticated and current_user.role.name == "admin":
        form = NewPage()
        if form.validate_on_submit():
            title = form.title.data
            content = form.content.data
            slug = form.slug.data
            if form.thumbnail.data:
                image_cover = SaveImage(form.thumbnail.data, True)
            else:
                image_cover = '../static/assets/img/posts/thumbnail_backg.svg'
            if form.password.data:
                page = Pages(title = title, content = content, thumbnail = image_cover ,password = form.password.data, slug = slug)
            else:
                page = Pages(title = title, content = content, thumbnail = image_cover, slug = slug)
            db.session.add(page)
            db.session.commit()
            flash("Tạo trang thành công!", category="success")
            return redirect(url_for('pages.viewPage', slug = slug))
        return render_template('pages/new.html', user=current_user, title = "Trang mới", form=form)
    else:
        flash("Bạn không có quyền truy cập!", category="warrning")
        return redirect(url_for('#'))


@pages.route('/trang/<string:slug>', methods=['POST', 'GET'])
def viewPage(slug):
    form = UnlockPage()
    page = Pages.query.filter_by(slug=slug).first()
    if page:
        if page.password != None:
            if form.validate_on_submit():
                if form.password.data == page.password:
                    return render_template("pages/index.html", page=page, user=current_user, title=page.title)
                else:
                    flash("Mật khẩu không chính xác!", "error")
            return render_template("pages/lock.html", page=page,form=form ,user=current_user, title=page.title)
        else:
            return render_template("pages/index.html", page=page, user=current_user, title=page.title)  
    else:
        abort(404)
            
@pages.route("/trang/<string:slug>/sua", methods=["GET", "POST"])
def editPage(slug):
    form = EditPage()
    page = Pages.query.filter_by(slug=slug).first()
    if page:
        if current_user.is_authenticated and current_user.role.name == "admin":
            if form.validate_on_submit():
                page.title = form.title.data
                page.content = form.content.data
                page.slug = form.slug.data
                if form.thumbnail.data:
                    page.thumbnail = SaveImage(form.thumbnail.data, True)
                if form.password.data:
                    page.password = form.password.data
                db.session.commit()
                flash("Chỉnh sửa thành công!", "success")
                return redirect(url_for('pages.viewPage', slug=page.slug))
            form.title.data = page.title
            form.content.data = page.content
            form.slug.data = page.slug
            form.password.data = page.password
            return render_template("pages/new.html", form=form, user=current_user, title=page.title)
        else:
            flash("Bạn không có quyền truy cập", "error")
            return redirect(url_for('main.home'))
    else:
        abort(404)
