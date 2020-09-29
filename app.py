import os
from flask import Flask, request, render_template, redirect, flash, session, g

from models import db, connect_db, GuestbookEntry
from forms import GuestbookEntryForm
# from forms import LoginForm, UserForm, QuestionForm
from datetime import datetime

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres:///guestbook_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'oh-so-secret'

connect_db(app)

@app.route('/')
def home_route():
    """Home route"""
    form = GuestbookEntryForm()
    if form.validate_on_submit():
        print(f'Name: {form.name.data}')
        print(f'Name: {form.message.data}')
        
        try:
            new_entry = GuestbookEntry(
                name=form.name.data,
                message=form.message.data
            )
            db.session.commit()
        except:
            flash("Unexpected error. Please try again!")
            return render_template('home.html', form=form)

        return render_template('thank_you.html', name=form.name.data)

    else:
        return render_template('home.html', form=form)

