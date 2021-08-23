##################### IMPORT #####################
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo
from Svute_Flask.models import User
from werkzeug.security import generate_password_hash, check_password_hash



class Register_Form(FlaskForm):
    '''FORM ĐĂNG KÝ TÀI KHOẢN'''
    username = StringField('Tên người dùng', validators=[DataRequired(message='Tên tài khoản không được để trống!'), Length(min=2, max=20, message='Tên tài khoản từ 2 đến 20 ký tự!')])
    password = PasswordField('Mật khẩu', validators=[DataRequired(message='Mật khẩu không được để trống'), Length(min=6, max=50, message='Mật khẩu có độ dài từ 6 đến 50 ký tự!')])
    confirm_password = PasswordField('Xác nhận mật khẩu',validators=[DataRequired(), EqualTo('password')])
    fullname = StringField('Họ và tên', validators=[DataRequired(message='Họ và tên không được để trống!'), Length(min=2, max=50, message='Tên tài khoản từ 2 đến 50 ký tự!')])
    email = StringField('Email', validators=[DataRequired(message='Email không được để trống!'), Email(message="Địa chỉ email không hợp lệ!")])
    submit = SubmitField('Đăng ký')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Tên người dùng đã tồn tại, vui lòng chọn tên khác.','error')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email đã tồn tại, vui lòng chọn tên khác.','error')


class Login_Form(FlaskForm):
    '''FORM ĐĂNG NHẬP'''
    username = StringField('Tài khoản', validators=[DataRequired(message='Tên tài khoản không được để trống!'), Length(min=2, max=20, message='Tên tài khoản từ 2 đến 20 ký tự!')])
    password = PasswordField('Mật khẩu', validators=[DataRequired(message='Mật khẩu không được để trống'), Length(min=6, max=50, message='Mật khẩu có độ dài từ 6 đến 50 ký tự!')])
    remember = BooleanField('Ghi nhớ tài khoản')
    submit = SubmitField('Đăng nhập')



class Update_Account_Form(FlaskForm):
    '''LỚP CẬP NHẬT NGƯỜI DÙNG'''
    username = StringField('Tài khoản', validators=[DataRequired(message="Tên người dùng không được để trống"), Length(min=2, max=20)])
    #fullname = StringField('Họ', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(message="Email không được để trống"), Email()])
    picture = FileField('Cập nhật ảnh đại diện', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Cập nhật')
    fb_link = StringField('Đường dẫn Facebook',validators=[Length(max=50)])
    tw_link = StringField('Đường dẫn Twitter',validators=[Length(max=50)])
    git_link = StringField('Đường dẫn Github',validators=[Length(max=50)])
    web_link = StringField('Đường dẫn website',validators=[Length(max=50)])
    password = PasswordField('Mật khẩu', validators=[Length(max=50, message='Mật khẩu có độ dài từ 6 đến 50 ký tự!')])
    confirm_password = PasswordField('Xác nhận mật khẩu',validators=[EqualTo('password')])
    about = TextAreaField('Giới thiệu về bạn...',validators=[Length(max=500, message='Tóm tắt ngắn ngọn thôi bạn :D')])
    def validate_username(self, username):
        '''HÀM XÁC NHẬN CÓ TỒN TẠI USERNAME HAY CHƯA.'''
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Tên người này đã tồn tại.')

    def validate_email(self, email):
        '''HÀM XÁC NHẬN CÓ TỒN TẠI EMAIL HAY CHƯA.'''
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('Địa chỉ email này đã tồn tại.')

