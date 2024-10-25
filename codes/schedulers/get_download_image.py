#이미지 다운로드
#refer : https://www.mk.co.kr/
# target image link tag : #list_area > ul div.thumb_area > img
import os
import urllib.request as req
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

class get_image:
    def main():
        # html 파일 요청
        response = requests.get(f'https://www.mk.co.kr/')

        # html 구조화
        soup = BeautifulSoup(response.text , 'html.parser')
        image_link_list = soup.select(f'#list_area > ul div.thumb_area > img')
        news_name = soup.select('#list_area div.txt_area > h3') # 기사제목 list_area div.txt_area > h3
        news_time = soup.select('#list_area div.txt_area > .info_group') # 기사시간 list_area div.txt_area > .info_group

        # MongoDB 서버에 연결 : Both connect in case local and remote
        client = MongoClient('mongodb://192.168.0.63:27017/')   

        # 'mydatabase' 데이터베이스 선택 (없으면 자동 생성)
        db = client['newslist_jihunshim']

        # 'users' 컬렉션 선택 (없으면 자동 생성)
        collection = db['newslist']

        # 저장 위치 정하기

        folder_name = f'./downloads'
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        print(f'{len(image_link_list)},{len(news_name)},{len(news_time)}')

        for index, image_link in enumerate(image_link_list):
            image_uri = image_link.attrs['data-src']
            req.urlretrieve(image_uri, f'{folder_name}/{index}.jpg')
            pass

        for news_namess in news_name :
            print (f'title : {news_namess.text}')
            
        for news_timess in news_time :
            print (f'title : {news_timess.text}')

        news_list=[]
        for image_link, news_namess, news_timess in zip(image_link_list,news_name,news_time):
                    # 입력할 데이터
            news = {
                'image': image_link.attrs['data-src'].strip(),
                'name': news_namess.text.strip(),
                'time': news_timess.text.strip(),
                }
            news_list.append(news)
            pass

        result = collection.insert_many(news_list)
            
        print('result ids :', result.inserted_ids)
        
    if __name__ == '__main__':
        main()
        pass