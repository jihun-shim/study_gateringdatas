# - https://news.naver.com/section/101 있는 news 정보 수집
# refer : https://news.naver.com/section/101
# - 리스트에서 링크와 제목 가져오기
# ##newsct > div.section_latest > div > div.section_latest_article._CONTENT_LIST._PERSIST_META div.sa_text > a
# - 기사내용 확인 uri
# [href]
# - 기사 내용 가져오기
# #dic_area

import requests
from bs4 import BeautifulSoup

def main():
    response = requests.get(f'https://news.naver.com/section/101')
    soup = BeautifulSoup(response.text, 'html.parser')
    titles_link = soup.select('#newsct > div.section_latest > div > div.section_latest_article._CONTENT_LIST._PERSIST_META div.sa_text > a')
    for title_link in titles_link:
        print(f'title : {title_link.text}')
        news_content_url = title_link.attrs['href']
        print(f'news_content_url : {news_content_url}')
        # 기사 내용 가져오기
        response_content = requests.get(f'{news_content_url}')
        soup_content = BeautifulSoup(response_content.text, 'html.parser')
        content = soup_content.select_one(f'#dic_area')
        print(f'content : {content.text}')
        print(f'--'*10)
        pass
    return
if __name__ == '__main__':
    main()
    pass