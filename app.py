import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dbnotepad

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
movie = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')



@app.route('/')
def home():
    return render_template('index.html')

#만약 main이면 실행시켜라?
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


#필요한 데이터베이스 
#img url주소값
#제목
#설명
#내코멘트?