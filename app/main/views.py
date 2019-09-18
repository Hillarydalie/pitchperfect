from flask import render_template,request,redirect,url_for
from flask_login import login_required,current_user
from datetime import datetime
from .. import db
from . import main
from ..models import User,Comment,Post
from .forms import PostForm,CommentForm

@main.route('/')
@login_required
def index():
    return render_template('index.html')

@main.route("/", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        # Get form filled details
        form = request.form
        title = form.get("title")
        category = form.get("radioselection")
        description = form.get("pitchdecription")
    return render_template('index.html')

@main.route("/home")
@login_required
def about():
    pitches = Post.query.all()
    return render_template("index.html", pitches=pitches)

@main.route("/home", methods=["GET","POST"])
def new_pitch():
    if request.method == "POST":
        form = request.form
        title = form.get("pitchtitle")
        category = form.get("pitchcategory")
        description = form.get("pitchdecription")
        post = Post(title=title, category=category, description = description, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('index.html')

@main.route('/pitch/details/<pitch_id>')
@login_required
def pitch_details(pitch_id):
    pitch = Post.query.filter_by(id = pitch_id ).first()
    comments = Comment.query.filter_by(id = pitch_id).all()
    return render_template('details.html',pitch = pitch , comments = comments)

    