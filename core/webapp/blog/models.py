from datetime import datetime

from webapp import db, uploaded_images

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    admin = db.Column(db.Integer, db.ForeignKey('author.id'))
    posts = db.relationship('Post', backref='blog', lazy='dynamic')
    
    def __init__(self, name, admin):
        self.name = name
        self.admin = admin
    
    def __repr__(self):
        return "<Blog %r." % self.name

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    image = db.Column(db.String(256))
    slug = db.Column(db.String(256))
    publish_date = db.Column(db.DateTime)
    live = db.Column(db.Boolean)
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))
    
    @property
    def imgsrc(self):
        return uploaded_images.url(self.image)
    
    def __init__(self, blog, author, title, body, category, image=None, slug=None, publish_date=None, live=True):
        self.blog_id = blog.id
        self.author_id = author.id
        self.title = title
        self.body = body
        self.category_id = category.id
        self.image = image
        self.slug = slug
        self.publish_date = publish_date or datetime.utcnow()
        self.live = live
        
    def __repr__(self):
        return '<Post %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return '<Category %r>' % self.name
    
    def __str__(self):
        return self.name