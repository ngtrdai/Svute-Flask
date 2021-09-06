from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email
from wtforms.fields import SubmitField, StringField, PasswordField, TextAreaField
from flask_ckeditor import CKEditorField

class Encryption(FlaskForm):
    code = StringField("Sử dụng chìa khóa này để giải mã!")
    content_en = CKEditorField('Nội dung...', validators=[DataRequired(message="Nội dung không được để trống!")])
    submit = SubmitField('Mã hóa')

class Decryption(FlaskForm):
    code = StringField("Nhập chìa khóa để giải mã!")
    content_de = StringField('Nội dung...')
    submit = SubmitField('Giải mã')