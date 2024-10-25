# MongoDB 서버에 연결 : Both connect in case local and remote
# client = MongoClient('mongodb://192.168.0.63:27017/')   

# 'mydatabase' 데이터베이스 선택 (없으면 자동 생성)
# db = client['mydatabase']

# 'users' 컬렉션 선택 (없으면 자동 생성)
# collection = db['users']

# 입력할 데이터
# user_data = {
#     'name': 'John Doe',
#     'age': 30,
#     'email': 'johndoe@example.com'
# }

# 데이터 입력
# result = collection.insert_one(user_data)

# 입력된 문서의 ID 출력
# print('Inserted user id:', result.inserted_id)

# - underkg.co.kr 있는 news 정보 수집
# refer : https://underkg.co.kr/news
# - 리스트에서 링크와 제목 가져오기
# #board_list h1 > a
# - 기사내용 확인 uri
# [href]
# - 기사 내용 가져오기
# div.docInner > div.read_body

# select->one을 붙히니까 attrs 가 작동이 안되는점
# 챗gpt와 다른점
# 디버깅에서 result = collection.insert_many(news_list) 오류나는이유

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

def main():
    respone = requests.get(f'https://underkg.co.kr/news')
    soup = BeautifulSoup(respone.text, 'html.parser')
    titles_link = soup.select('#board_list h1 > a')
    titles_date = soup.select('span.time > span')
    titles_read_papers = soup.select('span.readNum > span')
    
    # MongoDB 서버에 연결 : Both connect in case local and remote
    client = MongoClient('mongodb://192.168.0.63:27017/')   

    # 'mydatabase' 데이터베이스 선택 (없으면 자동 생성)
    db = client['news_jihunshim']

    # 'users' 컬렉션 선택 (없으면 자동 생성)
    collection = db['news_jihunshim']

    news_list=[]
    for title_link in titles_link:
        print(f'title : {title_link.text}')
        news_content_url = title_link.attrs['href']
        print(f'news_content_url : {news_content_url}')
        news_date = titles_date
        print(f'news_date : {news_date.}')
        read_papers = titles_read_papers
        print(f'read_papers : {read_papers}')
        
        # 기사 내용 가져오기
        respone_content = requests.get(f'{news_content_url}')
        soup_content = BeautifulSoup(respone_content.text, 'html.parser')
        content = soup_content.select_one(f'div.docInner > div.read_body')
        print(f'content : {content.text}')
        print(f'--'*10)
        
        # 입력할 데이터
        news = {
            'name': title_link.text,
            'link': news_content_url,
            'date': news_date,
            'read_papers': read_papers,
            'article': content.text
            }
        news_list.append(news)
        pass
    
    # 데이터 입력
    result = collection.insert_many(news_list)
    
    return
if __name__ == '__main__':
    main()
    pass