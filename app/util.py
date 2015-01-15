# -*- coding: utf-8 -*-

from datetime import datetime
import calendar
from config import LEADING_LENGTH

def getTimestamp():
    dt = datetime.utcnow()
    return calendar.timegm(dt.utctimetuple())

def timeFromStamp(stamp):
    if int(stamp) <= 0:
        return None
    return datetime.fromtimestamp(int(stamp)).strftime('%Y-%m-%d %H:%M:%S')

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
