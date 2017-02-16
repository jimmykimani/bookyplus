# from flask_wtf import Form
# from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import DataRequired,url,Length, Email, Regexp, EqualTo
# from wtforms import ValidationError
# from wtforms.fields.html5 import URLField
# from models import User

# class BookmarkForm(Form):
#     url = URLField('Enter your url:', validators=[DataRequired(), url()])
#     description = StringField('Enter Description:' )
#     tags = StringField('Tags', validators=[Regexp(r'^[a-zA-Z0-9, ]*$', message=
#     'Tags can only contain letters and numbers')])
#     submit = SubmitField('Save')


#     def validate(self):
#         if not self.url.data.startswith("http://") or\
#             self.url.data.startswith("https://"):
#             self.url.data = "" + self.url.data

#         if not Form.validate(self):
#             return False
#         if not self.description.data:
#             self.description.data = self.url.data
        
#         stripped = [t.strip() for t in self.tags.data.split(',')]
#         not_empty = [tag for tag in stripped if tag]
#         tagset = set(not_empty)
#         self.tags.data = ",".join(tagset)

#         return True






# class ChangePasswordForm(Form):
#     username = StringField('Username', validators=[
#     DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
#                                         'Usernames must have only letters, '
#                                         'numbers, dots or underscores')])
#     old_password = PasswordField('Old password', validators=[DataRequired()])
#     password = PasswordField('New password', validators=[
#         DataRequired(), EqualTo('password2', message='Passwords must match')])
#     password2 = PasswordField('Confirm new password', validators=[DataRequired()])
#     submit = SubmitField('Reset Password')
    


