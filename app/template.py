# -*- coding: utf-8 -*-

from service import ArticleService, GroupService
from config import DESCRIPTION, KEY_WORDS, TITLE, BLOG_TITLE, MENUS
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
            page['title'] = u'首页'
        elif i == pages_count:
            page['title'] = u'末页'
        else:
            page['title'] = i+1
        if i== page:
            page['active'] = 'true'
        pages.append(page)
    data['pages'] = pages
    return jsonify(data)

def myrender(file, data = None):
    html = ''
    path = os.path.split(os.path.realpath(__file__))[0]
    file = '%s/%s'%(path, file)
    print file
    if os.path.isfile(file):
        tf = open(file, 'r')
        tpl = tf.read()
        if data:
            html = pystache.render(tpl, data)
        else:
            html = tpl
        tf.close()
    return html

