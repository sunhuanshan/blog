#! -*- coding : utf-8 -*-
from app import db
from models import Article, Author, Group, Comment
from logger import logger
from __builtin__ import isinstance
from itertools import count

class AuthorDao():

    def getAllAuthors(self):
        authorList = Author.query.all()
        return authorList

    def addAuthor(self, author):
        if author and isinstance(author, Author):
            db.session.add(author)
            db.session.commit()
            db.session.flush()
        #else:
    
    def getAuthorNameById(self, id):
        authorName = ''
        try:
            author = Author.query.filter_by(id = id).first()
            if author:
                authorName = author.name
        except Exception, e:
            logger.error('get author\'s name by id error %s' % e)
        return authorName
    
    def getAuthorByName(self, name):
        author = Author.query.filter_by(name = name).first()
        return author

    def removeAuthor(self, name):
        author = Author.query.filter_by(name = name).first()
        if author:
            db.session.delete(author)
            db.session.commit()
            db.session.flush()
        #else:
    
class ArticleDao():
    
    def getArticles(self):
        try:
            articles = Article.query.order_by(Article.create_time.desc()).all()
            return articles
        except Exception, e:
            logger.error(' get articles error %s', e)

    def getArticlesCount(self):
        try:
            count = Article.query.order_by(Article.create_time.desc()).count()
            return count
        except Exception, e:
            logger.error(' get articles count error %s', e)

    #def getArticlesByPage(self, start, limit):
    #    try:
    #        articles = Article.query.order_by(Article.create_time.desc()).get((start, limit))
    #        return articles
    #    except Exception, e:
    #        logger.error(' get a page articles error %s', e)


    def addArticle(self, art):
        try:
            db.session.add(art);
            db.session.flush();
            db.session.commit();
        except Exception, e:
            logger.error(' add article error %s', e)
    
    def getArticleByTitle(self, title):
        try:
            article = Article.query.filter_by(title = title).first()
            return article
        except Exception, e:
            logger.error(' get article by title error %s', e)
    
    def getArticlesByTime(self, timeBegin, timeEnd):
        try:
            arts = []
            articles = self.getArticles()
            for art in articles:
                if (art.create_time >=  timeBegin) and (art.create_time < timeEnd) :
                    arts.append(art)
            return arts
        except Exception, e:
            logger.error(' get article by create time error %s', e)
    
    def removeArticle(self, title):
        try:
            articles = Article.query.filter_by(title = title).all()
            for article in articles:
                db.session.delete(article)
            db.session.flush()
            db.session.commit()
        except Exception, e:
            logger.error(' remove article by title error %s', e)
    
    def removeArticleById(self, id):
        try:
            articles = Article.query.filter_by(id = id).all()
            for article in articles:
                db.session.delete(article)
            db.session.flush()
            db.session.commit()
        except Exception, e:
            logger.error(' remove article by id error %s', e)
    
    def getArticleById(self, id):
        try:
            articles = Article.query.filter_by(id = id).all()
            return articles
        except Exception, e:
            logger.error(' get article by id error %s', e)

    def getArticleByTitle(self, title):
        try:
            article = Article.query.filter_by(title = title).first()
            return article
        except Exception, e:
            logger.error(' get article by title error %s' % e)
        
    def addClickCount(self, id):
        try:
            article = Article.query.filter_by(id = id).first()
            if article:
                article.clicks = article.clicks + 1
                db.session.flush()
                db.session.commit()
        except Exception, e:
            logger.error(' add article clicks error %s ' % e)
            
    def addCommentCount(self, id):
        try:
            article = Article.query.filter_by(id = id).first()
            if article:
                article.comments = article.comments + 1
                db.session.flush()
                db.session.commit()
        except Exception, e:
            logger.error(' add article comments error %s' % e)
        
    def articlesByGroupId(self, id):
        try:
            articles = Article.query.filter_by(group = id).all()
            return articles 
        except Exception, e:
            logger.error('get articles by gtoup id error %d' % e)
        
class GroupDao():
    
    def getGroups(self):
        try:
            groups = Group.query.all()
            return groups
        except Exception, e:
            logger.error('get groups error %s ' % e)
            
    def getGroupById(self, id):
        try:
            group = Group.query.filter_by(id = id).first()
            return group
        except Exception, e:
            logger.error('get group by id error %s' % e)
    
    def getGroupNameById(self, id):
        groupName = ''
        try:
            group = Group.query.filter_by(id = id).first()
            if group:
                groupName = group.name
        except Exception, e:
            logger.error('get group name by id error %s' % e)
        return groupName
    
    def addGroup(self, group):
        try:
            if isinstance(group, Group):
                db.session.add(group)
                db.session.flush()
                db.session.commit()
            else:
                raise Exception('group is not a instance of Group')
        except Exception, e:
            logger.error('add group error %s' % e)
    
    def getGroupByName(self, name):
        try:
            group = Group.query.filter_by(name = name).first()
            return group
        except Exception, e:
            logger.error('get group by name error %s' % e)
            
    def removeGroup(self, name):
        try:
            group = Group.query.filter_by(name = name).first()
            if group:
                db.session.delete(group)
                db.session.flush()
                db.session.commit()
        except Exception, e:
            logger('remove group error %s' % e)
            
    def getGroupById(self, id):
        try:
            gp = Group.query.filter_by(id = id).first()
            return gp
        except Exception, e:
            logger.error('get group by id error %s' % e)
    
    def addGroupCount(self, id):
        try:
            gp = Group.query.filter_by(id = id).first()
            if gp:
                gp.count = gp.count +1
                db.session.flush()
                db.session.commit()
        except Exception, e:
            logger.error('add group count error %s' % s)
    
    def updateGroupCount(self, id, count):
        try:
            gp = Group.query.filter_by(id = id).first()
            if gp:
                gp.count = count
                db.session.flush()
                db.session.commit()
        except Exception, e:
            logger.error('update group count error %s' % e)
    
class CommentDao():
    
    def getCommentsByArticleId(self, articleId):
        try:
            coms = Comment.query.filter_by(article_id = articleId).order_by(Comment.article_id).all()
            return coms
        except Exception, e:
            logger.error('get comments by article error %s ' % e)
            
    def addComment(self, comment):
        try:
            if isinstance(comment, Comment):
                db.session.add(comment)
                db.session.flush()
                db.session.commit()
        except Exception, e:
            logger.error('add comment error %s ' % e)
            
    