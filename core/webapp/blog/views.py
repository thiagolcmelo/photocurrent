import re
from unicodedata import normalize
from webapp import app, bcrypt, db
from flask import render_template, redirect, flash, url_for, session, abort
from blog.form import SetupForm, PostForm
from blog.models import Blog, Post, Category
from author.models import Author
from author.decorators import login_required, author_required
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from slugify import slugify

POSTS_PER_PAGE = 5

@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page=1):
    blog = Blog.query.first()
    if not blog:
        return redirect(url_for('setup'))
    posts = Post.query.order_by(Post.publish_date.desc()).paginate(page, POSTS_PER_PAGE, False)
    return render_template('blog/index.html', blog=blog, posts=posts)

@app.route('/admin')
@app.route('/admin/<int:page>')
@author_required
def admin(page=1):
    if session.get('is_author'):
        posts = Post.query.order_by(Post.publish_date.desc()).paginate(page, POSTS_PER_PAGE, False)
        return render_template('blog/admin.html', posts=posts)
    abort(403)

@app.route('/setup', methods=['POST', 'GET'])
def setup():
    form = SetupForm()
    error = ""
    if form.validate_on_submit():
        author = Author(
                form.fullname.data,
                form.email.data,
                form.username.data,
                bcrypt.generate_password_hash(form.password.data),
                True
            )
        db.session.add(author)
        db.session.flush()
        if author.id:
            blog = Blog(
                    form.name.data,
                    author.id
                )
            db.session.add(blog)
            db.session.flush()
            if author.id and blog.id:
                db.session.commit()
                flash("Blog created")
                return redirect(url_for("admin"))
            else:
                error = "Error creating blog"
                db.session.rollback()
        else:
            error = "Error creating author"
            db.session.rollback()
    return render_template("blog/setup.html", form=form, error=error)

@app.route('/post', methods=['POST', 'GET'])
@author_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        if form.new_category.data:
            new_category = Category(form.new_category.data)
            db.session.add(new_category)
            db.session.flush()
            category = new_category
        elif form.category.data:
            category_id = form.category.get_pk(form.category.data)
            category = Category.query.filter_by(id=category_id).first()
        else:
            category = None
        blog = Blog.query.first()
        author = Author.query.filter_by(username=session['username']).first()
        title = form.title.data
        body = form.body.data
        slug = slugify(title)
        post = Post(blog, author, title, body, category, slug)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('article', slug=slug))
            
    return render_template('blog/post.html', form=form)

@app.route('/article/<slug>')
def article(slug):
    post = Post.query.filter_by(slug=slug).first()
    return render_template("blog/article.html", post=post)