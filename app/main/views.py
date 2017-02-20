from flask import render_template, flash, redirect, request, url_for
from flask_login import login_user, logout_user, login_required, current_user
from . import main
from .. import db,login_manager
from ..models import Bookmark,User, Tag


 


@main.route('/')
@main.route('/home')
def home():
    return render_template('base.html', new_bookmarks=Bookmark.newest(5))    


@main.route('/index')
@login_required
def index():
    return render_template('index.html', new_bookmarks=Bookmark.newest(5))



@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html',user=user)    