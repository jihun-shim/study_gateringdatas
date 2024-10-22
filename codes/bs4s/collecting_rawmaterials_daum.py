import requests   #url 주소 입력과 해당 html 가져오기

# 브라우저 주소창
response = requests.get('https://finance.daum.net/domestic/exchange')
#print(response.text)   # html contents

# - 환율 변동 가격 수집
# refer https://finance.daum.net/domestic/exchange
# <span class="num">69.22</span>
# span.num
from selenium import webdriver
from bs4 import BeautifulSoup   #html 해석기

driver = webdriver.Chrome()
driver.get('https://finance.daum.net/domestic/exchange')
html = driver.page_source

# Dom 구조화
soup = BeautifulSoup(response.text, 'html.parser')

currency_prices = soup.select( '#boxCommodities .box_contents div table tbody tr td.pR span.num' )
type(currency_prices)

for currency in currency_prices:
    print(f'Tag : {currency}, Currency price : {currency.text}')
    pass

pass