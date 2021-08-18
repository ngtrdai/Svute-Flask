from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, TextAreaField, DateField, SelectField, StringField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField, TimeField

class ToDoForm(FlaskForm):
    content = TextAreaField('Nhập công việc cần làm...', validators=[DataRequired(message="Nội dung không được để trống!"), Length(min=2,max=255, message='Tiêu đề quá dài!')])
    category = SelectField('Trạng thái', validators=[DataRequired()])
    start_date = DateField(id='start_date')
    start_time = TimeField(id='start_time')
    end_date = DateField(id='end_date')
    end_time = TimeField(id='end_time')
    submit =SubmitField('Nhập')