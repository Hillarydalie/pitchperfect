from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,StringField,SelectField
from wtforms.validators import Required
from ..models import Post,Comment

class PostForm(FlaskForm):
    pitchtitle = TextAreaField('Pitch Title', validators=[Required])
    pitchdescription = TextAreaField('Pitch Description', validators=[Required])
    pitchcategory = SelectField('Pitch Category', choices = [('Technology', 'Technology'),('Health','Health'),('Nutrition','Nutrition')], validators=[Required])
    submit = SubmitField('Submit Pitch')

class CommentForm(FlaskForm):
    commentdescription = TextAreaField('Pitch Description', validators=[Required])
    submit = SubmitField('Submit Comment')