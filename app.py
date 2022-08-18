from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.dbjungle


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['GET'])
def read_articles():
    result = list(db.articles.find({},{'_id':False}))
    return jsonify({'result' : 'success', 'articles' : result})


# API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def post_articles():

    try:
        # 1. 클라이언트로부터 데이터를 받기
        url_receive = request.form['url_give']
        comment_receive = request.form['comment_give']

        # 2. meta tag를 스크래핑하기
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url_receive, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')

        og_image = soup.select_one('meta[property="og:image"]')
        og_title = soup.select_one('meta[property="og:title"]')
        og_description = soup.select_one('meta[property="og:description"]')

        url_title = og_title['content']
        url_description = og_description['content']
        url_image = og_image['content']

        article = {'url': url_receive, 'title': url_title, 'desc': url_description, 'image': url_image, 'comment': comment_receive}
        
        # 3. mongoDB에 데이터 넣기
        db.articles.insert_one(article)    
        return jsonify({'result' : 'success'})


    except Exception as e:
        print('예외가 발생했습니다.', e)
        return render_template('pageNotFound.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('pageNotFound.html'), 404

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
