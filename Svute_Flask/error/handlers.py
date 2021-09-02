from flask import Blueprint, render_template
from flask_login import current_user
errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html', user=current_user, title="404 - Không tìm thấy trang"), 404

@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/404.html',user=current_user, title="Lỗi 403"), 403

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/404.html',user=current_user, title="Lỗi 500"), 500