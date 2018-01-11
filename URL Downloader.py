# -*- coding: cp936 -*-
#Python有几种网页下载器呢？
"""
* urllib2  Python官方的基础模块
* requests 第三方包
"""
import urllib2
#创建Request对象
request = urllib2.Request("https://www.taobao.com/")
#添加数据
#request.add_data('a','1')
#添加http的header
request.add_header('User-Agent','Mozilla/5.0')
#发送请求获取结果
response = urllib2.urlopen(request)
