import requests     #url 주소 입력과 해당 html 가져오기

# 검색어 받기
keyword = input('input search word :')

# 브라우저 주소창
url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={keyword}'
response = requests.get(url)

#print(response.text)   # html contents

# - naver 지식인 검색어 따른 타이틀 수집
# refer https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B8%88%EC%9C%B5
# span.lnk_tit 

from bs4 import BeautifulSoup  #html 해석기

# Dom 구조화
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select('span."fds-comps-header-headline xWYCPbd1ikavaw8UZRF0"')
# len(titles)
# 15
# titles[10]
# <span class="lnk_tit">급할수록 빠르게 위머니</span>

for title in titles :
    print(title.text)
    
pass