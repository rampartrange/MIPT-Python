from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, login_required, logout_user
from flask import current_app as app
from datetime import datetime
from .models import db, User, Post, is_username_valid
from .forms import LoginForm, SignUpForm, ProfileEditForm, PostCreateForm


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = enumerate(Post.query.order_by(Post.timestamp.desc()).all(), 1)
    return render_template('index.html', title='Home', users=User.query.all(),
                           posts=enumerate(Post.query.order_by(Post.timestamp.desc()).all(), 1))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash(f'Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignUpForm()
    if form.validate_on_submit():
        if not is_username_valid(form.username.data):
            flash(f'Please choose another username')
            return redirect(url_for('sign_up'))

        user = User()
        user.set_username(form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>')
@login_required
def user_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(Post.timestamp.desc()).all()
    return render_template('user.html', user=user,
                           posts=enumerate(posts, 1))


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = ProfileEditForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash(f'Your profile information has been changed successfully')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.bio.data = current_user.bio
    return render_template('edit_profile.html', title='Edit Profile', form=form)


@app.route('/create_new_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostCreateForm()
    if form.validate_on_submit():
        post = Post(author=current_user)
        post.title = form.title.data
        post.text = form.text.data
        post.timestamp = datetime.utcnow()
        db.session.add(post)
        db.session.commit()
        flash(f'Post has been submitted!')
        return redirect(url_for('user_profile', username=current_user.username))
    return render_template('create_post.html', title='Create new post', form=form)


@app.route('/user/<username>/delete_post/<post_id>', methods=['GET', 'POST'])
@login_required
def delete_post(post_id, username=current_user):
    post = Post.query.filter_by(id=post_id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('user_profile', username=username))


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
