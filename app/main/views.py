from flask import render_template
from flask_login import login_required
from . import main

@main.route('/')
@login_required
def index():
    return render_template('index.html')


@main.route('/about')
@login_required
def about():
    return render_template('about.html')

@main.route('/pitches')
@login_required
def pitches():
    return render_template('index.html')
    