from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo,url
from wtforms import ValidationError
from flask_wtf.html5 import URLField


class BookmarkForm(Form):
    url = URLField('url', validators=[DataRequired(), url()])
    description = StringField('Description', validators=[DataRequired()] )
    

def validate(self):
    if not self.url.data.startwith('http://') or \
            self.url.data.startswith('http://'):
            self.url.data = 'http://'+ self.url.data

    if not Form.validated(self):
        return False
    if not self.description.data:
        self.description.data = self.url.data
    return True
