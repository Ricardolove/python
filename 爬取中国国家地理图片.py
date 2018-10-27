import requests
import bs4
from bs4 import BeautifulSoup
import os

def getHTMLText(url):
    try:
        r = requests.get(url,header=kv,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("网页抓取过程出现问题")

def fillpictureList(plist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])