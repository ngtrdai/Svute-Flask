from flask_wtf import FlaskForm
from flask_codemirror.fields import CodeMirrorField
from wtforms.fields import SubmitField

class PostCode(FlaskForm):
    sourceCode = CodeMirrorField(language='python', config={'lineNumbers': 'true'})
    submit =SubmitField('Gửi')