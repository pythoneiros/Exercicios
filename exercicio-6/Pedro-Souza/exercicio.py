#!/usr/bin/env python 
#_*_ coding:utf-8 _*_

import requests
import re

html = requests.get("https://facebook.com").text
href = re.findall('href="(.*?)"', html)
txt = open("list.txt", "a")
for i in href:
	txt.write(i+"\n")
txt.close()