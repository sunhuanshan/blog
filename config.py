# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

LEADING_LENGTH = 300

UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app', 'static', 'imag')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

DESCRIPTION = u"孙焕山"
KEY_WORDS=u"孙焕山"
TITLE=u"孙焕山"
BLOG_TITLE="diligent, explore, share"
MENUS = [{"menu_title":u"首页", "menu_url":"/index"},
         {"menu_title":u"标签", "menu_url":"/tags"},
         {"menu_title":u"关于我", "menu_url":"/me"}]