from flask_wtf import FlaskForm
from flask_codemirror.fields import CodeMirrorField
from wtforms.validators import DataRequired, Length
from wtforms.fields import SubmitField, StringField, TextAreaField,SelectField, PasswordField

class PostCode(FlaskForm):
    title = StringField(validators=[Length(max=200, message="Tiêu đề quá dài!")])
    description = TextAreaField(validators=[Length(max=2000, message="Mô tả hơi dài :(")])
    sourceCode = TextAreaField()
    syntax = SelectField("Chọn ngôn ngữ",id="syntax" ,validators=[DataRequired(message="Không được để trống, nếu văn bản để Markdown")])
    password = StringField('Mật khẩu (nếu có)', validators=[Length(max=100, message='Mật khẩu quá dài!')])
    submit =SubmitField('Đăng')

class ViewCode(FlaskForm):
    title = StringField()
    description = TextAreaField()
    sourceCode = TextAreaField()

class EditCode(FlaskForm):
    title = StringField(validators=[Length(max=200, message="Tiêu đề quá dài!")])
    description = TextAreaField(validators=[Length(max=2000, message="Mô tả hơi dài :(")])
    sourceCode = TextAreaField()
    syntax = SelectField("Chọn ngôn ngữ",id="syntax" ,validators=[DataRequired(message="Không được để trống, nếu văn bản để Markdown")])
    password = StringField('Mật khẩu (nếu có)', validators=[Length(max=100, message='Mật khẩu quá dài!')])
    submit =SubmitField('Đăng')

class UnlockCode(FlaskForm):
    password = PasswordField('Vui lòng nhập mật khẩu để mở...', validators=[DataRequired(message="Mật khẩu không được để trống!"),Length(max=100, message='Mật khẩu quá dài!')])
    submit = SubmitField('Mở khóa')