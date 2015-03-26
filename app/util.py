# -*- coding: utf-8 -*-

import time
from datetime import datetime
import calendar
from config import LEADING_LENGTH

def getTimestamp():
    dt = datetime.utcnow()
    return calendar.timegm(dt.utctimetuple())

def getTimesampFromDate(strDate):
    if strDate:
        return time.mktime(datetime.strptime(strDate, "%Y-%m-%d %H:%M:%S").timetuple())
    else :
        return 0

def timeFromStamp(stamp):
    if int(stamp) <= 0:
        return None
    return datetime.fromtimestamp(int(stamp)).strftime('%Y-%m-%d %H:%M:%S')

def daysFromMonth(month):
    days = {0:0, 1:31, 2:27, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if month and int(month):
        return days[int(month)]
    else:
        return 0
    
def monthFromStamp(stamp):
    if int(stamp) <= 0:
        return None
    return datetime.fromtimestamp(int(stamp)).strftime('%Y-%m')

def creatLeading(content):
    length = len(content)
    leading =''
    if length > LEADING_LENGTH:
        tmp_leading = content[:LEADING_LENGTH]
        #去掉所有<*>类型的字符串
        flag = False
        for char in tmp_leading:
            if not char == '<' and not flag:
                leading = '%s%s' % (leading, char)
            else:
                flag = True
                if char == '>':
                    flag = False
    else:
        leading = content
    return leading

def replaceImage(content):
    recontent = content.replace('&lt;image&gt;', '<div align="center"><br><img class = "blog-img" src="static/imag/')
    content = recontent.replace('&lt;/image&gt;', '"</img></div><br>') 
    return content
