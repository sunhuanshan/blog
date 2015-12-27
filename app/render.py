# -*- coding: utf-8 -*-

from service import ArticleService, GroupService, CommentService
from config import AUTHOR, VIEW_TITLE, PUBLISHED, DESCRIPTION, \
    KEY_WORDS, TITLE, BLOG_TITLE, MENUS, COPY_RIGHT, LICENSE, \
    PERMIT, FIRST_PAGE, NEXT_PAGE, LAST_PAGE, EMAIL_TITLE, NAME_TITLE,\
    REVIEWER_TITLE, CONFIRM, CANCEL, REVIEW_TITLE, REVIEW_BOX_TITLE,SUBMIT,\
    REVIEW_COUNT_TITLE, REVIEW_COUNT_UNIT, REPLAY, FAVORITE, FAVORITE_TITLE,\
    VIEW_COUNT_TITLE
from flask import jsonify
import os
import pystache

def getTemplateHeaderData():
    index_data={}
    #导入页头等配置信息
    index_data['description'] = DESCRIPTION
    index_data['keywords'] = KEY_WORDS
    index_data['title'] = TITLE
    index_data['blog_title'] = BLOG_TITLE
    index_data['menus'] = MENUS
    return index_data

def getTemplateFooterData():
    foot_data={}
    #页脚信息
    foot_data['copy_right'] = COPY_RIGHT
    foot_data['license'] = LICENSE
    foot_data['permit'] = PERMIT
    return foot_data

def getContentData():
    #文章信息
    data={}
    tagService = GroupService()
    tags = tagService.getGroups()
    if len(tags) > 0:
        data['tags_data'] = True
        data['tags'] = tags
    atService = ArticleService()
    arts = atService.getArticlesByPage(0, 10)
    if len(arts) > 0:
        data['articles_data'] = True
        data['articles'] = arts
        data['published'] = PUBLISHED
        data['view_title'] = VIEW_TITLE
    count = atService.getArticlesCount()
    pages_count = count / 10
    pages=[]
    next_page = {}
    if pages_count  > 10:
        next_page['title'] = NEXT_PAGE
        next_page['id'] = '2'
    for i in range(0, pages_count+1):
        page = {}
        page['id'] = '%s' % (i+1)
        if i == 0:
            page['title'] = FIRST_PAGE
        elif i == pages_count:
            if next_page:
                pages.append(next_page)
            page['title'] = LAST_PAGE
        else:
            page['title'] = '%s' % (i+1)
        if i == page:
            page['active'] = 'true'
        pages.append(page)
    if len(pages) > 0:
        data['pages_data']=True
        data['pages'] = pages
    return data

def getArticlesData(page=1):
    data = {}
    data['articles_data'] = False
    atService = ArticleService()
    arts = atService.getArticlesByPage((page-1)*10, 10)
    if len(arts) > 0:
        data['articles_data']=True
        data['reload'] = True
        data['articles'] = arts
        data['published'] = PUBLISHED
        data['view_title'] = VIEW_TITLE
        data['author']=AUTHOR
    return data

def getArticleData(at_id):
    data={}
    atService = ArticleService()
    atService.addClickCount(at_id)
    art = atService.getArticleById(at_id)
    if art:
        data['article']=art
        data['article']['author_title'] = AUTHOR
        data['article']['published']=PUBLISHED
        data['article']['view_title']=VIEW_TITLE
    return data

def getReview(at_id):
    data={}
    data['review_box'] = True
    data['input_review'] = True
    data['email_title'] = EMAIL_TITLE
    data['name_title']= NAME_TITLE
    data['confirm']=CONFIRM
    data['cancel']=CANCEL
    data['review_title'] = REVIEW_TITLE
    data['reviewer_title']=REVIEWER_TITLE
    data['review_box_title']=REVIEW_BOX_TITLE
    data['submit']=SUBMIT
    comService = CommentService()
    reviews = comService.getCommentsByArticleId(at_id)
    if len(reviews) > 0:
        data['review_history_data'] = True
        data['review_count_title']=REVIEW_COUNT_TITLE
        data['review_count_unit']=REVIEW_COUNT_UNIT
        data['replay']=REPLAY
        data['published']=PUBLISHED
        data['favorite']=FAVORITE
        data['favorite_title']=FAVORITE_TITLE
        data['review_history']= reviews
        data['review_count'] = len(reviews)
    return data

def getHistoryReview(at_id):
    data = {}
    comService = CommentService()
    reviews = comService.getCommentsByArticleId(at_id)
    if len(reviews) > 0:
        data['review_history_data'] = True
        data['review_count_title']=REVIEW_COUNT_TITLE
        data['review_count_unit']=REVIEW_COUNT_UNIT
        data['replay']=REPLAY
        data['published']=PUBLISHED
        data['favorite']=FAVORITE
        data['favorite_title']=FAVORITE_TITLE
        data['review_history']= reviews
        data['review_count'] = len(reviews)
    return data

def getTags():
    data = {}
    gpService = GroupService()
    atService = ArticleService()
    tags = gpService.getGroups()
    allTags = []
    for tag in tags:
        single_tag = {}
        tag_id = tag['id']
        ats = atService.getArticlesByGroupId(tag_id)
        tag['article_count'] = len(ats)
        single_tag['id']=tag_id
        single_tag['tag'] = tag
        single_tag['articles'] = ats
        allTags.append(single_tag)
    data['tags'] = allTags
    data['view_count_title'] = VIEW_COUNT_TITLE
    return data

def myRender(file, data = None):
    html = ''
    path = os.path.split(os.path.realpath(__file__))[0]
    file = '%s/%s'%(path, file)
    if os.path.isfile(file):
        tf = open(file, 'r')
        tpl = tf.read()
        if data:
            html = pystache.render(tpl, data)
        else:
            print html
            html = tpl
        tf.close()
    return html

