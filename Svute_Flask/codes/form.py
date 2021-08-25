from flask_wtf import FlaskForm
from flask_codemirror.fields import CodeMirrorField
from wtforms.validators import DataRequired, Length
from wtforms.fields import SubmitField, StringField, TextAreaField

class PostCode(FlaskForm):
    title = StringField(validators=[Length(max=200, message="Tiêu đề quá dài!")])
    description = TextAreaField(validators=[Length(max=2000, message="Mô tả hơi dài :(")])
    sourceCode = CodeMirrorField(language='python', config={'lineNumbers': 'true'})
    submit =SubmitField('Gửi')

class ViewCode(FlaskForm):
    title = StringField()
    description = TextAreaField()
    sourceCode = CodeMirrorField(language='python', config={'lineNumbers': 'true', 'readOnly': 'true'})