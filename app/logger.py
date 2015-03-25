# -*- coding: utf-8 -*-

import logging.handlers
import datetime
from config import basedir
import os

logger = logging.getLogger('mylogger')

today = datetime.date.today()
filePath = os.path.join(basedir, 'log')
if not os.path.exists(filePath):
    os.makedirs(filePath)

logFile  = os.path.join(filePath, 'blog.log')
fh = logging.handlers.TimedRotatingFileHandler(logFile, 'midnight', 1)
fh.suffix = '%Y-%m-%d'
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(pathname)s - %(lineno)d - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)