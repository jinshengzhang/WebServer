#!/usr/bin/python
#coding=utf-8
"""
*文件说明:测试各种函数
*作者:高小调
*创建时间:2017年07月27日 星期四 16时15分18秒
*开发环境:Kali Linux/Python v2.7.13
"""
from modules import cdn_check
from modules import port_scan
import requests
from sys import argv
from lib import Spider
from modules import sql_check
from modules import webcms_check
from lib import Downloader
from modules import webshell_check
from modules import xss_check
from modules import bak_check
#测试检查页面是否存在sql注入
def test_sql_check():
    #ret = sql_check.run("http://www.hbxffy1.com/info/dispnews.asp?id=1709")
    #ret = sql_check.run("http://www.szxcc.com/gb/about1_xinxi.asp?id=325")
    ret = sql_check.run("http://www.szxcc.com/gb/zxgg_detail.asp?id=376")
    print(ret);
    #ret = sql_check.run("http://www.chinaxinge.com/company/skin/12/index.asp?id=7798")
    #print ret;

#测试从url中获取域名
def test_get_domain():
    print (cdn_check.get_domain("http://blog.csdn.net/imzoer/article/details/8636764"))
    print (cdn_check.get_domain("http://www.cnblogs.com/allenblogs/archive/2011/11/15/2055149.html"))
    print (cdn_check.get_domain("https://my.oschina.net/guol/blog/95699"))
    print (cdn_check.get_domain(""))

#测试表单数据
def test_get_post_request_info():
    url = "http://ce.cloud.360.cn"
    web_content = requests.get(url)
    print (cdn_check.get_post_request_info(web_content.text))

#测试cdn检测
def test_cdn_check():
    script,first = argv
    msg,state=cdn_check.run(first)
    print (msg)

#测试端口扫描
def test_port_scan():
    script,ip = argv
    if ip == None:
        print ("Usage:%s [ip]"%script)
        return False
    ps = port_scan.PortScan(ip)
    ps.run()

#测试小爬虫
def test_spider():
    s = Spider.Spider("http://www.szxcc.com/gb/",10);
    ret = s.craw()
    for url in ret:
        ret = sql_check.run(url)
        if(ret is True):
            break;
#测试WebCMS指纹识别
def test_webcms_check():
    cms_check = webcms_check.webcms("http://www.szxcc.com/gb",10)
    cms_check.run()
    #down = Downloader.Downloader()
    #print down.get("http://www.szxcc.com/gb/install/")
#测试webshell_check
def test_webshell_check():
    ret = webshell_check.run("http://gaoxiaodiao.com/sasa.php")
    print ret
def test_xss_check():
    #urls = xss_check.urlsplit("http://gaoxiaodiao.com/index.asp?id=1&cate=2&something=3");
    #for url in urls:
    #    print url
    xss_check.run("http://127.0.0.1/xss.php?code=1")
def test_bak_check():
    #paths = bak_check.get_parent_paths("/a/b/c/d/e/f/g/")
    #for path in paths:
    #    print(path)
    bak_check.run("http://gaoxiaodiao.com/a/b/c/d/e/f/g")
if __name__ == '__main__':
    #test_get_domain()
    #test_get_post_request_info()
    #test_cdn_check()
    #test_port_scan()
    #test_spider()
    #test_sql_check()
    #test_webcms_check()
    #test_webshell_check()
    #test_xss_check()
    test_bak_check()
