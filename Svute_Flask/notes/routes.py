##################### IMPORT #####################
from Svute_Flask.models import Note
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from Svute_Flask import db

notes = Blueprint('notes', __name__)

@notes.route('/ghichu', methods=['POST', 'GET'])
@login_required
def note():
    if request.method == "POST":
        if not request.form.get("title"):
            flash('Tiêu đề không được để trống', category='error')
        elif not request.form.get("note"):
            flash('Nội dung không được để trống', category='error')
        else:
            title = request.form.get("title")
            contentNote = request.form.get("note")
            note = Note(title = title, note=contentNote, user_id = current_user.id)
            db.session.add(note)
            db.session.commit()
            flash('Ghi chú thành công', category='success')
            return redirect('/ghichu')
    notes = current_user.notes
    return render_template("notes.html", notes = notes, user=current_user, title='Ghi chú')

@notes.route('/ghichu/xoa', methods=['POST'])
def delete_note():
    note_id = request.form.get("note_id")
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return redirect(url_for('notes.note'))

@notes.route('/ghichu/chinhsua', methods=['POST'])
def edit_note():
    upTitle = request.form.get("updateTitle")
    upNote = request.form.get("updateNote")
    noteID = request.form.get("noteID")
    note = Note.query.get_or_404(noteID)
    if note:
        if note.user_id == current_user.id:
            note.title = upTitle
            note.note = upNote
            db.session.commit()
    return redirect(url_for('notes.note'))