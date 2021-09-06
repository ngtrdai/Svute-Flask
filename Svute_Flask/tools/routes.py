from flask import render_template, url_for, flash, redirect, request, Blueprint,send_from_directory
from flask_login import current_user, login_required
from Svute_Flask.models import Encode, User
from Svute_Flask import db, app
from Svute_Flask.tools.forms import Encryption, Decryption
from secrets import token_hex
tools = Blueprint('tools', __name__)

@tools.route('/congcu')
@login_required
def listTools():
    return render_template('tools.html', user=current_user)

@tools.route('/random')
def random():
    return render_template('tools/random.html', user=current_user)

@tools.route('/encode', methods=['POST', 'GET'])
def encode():
    encryptionForm = Encryption()
    decryptionForm = Decryption()
    formid = request.args.get('formid', 1, type=int)
    if encryptionForm.validate_on_submit() and formid== 1:
        content = encryptionForm.content_en.data
        code = token_hex(5)
        if current_user.is_authenticated:
            encode = Encode(code = code, content = content, author = current_user)
        else:
            encode = Encode(code = code, content = content, author = User.query.filter_by(username='khach').first())
        db.session.add(encode)
        db.session.commit()
        flash("Mã hóa thành công!", "success")
        encryptionForm.code.data = code
        return render_template('tools/encode.html',decryptionForm=decryptionForm,code=code,encryptionForm=encryptionForm,content="", user=current_user, title = "Mã hóa nội dung")
    
    if decryptionForm.validate_on_submit() and formid== 1:
        code = decryptionForm.code.data
        encode = Encode.query.filter_by(code=code).first()
        if encode:
            content = encode.content
            decryptionForm.code.data = encode.code
            flash("Giải mã thành công!", "success")
            return render_template('tools/encode.html',encryptionForm=encryptionForm,content = content, user=current_user, title = "Mã hóa nội dung")
        flash("Chìa khóa không đúng!", "error")
        return redirect(url_for("tools.encode"))
    return render_template('tools/encode.html',encryptionForm=encryptionForm,decryptionForm=decryptionForm,content="", user=current_user, title = "Mã hóa nội dung")