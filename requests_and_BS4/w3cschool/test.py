#!/usr/bin/env python
#-*- coding:utf-8 -*-

W3C_PAGE='http://www.w3cschool.cc'
W3C_DIR='w3cschool'
SINA_PAGE='http://www.sina.com.cn'
QQ_PAGE='http://www.qq.com'

import urlparse
import requests
import codecs
import os
from bs4 import BeautifulSoup as bs


def do_test(index_url):
    res=requests.get(index_url)
    soup=bs(res.text)
    with codecs.open("index.html",'w',encoding='utf-8') as f:
        f.write(soup.prettify())

    div_leftcolumn = soup.find("div",id="leftcolumn")
    # target 是控制浏览器行为的
    for a_tag in div_leftcolumn("a"):
        url = handle_href(index_url,index_url,a_tag["href"])
        up=urlparse.urlparse(url)
        dirname="." + os.path.dirname(up.path)
        if up.path[-1]=="/":
            dirname=os.path.dirname(dirname)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        filename="."+up.path
        if filename[-1]=="/":
            filename=filename[:-1]
        res=requests.get(url)
        with codecs.open("."+up.path,'w',encoding='utf-8') as f:
            f.write(res.text)

        sub_soup=bs(res.text)
        sub_div_leftcolumn = sub_soup.find("div",id="leftcolumn")
        for sub_a_tag in sub_div_leftcolumn("a"):
            sub_url=handle_href(index_url,url,sub_a_tag["href"])
            up=urlparse.urlparse(sub_url)
            dirname="."+os.path.dirname(up.path)
            if up.path[-1]=="/":
                dirname=os.path.dirname(dirname)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            filename="."+up.path
            if filename[-1]=="/":
                filename=filename[:-1]
            res=requests.get(url)
            with codecs.open(filename,'w',encoding='utf-8') as f:
                f.write(res.text)




def do_test2():
    res=requests.get(QQ_PAGE)
    #res.encoding='gb2312'  # for site encoded by gb2312 eg. sina
    soup=bs(res.text)
    with codecs.open("sina.html",'w',encoding='utf-8') as f:        # bcs bs encode text in utf-8
        f.write(soup.prettify())

# return a url that can direcly GET
# I'll never create a url string end with '/'
def handle_href(index_url,current_url,href_string):
    if href_string[0:7]=="http://" :
        return href_string
    elif href_string.find('/') != -1:
        return index_url+ '/' + href_string
    else:
        return current_url[:current_url.rfind('/')]+ '/' + href_string
        


def download_page(url,filename):
    res=requests.get(url)
    with codecs.open(filename,'w',encoding='utf-8') as f:
        f.write(res.text)

if(__name__=='__main__'):
    os.chdir("./w3cschool")
    do_test(W3C_PAGE)
    #do_test2()




