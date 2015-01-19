# -*- coding: utf-8 -*-
from flask import render_template, jsonify, request, url_for
from app import app
from service import ArticleService, GroupService
from logger import logger
from jmodels import MyJSONEncoder
from werkzeug import responder
from app.service import CommentService

app.json_encoder = MyJSONEncoder

artService = ArticleService()
gpService = GroupService()
comService = CommentService()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/article/list', methods = ['GET', 'POST'])
def articleList():
    resp = {}
    try:
        arts = artService.getAllArticle()
        if arts:
            resp['success'] = True
            resp['items'] = arts
            resp['size'] = len(arts)
        else:
            raise Exception(' no articles exist')
    except Exception, e:
        logger.error(' get articles has an error %s' % e)   
        resp['success'] = False
        resp['detail'] = '获取文章失败'
   
    return jsonify(resp)

@app.route('/article/content', methods = ['GET', 'POST'])
def articleDetail():
    resp = {}
    try:
        artId = request.form['id']
        if artId:
            artService.addClickCount(artId)
            arts = artService.getArticleById(artId);
            coms = comService.getCommentsByArticleId(artId)
            resp['success'] = True
            resp['items'] = arts 
            resp['comments'] = coms 
        else:
            raise Exception('artId is null')
    except Exception, e:
        logger.error('get article detail error: %s' % e)
        resp['success'] = False
        resp['detail'] = '%s' % e
    
    return jsonify(resp)

@app.route('/article/groups', methods = ['GET', 'POST'])
def getGroups():
    resp = {}
    try:
        groups = gpService.getGroups()
        resp['success'] = True
        resp['items'] = groups
    except Exception, e:
        logger.error('get groups error %s' % e)
        resp['success'] = False
        resp['detail'] = '获取分组失败'
    return jsonify(resp)

@app.route('/article/comment', methods = ['GET', 'POST'])
def getComment():
    resp ={}
    try:
        artId = request.form['id']
        if artId:
            coms = comService.getCommentsByArticleId(artId)
            resp['success'] = True
            resp['items'] = coms 
        else:
            raise Exception('artId is null')
    except Exception, e:
        logger.error('get comments error %s' % e)
        resp['success'] = False
        resp['detail'] = '获取评论失败'
    return jsonify(resp)
        
@app.route('/article/addComment', methods = ['GET', 'POST'])
def addComment():
    resp = {}
    try:
        artId = request.form['id']
        commenter = request.form['commenter']
        comment = request.form['comment']
        if artId and commenter and comment:
            artService.addComment(artId)
            comService.addComments(artId, commenter, comment)
            resp['success'] = True
            resp['detail'] = '评论成功'
        else:
            raise Exception('parameter error')
    except Exception, e:
        logger.error('add comments error %s' % e)
        resp['success'] = False
        resp['detail'] = '评论失败，请重试。'
    return jsonify(resp)

@app.route('/article/articleByGroup', methods = ['GET', 'POST'])
def articleByGroup():
    resp = {}
    try:
        groupId = request.form['id']
        if groupId:
            arts = artService.getArticlesByGroupId(groupId)
            if arts and len(arts) > 0:
                resp['success'] = True
                resp['items'] = arts
                resp['size'] = len(arts)
            else:
                resp['success'] = False
                resp['detail'] = '该分组无文章'
        else:
            raise Exception('parameter error')
    except Exception, e:
        resp['success'] = False
        resp['detail'] = '获取文章失败'
        logger.error('get articles by group error %s' % e)
    return jsonify(resp)

@app.route('/new', methods = ['GET', 'POST'])
def newArticle():
    return render_template('new.html')

@app.route('/article/addarticle', methods = ['GET', 'POST'])
def addArticle():
    resp = {}
    try:
        title = request.form['title']
        group = request.form['group']
        content = request.form['content']
        key = request.form['key']
        logger.debug('key:' + key)
        if key or not key == 'sun123':
            resp['success'] = False
            resp['detail'] = '提交码错误，无法提交'
        else:
            if title and group and content:
                artService.addArticle(title, group, content)
                resp['success'] = True
                resp['detail'] = '发表文章成功'
            else:
                raise Exception('parameter error')
    except Exception, e:
        resp['success'] = False
        resp['detail'] = '%s' % e
    return jsonify(resp)