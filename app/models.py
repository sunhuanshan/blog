# -*- coding: utf-8 -*-
from app import db

ROLE_USER  = 0
ROLE_ADMIN = 1


class Author(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100), index = True, unique = True)
    passwd = db.Column(db.String(100))
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    #articles = db.relationship('Article', backref = 'author', lazy = 'dynamic')

    def __repr__(self):
        return '<User id= %s, name= %s>' % (self.id, self.name.encode('utf-8'))
    

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True)
    author = db.Column(db.Integer, default = 0)
    group = db.Column(db.Integer, default = 0)
    content = db.Column(db.Text)
    create_time = db.Column(db.Integer, default = 0)
    clicks = db.Column(db.Integer, default = 0)
    comments = db.Column(db.Integer, default = 0)
    
    def __repr__(self):
        return '<Article id = %s, title = %s, author = %s, group = %s, createTime = %s, clicks = %s, comments = %s >' % (self.id, self.title.encode('utf-8'), self.author, self.group, self.create_time, self.clicks, self.comments)
        #return '<Article id = %s>' % (self.id)

class Group(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), index = True)
    count = db.Column(db.Integer, default = 0)
    create_time = db.Column(db.Integer, default = 0)
    
    def __repr__(self):
        return '<Group id = %s, name = %s>' % (self.id, self.name.encode('utf-8'))

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    article_id = db.Column(db.Integer, index = True)
    comment = db.Column(db.Text)
    commenter = db.Column(db.String(100))
    create_time = db.Column(db.Integer, default = 0)
    
    def __repr__(self):
        return '<Comment id = %s, article_id = %s, commenter = %s >' % (self.id, self.article_id, self.commenter)

    