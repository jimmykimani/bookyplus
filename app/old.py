
# from flask import Flask, render_template,url_for,request,redirect,url_for,flash,abort
# from thermo import app, db,login_manager
# from models import User, Bookmark,Tag
# from flask_login import login_required,login_user, logout_user, current_user
# from forms import BookmarkForm, SigninForm, SignupForm, ChangePasswordForm

# @login_manager.user_loader
# def load_user(userid):
#     return User.query.get(int(userid))


# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     form = SignupForm()
#     if form.validate_on_submit():
#         user = User(email=form.email.data,
#                     username=form.username.data,
#                     password=form.password.data)
#         db.session.add(user)
#         db.session.commit()    
#         flash("You have successfully registered! You may now login.")
#         return redirect(url_for('login'))
#     return render_template('signup.html' , form=form)

# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html', new_bookmarks=Bookmark.newest(5))

# @app.route('/add', methods=['GET', 'POST'])
# @login_required
# def add():
#     form = BookmarkForm()
#     if form.validate_on_submit():
#         url = form.url.data
#         description = form.description.data
#         tags = form.tags.data
#         bm = Bookmark(user=current_user,url=url, description=description, tags=tags)
#         db.session.add(bm)
#         db.session.commit()
#         flash("Stored  '{}'".format(description))
#         return redirect(url_for('index'))
#     return render_template('add.html', form=form)


# @app.route('/user/<username>')
# def user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     return render_template('user.html',user=user)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = SigninForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is not None and user.check_password(form.password.data):
#             login_user(user, form.remember_me.data)
#             flash('Logged in successfully')
#             return redirect(request.args.get('next') or url_for('user'
#             ,username=user.username))
#         flash('Invalid username or password.')
#     return render_template('login.html', form=form)

# @app.route('/edit/<int:bookmark_id>', methods=['GET','POST'])
# @login_required
# def edit_bookmark(bookmark_id):
#     bookmark = Bookmark.query.get_or_404(bookmark_id)
#     if current_user != bookmark.user:
#         abort(403)
#     form = BookmarkForm(obj=bookmark)
#     if form.validate_on_submit():
#         form.populate_obj(bookmark)
#         db.session.commit()
#         flash('Your bookmark was saved succesfully')
#         return redirect(url_for('user', username=current_user.username))
#     return render_template('bookmark_form.html',form=form, title='Edit Bookmark')


# @app.route('/delete/<int:bookmark_id>', methods=['GET','POST'])
# @login_required
# def delete_bookmark(bookmark_id):
#     bookmark = Bookmark.query.get_or_404(bookmark_id)
#     if current_user != bookmark.user:
#         abort(403)
#     if request.method == "POST":
#         db.session.delete(bookmark)
#         db.session.commit()
#         flash( 'Deleted successfully')
#         return redirect(url_for('user', username=current_user.username))
#     else: 
#         flash( 'Please confirm delete ')
#     return render_template('confirm_delete.html',bookmark=bookmark, nolinks=True)

# @app.route('/change-password', methods=['GET', 'POST'])
# def change_password():
#     if not current_user.is_anonymous:
#         return redirect(url_for('main.index'))
#     form = ChangePasswordForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         flash('Invalid password.')     
#     form = ChangePasswordForm()
#     if form.validate_on_submit():
#         if current_user.verify_password(form.old_password.data):
#             current_user.password = form.password.data
#             db.session.add(current_user)
#             flash('Your password has been updated.')
#             return redirect(url_for('main.index'))
#         else:
#             flash('Invalid password.')
#     return render_template("change_password.html", form=form)    




# @app.route('/tag/<name>')
# def tag(name):
#     tag = Tag.query.filter_by(name=name).first_or_404()
#     return render_template('tag.html', tag=tag)


# @app.route('/logout')
# def logout():
#     logout_user()
#     flash("You've been Logged out!")
#     return redirect(url_for('index'))


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'),404


# @app.errorhandler(500)
# def server_error(e):
#     return render_template('500.html'),500

# @app.context_processor
# def inject_tags():
#     return dict(all_tags=Tag.all)


# if __name__=='__main__':
#     app.run(debug=True)