#이미지 다운로드
#refer : http://www.cgv.co.kr/movies/?lt=1&ft=0
# target image link tag : div.box-image > a > span > img

import requests
# html 파일 요청
response = requests.get(f'http://www.cgv.co.kr/movies/?lt=1&ft=0')

from bs4 import BeautifulSoup
# html 구조화
soup = BeautifulSoup(response.text , 'html.parser')

image_link_list = soup.select(f'div.box-image > a > span > img')

# 저장 위치 정하기
import os
folder_name = f'./downloads'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

import urllib.request as req
for index, image_link in enumerate(image_link_list):
    image_uri = image_link.attrs['src']
    req.urlretrieve(image_uri, f'{folder_name}/{index}.jpg')
    pass