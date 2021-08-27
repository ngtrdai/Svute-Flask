from flask_wtf import FlaskForm
from flask_codemirror.fields import CodeMirrorField
from wtforms.validators import DataRequired, Length
from wtforms.fields import SubmitField, StringField, TextAreaField,SelectField

class PostCode(FlaskForm):
    title = StringField(validators=[Length(max=200, message="Tiêu đề quá dài!")])
    description = TextAreaField(validators=[Length(max=2000, message="Mô tả hơi dài :(")])
    sourceCode = TextAreaField()
    syntax = SelectField("Chọn ngôn ngữ",id="syntax" ,validators=[DataRequired(message="Không được để trống, nếu văn bản để Markdown")])
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
    submit =SubmitField('Đăng')