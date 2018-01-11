# -*- coding: cp936 -*-
#Python有几种网页下载器呢？
"""
* urllib2  Python官方的基础模块
* requests 第三方包
"""
import urllib2

url = "http://www.baidu.com"
print (u"第一种方法")
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print (u"第二种方法")
request2 = urllib2.Request(url)
request2.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request2)
print response1.getcode()
print len(response1.read())


print(u"第三种方法")
