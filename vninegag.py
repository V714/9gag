### Script for getting source and name from new article on 9gag.com

import urllib

ninegag = "http://9gag.com/"
### This is how script recognize new article.
wWSf='"position":1,"url":"https:\/\/9gag.com\/gag\/'
iasf='https://img-9gag-fun.9cache.com/photo/'

def pageToStr(url):
    a = urllib.request.urlopen(url)
    enc = a.headers.get_content_charset("utf-8")
    d = a.read()
    return d.decode(enc)

### Getting link of gag from 1st position
def getGag():
    b = pageToStr(ninegag)
    c = b.find(wWSf)+45
    ce= len(b)-c-7
    gag = b[c:-ce]
    return ninegag+"gag/"+gag

### Returning title as a string.
def getTitle(link):
    b = pageToStr(link)
    c = b.find("<title>")+7
    d = len(b)-b.find("</title>")+7
    return str(b[c:-d])

### Returning link to content (gif/photo/video) as a string.
def getLink(link):
    b = pageToStr(link)
    c = b.find(wWSf)+45
    ce= len(b)-c-7
    gag = b[c:-ce]
    check = iasf+gag+"_460svvp9.webm"
    if getTitle(check)=="9GAG - 404 Nothing here":
        return iasf+gag+"_700bwp.webp"

    else:
        return check
