# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

LEADING_LENGTH = 300

UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app', 'static', 'imag')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

DESCRIPTION = "孙焕山"
KEY_WORDS="孙焕山"
TITLE="孙焕山"
BLOG_TITLE="diligent, explore, share"
MENUS = [{"menu_title":"首页", "menu_url":"/index"},
         {"menu_title":"标签", "menu_url":"/tags"},
         {"menu_title":"关于我", "menu_url":"/me"}]