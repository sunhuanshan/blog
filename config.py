# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

LEADING_LENGTH = 1300

SUBMIT_KEY = 'sun123'
UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app', 'static', 'imag')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

DESCRIPTION = u"孙焕山"
KEY_WORDS=u"孙焕山"
TITLE=u"孙焕山"
BLOG_TITLE="diligent, explore, share"
MENUS = [{"menu_title":u"首页", "menu_url":"/index"},
         {"menu_title":u"标签", "menu_url":"/tags"},
         {"menu_title":u"关于我", "menu_url":"/me"}]
COPY_RIGHT = u"Copyright (c) 2015-2015 CodingLabs 本博客内容采用"
LICENSE=u"知识共享署名 3.0 中国大陆许可协议"
PERMIT=u"进行许可"
PUBLISHED=u"发表于"
VIEW_TITLE=u"评论"
FIRST_PAGE=u"首页"
LAST_PAGE=u"末页"
NEXT_PAGE=u"下一页"
AUTHOR=u"作者"
####review
EMAIL_TITLE=u"邮箱："
NAME_TITLE=u"名称："
REVIEWER_TITLE=u"以游客身份留言"
CONFIRM=u"确认"
CANCEL=u"取消"
REVIEW_TITLE=u"评论一下"
REVIEW_BOX_TITLE=u"说点什么..."
SUBMIT=u"提交"
REVIEW_COUNT_TITLE=u"评论总数共有"
REVIEW_COUNT_UNIT=u"条"
REPLAY=u"回复"
FAVORITE=u"顶一下"
FAVORITE_TITLE=u"个人觉得很赞"
VIEW_COUNT_TITLE=u"阅读"