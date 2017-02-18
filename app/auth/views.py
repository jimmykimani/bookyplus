
from flask import Flask, render_template,url_for,request,redirect,url_for,flash,abort
# from thermo import auth, db,login_manager
# from models import User, Bookmark,Tag
from flask_login import login_required,login_user, logout_user, current_user
from forms import SigninForm, SignupForm
from .. import db
from .import auth
from ..models import Bookmark,User, Tag






@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()    
        flash("You have successfully registered! You may now login.")
        return redirect(url_for('auth.login'))
    return render_template('signup.html' , form=form)




@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash('Logged in successfully')
            return redirect(request.args.get('next') or url_for('main.index'
            ,username=user.username))
        flash('Invalid username or password.')
    return render_template('login.html', form=form)
 



@auth.route('/logout')
def logout():
    logout_user()
    # flash("You've been Logged out!")
    return render_template('base2.html',new_bookmarks=Bookmark.newest(5))







if __name__=='__main__':
    auth.run(debug=True)