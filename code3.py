#coding = utf-8
import re
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    html=html.decode('utf-8')
    reg = 'src="(http.*?jpg)"'
    imgre = re.compile(reg)
    #查找所有
    imglist = re.findall(imgre,html)
    log(imglist)
    x = 0
    #遍历图片地址并保存
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        log(imgurl)
        x+=1
    log('download complate!')

def getJX3Img(html):
    html=html.decode('utf-8')
    print(html)
    reg = '<div>.*?</div> '
    result = re.findall(reg,html)
    print (result)
       
    
def download(url):
    urllib.request.urlretrieve(url,'1.jpg')


def log(string):
    print('log____   %s\n' %string)


def d():
    _html = getHtml('http://yuyuyu0705.lofter.com/')
    getImg(_html)

def download(url):
    __html = getHtml(url)
    getImg(__html)

def help():
    print(u"d()---直接下载内置的地址中的图片")
    print(u"download(url)---url替换成地址")
#    getJX3Img(_html)
