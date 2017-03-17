#!/usr/bin/python
# coding:utf-8

from urllib import request
import re


class DouBan(object):
    def __init__(self):
        self.page = 0
        self.url = 'https://movie.douban.com/top250?start='

    # 获取页面文本内容
    def get_page_content(self, index):
        url = self.url+str(index)
        print(url)
        try:
            response = request.urlopen(url)
            content = response.read().decode('utf-8')
            return content
        except Exception as e:
            print('get_page_content error' + e)

    # 筛选出页码内容中的电影信息
    def get_movie_info(self, page_content):
        pattern = re.compile(
            r'<div .*?item">.*?<div.*?"info">.*?<div.*?hd">.*?<a.*?>.*?<span.*?title">(.*?)</span>.*?</a>'
            r'.*?<div.*?bd">.*?<p.*?>.*?导演:(.*?)&nbsp;.*?主演:(.*?)<br>.*?</p>.*?<div.*?star">.*?'
            r'<span.*?average">(.*?)</span>',
            re.S)
        items = re.findall(pattern, page_content)
        for item in items:
            for temp in item:
                print(temp.strip())
            print("\n")

    def start(self, max_page):
        for i in range(1, max_page+1):
            content = self.get_page_content((i-1)*25)
            self.get_movie_info(content)


douban = DouBan()
douban.start(10)
