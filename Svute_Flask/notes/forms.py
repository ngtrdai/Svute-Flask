from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class NoteForm(FlaskForm):
    title = StringField("Tiêu đề", validators=[DataRequired(message="Tiêu đề không được để trống!"), Length(max=150,message="Tiêu đề quá dài.")])
    content = TextAreaField("Nội dung", validators=[DataRequired(message="Tiêu đề không được để trống!"), Length(max=20000,message="Nội dung không được quá 20000 ký tự.")])
    submit = SubmitField('Ghi chú')