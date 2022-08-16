import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://cu.bgfretail.com/product/view.do?category=event&gdIdx=1',headers=headers)
for i in range(2):
    http = f'https://cu.bgfretail.com/product/view.do?category=event&gdIdx={i}'
    print(http)
    data = requests.get(http,headers=headers)
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
    print(data)


    soup = BeautifulSoup(data.text, 'html.parser')
    foods = soup.select('li.prod_list')


##wrap > #contents > .relCon > .prodListWrap  > 



for food in foods:
    print(food)