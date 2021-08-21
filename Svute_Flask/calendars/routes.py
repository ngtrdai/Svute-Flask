from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from Svute_Flask.calendars.form import ToDoForm
from Svute_Flask.models import Calendar, Category_calendar
from Svute_Flask import db

calendars = Blueprint('calendars', __name__)


@calendars.route('/sukien', methods=['POST', 'GET'])
@login_required
def calendar():
    form = ToDoForm()
    form.category.choices = [category.name for category in Category_calendar.query.all()]
    events = []
    calendars = Calendar.query.filter_by(user_id = current_user.id).all()
    for calendar in calendars:
        event = {
            'todo': calendar.content,
            'start': calendar.start,
            'end': calendar.end,
        }
        events.append(event)
    if form.validate_on_submit():
        calendar = Calendar(user_id=current_user.id,
                            category = Category_calendar.query.filter_by(name = form.category.data).first(),
                            content = form.content.data, 
                            start = str(form.start_date.data) +'T'+ str(form.start_time.data),
                            end = str(form.end_date.data) +'T'+ str(form.end_time.data)
                            )
        db.session.add(calendar)
        db.session.commit()
        flash('Thêm công việc thành công!', 'success')
        return redirect(url_for('calendars.calendar'))
    return render_template('calendar.html', user=current_user, events=events, form = form, calendars = calendars)

@calendars.route('/sukien/xoa', methods=['POST', 'GET'])
@login_required
def deleteToDo():
    calendar_id = request.form.get("calendar_id")
    calendar = Calendar.query.get(calendar_id)
    if calendar:
        if calendar.user_id == current_user.id:
            db.session.delete(calendar)
            db.session.commit()
    return redirect(url_for('calendars.calendar'))