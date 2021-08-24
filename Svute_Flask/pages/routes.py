from flask import render_template, url_for, flash, redirect, request, Blueprint
from sqlalchemy.sql.expression import null
from Svute_Flask.models import Category, Post, User
from flask_login import current_user
pages = Blueprint('pages', __name__)

@pages.route('/chuyenmuc/<string:slug>', methods=['POST','GET'])
def category(slug):
    page = request.args.get('page', 1, type=int)
    category = Category.query.filter_by(slug=slug).first()
    hasPost = False if len(category.posts) == 0 else True
    posts = Post.query.filter_by(category_id=category.category_id).order_by(Post.post_id.desc()).paginate(page=page,per_page=5)

        
    return render_template('pages/categorys.html', user=current_user, posts = posts, title=category.name, hasPost = hasPost)