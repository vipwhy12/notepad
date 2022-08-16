from ftplib import all_errors
from turtle import title
from unicodedata import name
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle 

# 코딩 시작
movie_name = db.movies.find_one({'title':'매트릭스'})

print(movie_name['star'])

score = movie_name['star']

aaa = list(db.movies.find({'star':score}))

for a in aaa:
    print(a['title'])


#매트릭스 영화의 평점을 0점으로 만들기
db.movies.update_one({'title':'매트릭스'}, {'$set':{'star':0}})