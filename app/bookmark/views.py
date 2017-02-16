from flask import Flask, render_template,url_for,request,redirect,url_for,flash,abort
from flask_login import login_required,login_user, logout_user, current_user
from . import bookmark
from forms import BookmarkForm
from ..models import User, Bookmark,Tag
from ..import db,app
from .. import models



@bookmark.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        tags = form.tags.data
        bm = Bookmark(user=current_user,url=url, description=description, tags=tags)
        db.session.add(bm)
        db.session.commit()
        flash("Stored  '{}'".format(description))
        return redirect(url_for('main.index'))
    return render_template('add.html', form=form)




@bookmark.route('/edit/<int:bookmark_id>', methods=['GET','POST'])
@login_required
def edit_bookmark(bookmark_id):
    bookmark = Bookmark.query.get_or_404(bookmark_id)
    if current_user != bookmark.user:
        abort(403)
    form = BookmarkForm(obj=bookmark)
    if form.validate_on_submit():
        form.populate_obj(bookmark)
        db.session.commit()
        flash('Your bookmark was saved succesfully')
        return redirect(url_for('main.user', username=current_user.username))
    return render_template('bookmark_form.html',form=form, title='Edit Bookmark')


@bookmark.route('/delete/<int:bookmark_id>', methods=['GET','POST'])
@login_required
def delete_bookmark(bookmark_id):
    bookmark = Bookmark.query.get_or_404(bookmark_id)
    if current_user != bookmark.user:
        abort(403)
    if request.method == "POST":
        db.session.delete(bookmark)
        db.session.commit()
        flash( 'Deleted successfully')
        return redirect(url_for('main.user', username=current_user.username))
    else: 
        flash( 'Please confirm delete ')
    return render_template('confirm_delete.html',bookmark=bookmark, nolinks=True)

@bookmark.route('/tag/<name>')
def tag(name):
    tag = Tag.query.filter_by(name=name).first_or_404()
    return render_template('tag.html', tag=tag)

@app.context_processor
def inject_tags():
    return dict(all_tags=Tag.all)  