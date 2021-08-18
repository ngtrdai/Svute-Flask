from Svute_Flask.models import Code
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from Svute_Flask import db
from Svute_Flask.codes.form import PostCode

codes = Blueprint('codes', __name__)

@codes.route('/code')
def code():
    form = PostCode()
    if form.validate_on_submit():
        source = form.source.data
        code = Code(source = source, user_id = current_user.id, )
        db.session.add(code)
        db.session.commit()
        flash('Đăng code thành công!', 'success')
    
    return render_template('code.html', user=current_user, form = form, title = "Code")
