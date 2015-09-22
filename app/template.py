# -*- coding: utf-8 -*-

from service import ArticleService, GroupService
from config import DESCRIPTION, KEY_WORDS, TITLE, BLOG_TITLE, MENUS
from flask import jsonify

def getTemplateHeaderData():
    index_data={}
    #导入页头等配置信息
    index_data['description'] = DESCRIPTION
    index_data['keywords'] = KEY_WORDS
    index_data['title'] = TITLE
    index_data['blog_title'] = BLOG_TITLE
    index_data['menus'] = MENUS
    return jsonify(index_data)

def getArticlesData(page = 0):
    #文章信息
    data={}
    tagService = GroupService()
    tags = tagService.getGroups()
    data['tags'] = tags
    atService = ArticleService()
    arts = atService.getArticlesByPage(0, 10)
    data['articles'] = arts
    count = atService.getArticlesCount()
    pages_count = count / 10
    pages=[]
    for i in range(0, pages_count+1):
        page = {}
        page['url'] = '/page?id=%s' % (i+1)
        if i == 0:
            page['title'] = '首页'
        elif i == pages_count:
            page['title'] = '末页'
        else:
            page['title'] = i+1
        if i== page:
            page['active'] = 'true'
        pages.append(page)
    data['pages'] = pages
    return jsonify(data)



