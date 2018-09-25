#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

#加载库
import urllib
import urllib2
import json
from bs4 import BeautifulSoup


tags = []
# 获取所有标签
url = 'https://movie.douban.com/j/search_tags?type=movie'
request = urllib2.Request(url=url)
response = urllib2.urlopen(request, timeout=20)
result = response.read()
print result