from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired,url
from wtforms import ValidationError
from wtforms.fields.html5 import URLField


class BookmarkForm(Form):
    url = URLField('url', validators=[DataRequired(), url()])
    description = StringField('Description' )
    

def validate(self):
    if not self.url.data.startwith('http://') or \
            self.url.data.startswith('http://'):
            self.url.data = 'http://' + self.url.data

    if not Form.validate(self):
        return False
    if not self.description.data:
        self.description.data = self.url.data
    return True
  