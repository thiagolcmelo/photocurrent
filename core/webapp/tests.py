import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from webapp import app, db
from author.models import *
from blog.models import *

class UserTest(unittest.TestCase):
    def setUp(self):
        db_user = app.config['DB_USERNAME']
        db_pass = app.config['DB_PASSWORD']
        db_host = app.config['DB_HOST']
        db_name = 'test_blog'
        self.db_uri = "mysql+pymysql://%s:%s@%s/" % (db_user, db_pass, db_host)
        
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['BLOG_DATABASE_NAME'] = db_name
        app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri + db_name
        
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute("commit")
        conn.execute("CREATE DATABASE %s" % db_name)
        db.create_all()
        conn.close()
        
        self.app = app.test_client()
    
    def tearDown(self):
        db.session.remove()
        # db.drop_all()
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute("commit")
        conn.execute("DROP DATABASE %s" % app.config['BLOG_DATABASE_NAME'])
        conn.close()
        
    def create_blog(self):
        return self.app.post(
                '/setup', data=dict(
                    name='My blog test',
                    fullname='Thiago Melo',
                    email='thiago.lc.melo@gmail.com',
                    username='thiagolcmelo',
                    password='1234',
                    confirm='1234'
                ), follow_redirects=True
            )
    
    def login(self, username, password):
        return self.app.post('/login', data=dict(
                username=username, password=password
            ), follow_redirects=True)
    
    def logout(self):
        return self.app.get('/logout', follow_redirects=True)
    
    def test_create_blog(self):
        rv = self.create_blog()
        self.assertIn(b'Blog created', rv.data)
    
    def test_login_logout(self):
        self.create_blog()
        rv = self.login('thiagolcmelo', '1234')
        self.assertIn(b'User thiagolcmelo logged in', rv.data)
        rv = self.logout()
        self.assertIn(b'User logged out', rv.data)
        rv = self.login('thiagolcmelo', '12345')
        self.assertIn(b'Incorrect username and password', rv.data)
        
if __name__ == '__main__':
    unittest.main()