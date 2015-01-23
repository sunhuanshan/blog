# -*- coding:utf-8 -*-

from app.dao import  ArticleDao, AuthorDao, GroupDao, CommentDao
from app.models import Article, Author, Group, Comment
from app import util
from pip._vendor.requests.models import CONTENT_CHUNK_SIZE
from test_article import CONTENT, TITLE

class Test():
    def __init__(self):
        self.dao = ArticleDao()
        self.authorDao = AuthorDao()
        self.groupDao = GroupDao()
        self.commentDao = CommentDao()
        
    def test_add_author(self):
        u = Author(name = u'孙焕山', passwd = '123456')
        self.authorDao.addAuthor(u)
        
    def test_get_author(self):
        authors = self.authorDao.getAllAuthors()
        #print len(users)
        for au in authors:
            print au
    def test_remove_articles(self): 
        #title = u'测试标题'
        #self.dao.removeArticle(title)
        artId = 2
        self.dao.removeArticleById(artId)
    
    def add_art(self):
        art = Article()
        art.title = TITLE
        art.content = CONTENT
        art.author = 1
        art.group = 2
        art.clicks = 0
        art.create_time = util.getTimestamp()
        print art.title
        self.dao.addArticle(art)
        self.groupDao.addGroupCount(2)
    
    def get_articles(self):
        arts = self.dao.getArticles()
        for art in arts:
            print art
    
    def test_leading(self):
        content = u'''<p><strong>1)    引子</strong></p>'''
        leading = util.creatLeading(content)
        print leading 

    def test_add_group(self):
        group = Group()
        group.name =u'测试分组1'
        group.create_time = util.getTimestamp()
        self.groupDao.addGroup(group)
        group2 = Group()
        group2.name =u'测试分组2'
        group2.create_time = util.getTimestamp()
        self.groupDao.addGroup(group2)

    def test_get_groups(self):
        groups = self.groupDao.getGroups()
        for gp in groups:
            print gp 
            
    def test_add_comment(self):
        com = Comment()
        com.article_id = 1
        com.comment = u'一步之遥确实不好看'
        com.commenter = 'test commenter'
        com.create_time = util.getTimestamp()
        self.commentDao.addComment(com)
        
    def test_get_comment(self):
        artId = 1
        com = self.commentDao.getCommentsByArticleId(artId)
        print com
    
    def test_image_content(self):
        content = u'我们来了到了那里<image>abcedff.jpg</image>'
        print util.replaceImage(content)
        
if __name__ == "__main__":
    test = Test()
    #test.test_add_author()
    #test.test_get_author()
    #test.test_remove_articles()
    #test.test_leading()
    #test.test_add_group()
    #test.test_get_groups()
    
    #test.add_art()
    #test.get_articles()
    
    #test.test_add_comment()
    #test.test_get_comment()
    test.test_image_content()