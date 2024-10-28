# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
from pymongo import MongoClient

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력(https://underkg.co.kr/news)
browser.get("https://underkg.co.kr/news")

# - 몽고
client = MongoClient('mongodb://192.168.0.63:27017/')   
db = client['db_jihunshim']
collection = db['underkg_jihunshim']

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

# mongodb insert 제목(titles), 날짜(date), 읽은 수(read_view) , 기사본문(news_paper)
#board_list > div > div : element_bundle
#board_list h1 > a : titles
#board_list span.time > span : date 
#board_list span.readNum > span : read_view

from selenium.webdriver.common.by import By
currency_list = browser.find_elements(by=By.CSS_SELECTOR, value = '#board_list > div > div' )

for index, element_bundle in enumerate(currency_list):
    titles_tag = f'#board_list  h1 > a'
    titles = element_bundle.find_element(By.CSS_SELECTOR,titles_tag)
    date_tag = f'#board_list span.time > span'
    date = element_bundle.find_element(By.CSS_SELECTOR,date_tag)
    read_view_tag=f'#board_list span.readNum > span'
    read_view = element_bundle.find_element(By.CSS_SELECTOR,read_view_tag)
        
    result = f'titles : {titles.text}, date : {date.text}, read_view : {read_view.text}'
    print(result)

    pass