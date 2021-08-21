from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from Svute_Flask.models import User
from flask_ckeditor import CKEditorField

class PostForm(FlaskForm):
    title = StringField('Tiêu đề', validators=[DataRequired(message="Tiêu đề không được để trống!"), Length(min=1, max=100, message='Tiêu đề quá dài!')])
    content = CKEditorField('Nội dung...', validators=[DataRequired(message="Nội dung không được để trống!")])
    category = SelectField('Chọn chuyên mục', validators=[DataRequired()])
    brief = TextAreaField('Tóm tắt ngắn gọn', validators=[Length(max=200, message='Tóm tắt quá dài!')])
    tags = StringField('Thẻ')
    thumbnail = FileField('Tải lên ảnh thumbnail', validators=[FileAllowed(['jpg', 'png','jpeg'], message="Chỉ tải lên các định dạng ('.jpg', '.png', '.jpeg')")])
    submit = SubmitField('Đăng bài')

class CommentForm(FlaskForm):
    comment = StringField("Nhập bình luận vào đây...", validators=[DataRequired(message="Bạn chưa nhập nội dung bình luận!")])
    submit = SubmitField('Đăng')