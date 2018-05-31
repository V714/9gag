### Script for getting source and name from new article on 9gag.com

import urllib

ninegag = "http://9gag.com/"
### This is how script recognize new article.
wWSf='"position":1,"url":"https:\/\/9gag.com\/gag\/'
iasf='https://img-9gag-fun.9cache.com/photo/'

### Taking page html source to string
def pageToStr(url):
    a = urllib.request.urlopen(url)
    enc = a.headers.get_content_charset("utf-8")
    d = a.read()
    return d.decode(enc)
    
### Returning title as a string.
def getTitle():
    b = pageToStr(ninegag)
    c = b.find(wWSf)+45
    ce= len(b)-c-7
    gag = b[c:-ce]
    link = ninegag+"gag/"+gag
    b = pageToStr(link)
    c = b.find("<title>")+7
    d = len(b)-b.find("</title>")+7
    return str(b[c:-d])

### Returning link to content (gif/photo/video) as a string.
def getLink():
    b = pageToStr(ninegag)
    c = b.find(wWSf)+45
    ce= len(b)-c-7
    gag = b[c:-ce]
    return iasf+gag+"_460svvp9.webm"
