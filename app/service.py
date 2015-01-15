# -*- coding: utf-8 -*-
from app.models import Article, Group, Comment
from app.jmodels import JArticle, JGroup, JComment
from dao import ArticleDao, GroupDao, CommentDao
import util

class ArticleService():
    def __init__(self):
        self.articleDao = ArticleDao()
        self.groupDao = GroupDao()
        
    def getAllArticle(self):
        jarticles = []
        try:
            articles = self.articleDao.getArticles()
            for art in articles:
                jart = JArticle(art, False)
                print jart
                jarticles.append(jart)
        except Exception, e:
            raise Exception(e)
        return jarticles
            
    
    def getArticleById(self, artId):
        articles = self.articleDao.getArticleById(artId)
        jarticles = []
        for art in articles:
            jart = JArticle(art, True)
            jarticles.append(jart)
        return jarticles
    
    def getArticlesByGroupId(self, groupId):
        articles = self.articleDao.articlesByGroupId(groupId)
        jarticles = []
        for art in articles:
            jart = JArticle(art, False)
            jarticles.append(jart)
        return jarticles

    def addClickCount(self, artId):
        self.articleDao.addClickCount(artId)
        
    def addComment(self, artId):
        self.articleDao.addCommentCount(artId)
        
    def addArticle(self, title, groupName, content):
        try:
            article = self.articleDao.getArticleByTitle(title)
            if article:
                raise Exception('该标题已经存在')
            else:
                article = Article()
                article.title = title
                article.content = content
                group = self.groupDao.getGroupByName(groupName)
                if group:
                    article.group = group.id
                    self.groupDao.addGroupCount(group.id)
                else:
                    group = Group()
                    group.name = groupName 
                    group.count = 1
                    group.create_time = util.getTimestamp()
                    self.groupDao.addGroup(group)
                    article.group = group.id 
                article.author = 1
                article.create_time = util.getTimestamp()
                self.articleDao.addArticle(article)
        except Exception, e:
            raise Exception(e)
        
class GroupService():
    def __init__(self):
        self.groupDao =  GroupDao()
        
    def getGroups(self):
        groups = self.groupDao.getGroups()
        jgroups = []
        for gp in groups:
            jgp = JGroup(gp)
            jgroups.append(jgp)
        return jgroups

class CommentService():
    def __init__(self):
        self.commentDao = CommentDao()
    
    def getCommentsByArticleId(self, articleId):
        coms = self.commentDao.getCommentsByArticleId(articleId)
        jcoms = []
        for com in coms:
            jcom = JComment(com)
            jcoms.append(jcom)
        return jcoms
    
    def addComments(self, artId, commenter, comment):
        com = Comment()
        com.article_id = artId
        com.commenter = commenter
        com.comment = comment
        com.create_time = util.getTimestamp()
        self.commentDao.addComment(com)
    