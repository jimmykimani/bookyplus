from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,url,Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from wtforms.fields.html5 import URLField
from models import User

class BookmarkForm(Form):
    url = URLField('url', validators=[DataRequired(), url()])
    description = StringField('Description' )
    submit = SubmitField('Add')
    tags = StringField('Tags', validators=[ Regexp('^[A-Za-z][A-Za-z0-9.]_*$', 0,
                                          'Tags can only contain letters and numbers')]

    def validate(self):
        if not self.url.data.startswith('http://') or\
            self.url.data.startswith('https://'):
            self.url.data = 'http://' + self.url.data

        if not Form.validate(self):
            return False
        if not self.description.data:
            self.description.data = self.url.data
        return True


class SigninForm(Form):
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class SignupForm(Form):
    
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                           Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(3, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[ DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError('Username already in use.')
