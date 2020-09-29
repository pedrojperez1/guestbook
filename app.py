import os
from flask import Flask, request, render_template, redirect, flash, url_for

from models import db, connect_db, GuestbookEntry
from forms import GuestbookEntryForm
# from forms import LoginForm, UserForm, QuestionForm
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres:///guestbook_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'oh-so-secret'

connect_db(app)

@app.route('/', methods=['GET', 'POST'])
def home_route():
    """Home route"""
    form = GuestbookEntryForm()
    if form.validate_on_submit():
        try:
            new_entry = GuestbookEntry(
                name=form.name.data,
                message=form.message.data
            )
            db.session.add(new_entry)
            db.session.commit()
        except:
            flash("Unexpected error. Please try again!")
            return render_template('home.html', form=form)

        return redirect(url_for('thank_you', name=form.name.data))

    else:
        return render_template('home.html', form=form)

@app.route('/thank_you', methods=['GET'])
def thank_you():
    """Thank you route"""
    name = request.args.get('name').split(' ')[0]

    return render_template('thank_you.html', name=name)