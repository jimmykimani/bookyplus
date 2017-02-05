from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo,url
from wtforms import ValidationError
from flask_wtf.html5 import URLField


class BookmarkForm(FlaskForm):
    url = URLField('url', validators=[Required(), url()])
    description = StringField('Description', validators=[Required()] )
    

