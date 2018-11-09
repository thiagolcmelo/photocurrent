from webapp import app, bcrypt, db
from flask import render_template, redirect, url_for, session, request, flash
from author.form import RegisterForm, LoginForm
from author.models import Author
from author.decorators import login_required

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    
    if request.method == 'GET' and request.args.get('next', None):
        session['next'] = request.args.get('next', None)
        
    if form.validate_on_submit():
        author = Author.query.filter_by(
                username=form.username.data
            ).first()
        if author:
            if bcrypt.check_password_hash(author.password, form.password.data):
                session['username'] = form.username.data
                session['is_author'] = author.is_author
                flash('User %s logged in' % author.username)
                if 'next' in session:
                    next = session['next']
                    session.pop('next')
                    return redirect(next)
                return redirect(url_for('index'))
            else:
                error = "Incorrect username and password"
        else:
            error = "Incorrect username and password"
    return render_template("author/login.html", form=form, error=error)
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('login', next=url_for('admin')))
    return render_template('author/register.html', form=form)


@app.route('/logout')
def logout():
    session.pop('username')
    session.pop('is_author')
    flash("User logged out")
    return redirect(url_for('index'))