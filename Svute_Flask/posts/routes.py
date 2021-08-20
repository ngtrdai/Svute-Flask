##################### IMPORT #####################
from Svute_Flask.models import Post, Comments, User, Category
from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from flask_login import current_user, login_required
from Svute_Flask import db
from Svute_Flask.users.func import SaveImage
from Svute_Flask.posts.forms import PostForm
posts = Blueprint('posts', __name__)

@posts.route('/bai-viet/moi', methods=['POST', 'GET'])
@login_required
def new_post():
    form = PostForm()
    form.category.choices = [category.name for category in Category.query.all()]
    if form.validate_on_submit():
        brief = form.brief.data
        if form.thumbnail.data:
            image_cover = SaveImage(form.thumbnail.data, True)
        else:
            image_cover = 'img33.jpg'
        if brief == "":
            brief = form.content.data[:200]

        post = Post(title=form.title.data, 
                    content=form.content.data, 
                    brief = brief,
                    category = Category.query.filter_by(name = form.category.data).first(), 
                    author=current_user, 
                    image_cover = image_cover,
                    tags = form.tags.data)
        db.session.add(post)
        db.session.commit()
        flash('Bài viết đã được đăng thành công, cảm ơn bạn!', 'success')
        return redirect(url_for('main.home'))
    return render_template('new_post.html', user=current_user, form = form )

@posts.route('/bai-viet/<string:slug>', methods=['POST','GET'])
def post(slug):
    post = Post.query.filter_by(slug=slug).first()
    comments = Comments.query.filter_by(post_id=post.post_id).all()
    post.views += 1
    tags = post.tags.split(',')
    db.session.commit()
    if request.method == "POST":
        post_id = post.post_id
        user_id = current_user.id
        message = request.form.get('message')
        user = User.query.filter_by(id = user_id).first()
        comment = Comments(user_id=user_id, content=message, username = user.username, post_id=post_id,author=current_user)
        db.session.add(comment)
        post.comments = post.comments + 1
        db.session.commit()
        flash('Cảm ơn bạn đã bình luận!', 'success')
        return redirect(url_for('posts.post', slug=post.slug))
    return render_template('posts.html', title = post.title, comments = comments,post = post, user=current_user, tags = tags)

@posts.route('/bai-viet/<string:slug>/chinhsua', methods=['POST', 'GET'])
@login_required
def update_post(slug):
    form = PostForm()
    post = Post.query.filter_by(slug=slug).first()
    form.category.choices = [category.name for category in Category.query.all()]
    if post.author != current_user:
        abort(403)
    if form.validate_on_submit():
        post.brief = form.brief.data
        if form.thumbnail.data:
            image_cover = SaveImage(form.thumbnail.data, True)
        else:
            image_cover = post.image_cover
        brief = form.brief.data
        if brief == "":
            brief = form.content.data[:200]
        else:
            post.brief = form.brief.data
        post.title = form.title.data
        post.content = form.content.data
        post.category = Category.query.filter_by(name = form.category.data).first()
        post.tag = form.tags.data
        post.image_cover = image_cover
        db.session.commit()
        flash('Chỉnh sửa bài viết thành công!', 'success')
        return redirect(url_for('posts.post', slug=post.slug))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.tags.data = post.tags
        form.category.choice = post.category
        if post.brief != post.content[:200]:
            form.brief.data = post.brief
        
    return render_template('new_post.html', user=current_user, form =form)

@posts.route('/baiviet/<int:post_id>/xoa', methods=['POST', 'GET'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Xóa bài viết thành công!', 'success')
    return redirect(url_for('main.home'))
