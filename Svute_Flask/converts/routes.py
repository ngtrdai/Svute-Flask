from flask import render_template, url_for, flash, redirect, request, Blueprint,send_from_directory
from Svute_Flask.converts.imgtopdf.xuly import chuyendoi_img2pdf
import os
from flask_login import current_user, login_required
from Svute_Flask import db, app
from werkzeug.utils import secure_filename
import urllib.request

converts = Blueprint('converts', __name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@converts.route('/congcu')
@login_required
def tools():
    return render_template('tools.html', user=current_user)

@converts.route('/congcu/img-pdf',methods=['POST','GET'])
@login_required
def imgtopdf():
    if request.method == 'POST':
        if 'files[]' not in request.files:
            flash('Không có ảnh nào được tải lên!', category='warning')
            return redirect(url_for('converts.imgtopdf'))
        files = request.files.getlist('files[]')
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.root_path,'static/assets/img/tools', filename)) 
        flash('File(s) successfully uploaded')
        chuyendoi_img2pdf(files)
    return render_template('tools_imgtopdf.html', user=current_user)

@converts.route('/random')
def random():
    return render_template('Utilities/random.html', user=current_user)