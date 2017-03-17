#!/usr/bin/python
# coding:utf-8

from urllib import request
import re

try:
    response = request.urlopen('https://movie.douban.com/top250?start=225&filter=')
    content = response.read().decode('utf-8')
    pattern = re.compile(r'<div .*?item">.*?<div.*?"info">.*?<div.*?hd">.*?<a.*?>.*?<span.*?title">(.*?)</span>.*?</a>'
                         r'.*?<div.*?bd">.*?<p.*?>.*?导演:(.*?)&nbsp;.*?主演:(.*?)<br>.*?</p>.*?<div.*?star">.*?'
                         r'<span.*?average">(.*?)</span>',
                         re.S)
    items = re.findall(pattern, content)
    for item in items:
        for temp in item:
            print(temp.strip())
        print("\n")

except Exception as e:
    print('Exception', e)
finally:
    print('end')
