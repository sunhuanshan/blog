# -*- coding: utf-8 -*-
import os
from flask import Flask 
from config import basedir
from flask.ext.sqlalchemy import SQLAlchemy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

app.config.from_object('config')

app.secret_key = 'IUSYTS()ldisnfu%%'

db = SQLAlchemy(app)

from app import views, models