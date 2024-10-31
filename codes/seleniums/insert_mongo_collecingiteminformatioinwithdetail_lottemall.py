# - 실습 -
# - 검색어 따른 상품 정보 전부 수집
# - 항목 : 상품명, 가격, 상품상세
# - github, remote mongo uri 공유

# 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

#몽고
client = MongoClient('mongodb://192.168.0.63:27017/')
db = client['lottemall_jihunshim']
collection = db['lottemall_jihunshim']

webdriver_manager_directory = ChromeDriverManager().install()

#크롬드라이버 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

#크롬 웹드라이버의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력(https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q=%EB%AA%85%ED%92%88&mallId=1)
browser.get('https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q=%EB%AA%85%ED%92%88&mallId=1')

# 상품들 페이지 이동하며 정보 수집
# 1페이지 : #s-search-app span.srchPaginationActive
# 2페이지 ~ 끝까지 : #s-search-app div.srchPagination > a
# stop 키워드 : #s-search-app a.srchPaginationNext

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음 (and 확인)
html = browser.page_source
print(html)

element_value = f'#s-search-app span.srchPaginationActive, #s-search-app div.srchPagination > a'
page_list = browser.find_elements(by=By.CSS_SELECTOR, value = element_value)

element_selector_detail = f'#s-search-app div.srchPagination > a'
for index in range(1, len(page_list)):
    time.sleep(5)
    pagination_list = browser.find_elements(by=By.CSS_SELECTOR,value = element_value)
    if index == 35 :
        continue
    
    pagination_tag = pagination_list[index]
    srchPaginationNext = pagination_tag.get_attribute('class')
    if srchPaginationNext == 'srchPaginationNext' :
        break
    pagination_tag.click()
    time.sleep(2)
    
    # 상세 정보 수집
#     html = browser.page_source
#     soup = BeautifulSoup(html, 'html.parser')
#     detail_list = soup.select(element_selector_detail)
#     for detail in detail_list:
#         detail_uri = detail.attrs['id']
#         detail_uri = f'https://www.lotteon.com{detail_uri}'
#         response = requests.get(detail_uri)
#         pass
#     pass
# pass