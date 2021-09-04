from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length
from wtforms.fields import SubmitField, StringField, PasswordField
from flask_ckeditor import CKEditorField
from Svute_Flask.models import Pages

class NewPage(FlaskForm):
    title = StringField('Tiêu đề', validators=[DataRequired(message="Tiêu đề không được để trống!"), Length(min=1, max=100, message='Tiêu đề quá dài!')])
    slug = StringField('Đường dẫn', validators=[DataRequired(message="Đường dẫn không được để trống!"), Length(min=1, max=100, message='Tiêu đề quá dài!')])
    content = CKEditorField('Nội dung...', validators=[DataRequired(message="Nội dung không được để trống!")])
    thumbnail = FileField('Tải lên ảnh thumbnail', validators=[FileAllowed(['jpg', 'png','jpeg'], message="Chỉ tải lên các định dạng ('.jpg', '.png', '.jpeg')")])
    password = StringField('Mật khẩu (nếu có)', validators=[Length(max=100, message='Mật khẩu quá dài!')])
    submit = SubmitField('Tạo trang mới')

    def validate_slug(self, slug):
        page = Pages.query.filter_by(slug=slug.data).first()
        if page:
            raise page('Đường dẫn đã tồn tại.','error')

class UnlockPage(FlaskForm):
    password = PasswordField('Vui lòng nhập mật khẩu để mở...', validators=[DataRequired(message="Mật khẩu không được để trống!"),Length(max=100, message='Mật khẩu quá dài!')])
    submit = SubmitField('Mở khóa')

class EditPage(FlaskForm):
    title = StringField('Tiêu đề', validators=[DataRequired(message="Tiêu đề không được để trống!"), Length(min=1, max=100, message='Tiêu đề quá dài!')])
    slug = StringField('Đường dẫn', validators=[DataRequired(message="Đường dẫn không được để trống!"), Length(min=1, max=100, message='Tiêu đề quá dài!')])
    content = CKEditorField('Nội dung...', validators=[DataRequired(message="Nội dung không được để trống!")])
    thumbnail = FileField('Tải lên ảnh thumbnail', validators=[FileAllowed(['jpg', 'png','jpeg'], message="Chỉ tải lên các định dạng ('.jpg', '.png', '.jpeg')")])
    password = StringField('Mật khẩu (nếu có)', validators=[Length(max=100, message='Mật khẩu quá dài!')])
    submit = SubmitField('Chỉnh sửa')