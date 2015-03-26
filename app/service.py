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
    
    #按月份对时间进行分组
    def getTimeGroups(self):
        timeGroups = {}
        articles = self.articleDao.getArticles()
        for art in articles:
            if art.create_time > 0:
                time = util.monthFromStamp(art.create_time)
                if timeGroups.has_key(time):
                    timeGroups[time] = timeGroups[time] + 1
                else:
                    timeGroups[time] = 1
        return timeGroups
    
    def getArticlesByTime(self, time):
        beginTime = 0
        endTime = 0
        jarticles = []
        if time:
            #获取month
            month = '0'
            times = time.split('-')
            if len(times) > 0:
                month = times[1]
            days = util.daysFromMonth(month)
            strBegin = '%s-01 00:00:00' % time
            strEnd = '%s-%02d 00:00:00' % (time, days)
            beginTime = util.getTimesampFromDate(strBegin)
            endTime = util.getTimesampFromDate(strEnd)
            print '%s %s' % (strBegin, strEnd)
            articles =  self.articleDao.getArticlesByTime(int(beginTime), int(endTime))
            for art in articles:
                jart = JArticle(art, True)
                jarticles.append(jart)
        else:
            raise Exception( 'time is none')
        return jarticles
    
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
    