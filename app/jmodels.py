# -*- coding: utf-8 -*-
from models import Article, Group, Comment
from flask.json import JSONEncoder
import util
from dao import AuthorDao, GroupDao, CommentDao

authorDao = AuthorDao()
groupDao = GroupDao()

class JArticle():
    def __init__(self, article, isSingle):
        if isinstance(article, Article):
            self.id = article.id
            self.title = article.title.encode('utf-8')
            self.author = ''
            if article.author > 0:
                self.author = authorDao.getAuthorNameById(article.author).encode('utf-8')
            self.group = ''
            if article.group > 0:
                self.group_url = '/tags#tag_%s' % article.group
                self.group = groupDao.getGroupNameById(article.group).encode('utf-8')
            self.content = ''
            self.leading = ''
            if isSingle:
                self.content = article.content.encode('utf-8')
            else:
                self.leading = util.creatLeading(article.content).encode('utf-8')
            self.createTime = ''
            if article.create_time > 0:
                self.createTime = util.timeFromStamp(article.create_time)
            self.clicks = article.clicks
            self.comments = article.comments
            self.url='/at?id=%s' % self.id
        else:
            return None
    
    def __repr__(self):
        return '''<JArticle title = %s >''' % self.title

    def _to_json(self):
        return {
                "id":self.id, "title":self.title, "author":self.author,
                "group":self.group, "group_url":self.group_url, "content": self.content,
                "leading":self.leading, "create_time":self.createTime, "clicks":self.clicks,
                "comments":self.comments, "url":self.url
        }

    def _to_json_simple(self):
        return {
                "id": self.id, "title": self.title, "url": self.url,
                "create_time": self.createTime, "view_count": self.clicks}

class JGroup():
    def __init__(self, group):
        if isinstance(group, Group):
            self.id = group.id
            self.name = group.name.encode('utf-8')
            self.count = group.count
            self.createTime = ''
            self.url='/tags#tag_%s' % self.id
            if group.create_time > 0:
                self.createTime = util.timeFromStamp(group.create_time)
        else:
            return None
        
    def __repr__(self):
        return '''<JGroup name = %s >''' % self.name
    def _to_json(self):
        return { "id" : self.id, "name": self.name , "count": self.count,
                 "createTime": self.createTime, "url": self.url}

class JComment():
    def __init__(self, comment):
        if isinstance(comment, Comment):
            self.id = comment.id
            self.articleId = comment.article_id
            self.commenter = comment.commenter
            self.comment = comment.comment
            self.createTime = ''
            if comment.create_time > 0:
                self.createTime = util.timeFromStamp(comment.create_time)
            self.answer = comment.answer
            if comment.favorite > 0:
                self.favorite = comment.favorite
            else:
                self.favorite = False
        else:
            return None
    
    def __repr__(self):
        return '''<JComment id = %s>''' % self.id

    def _to_json(self):
        return { "id": self.id, "article_id": self.articleId, "commenter": self.commenter,
                "comment": self.comment, "create_time": self.createTime,
                "answer": self.answer ,"favorite_count": self.favorite}

class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, JArticle):
            return {
                    'id' : obj.id,
                    'title' : obj.title,
                    'author' : obj.author,
                    'group' : obj.group,
                    'leading': obj.leading,
                    'content' : obj.content,
                    'createTime' : obj.createTime,
                    'clicks' : obj.clicks,
                    'comments' : obj.comments,
            }
        if isinstance(obj, JGroup):
            return {
                    'id' : obj.id,
                    'name' : obj.name,
                    'count' : obj.count,
                    'createTime' : obj.createTime,
            }
        if isinstance(obj, JComment):
            return {
                    'id' : obj.id,
                    'articleId' : obj.articleId,
                    'commenter' : obj.commenter,
                    'comment' : obj.comment,
                    'createTime' : obj.createTime,
            }
        return super(MyJSONEncoder, self).default(obj)
    