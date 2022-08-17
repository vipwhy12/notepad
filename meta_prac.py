from select import select
from turtle import title
import requests
from bs4 import BeautifulSoup

url = 'https://platum.kr/archives/120958'


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

image = soup.select_one('meta[property="og:image"]')
title = soup.select_one('meta[property="og:title"]')
description = soup.select_one('meta[property="og:description"]')

url_imge = image['content']
url_title = title['content']
url_description = description['content']

print(url_imge, url_title, url_description )