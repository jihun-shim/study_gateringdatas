from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
from pymongo import MongoClient

webdriver_manager_directory = ChromeDriverManager().install()

#크롬드라이버실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# 크롬웹드라이버의 capabilities 속성 사용
capabilities = browser.capabilities

#- 항목 : 작성자, 작성일, 댓글, 좋아요와 싫어요 갯수
# page : body
# writer : #author-text span
# write_date : #published-time-text a
# reply : #content-text > span
# good : #vote-count-middle
# bad : #dislike-button div.yt-spec-touch-feedback-shape__fill

# 주소입력(https://www.youtube.com/watch?v=JdRcM4fLwgE&t=359s)
browser.get('https://www.youtube.com/watch?v=JdRcM4fLwgE&t=359s')

# 몽고
client = MongoClient('mongodb://192.168.0.63:27017/')   
db = client['youtube_jihunshim']
collection = db['youtube_jihunshim']

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

from selenium.webdriver.common.by import By
element_value = f'body'
element_body = browser.find_element(by=By.CSS_SELECTOR, value=element_value)

from selenium.webdriver.common.keys import Keys
import time

scroll_count = 50
for i in range(scroll_count):
    element_body.send_keys(Keys.PAGE_DOWN)    
    time.sleep(0.5)

pass

total=[]

element_value = f'#author-text span'
element_writer = browser.find_elements(by=By.CSS_SELECTOR, value=element_value)

element_value = f'#published-time-text a'
element_write_date = browser.find_elements(by=By.CSS_SELECTOR, value=element_value)

element_value = f'#content-text > span'
element_reply = browser.find_elements(by=By.CSS_SELECTOR, value=element_value)

element_value = f'#vote-count-middle'
element_good = browser.find_elements(by=By.CSS_SELECTOR, value=element_value)

# element_value = f'#dislike-button div.yt-spec-touch-feedback-shape__'
# element_bad = browser.find_elements(by=By.CSS_SELECTOR, value=element_value)

for writer, write_date, reply, good in zip(element_writer,element_write_date,element_reply,element_good):

    result = f'element_writer : {writer.text}, element_write_date : {write_date.text},element_reply : {reply.text}, element_good : {good.text}'
    print(result)

    list={
        'element_writer' : writer.text,
        'element_write_date' : write_date.text,
        'element_reply' : reply.text,
        'element_good' : good.text,
        'element_bad' : f'0'
        }
    total.append(list)

result = collection.insert_many(total)
pass

