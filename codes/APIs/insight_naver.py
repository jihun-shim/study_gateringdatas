import requests
import json
from pymongo import MongoClient


# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://python_selenium_drive_mongo-db_mongodb_7-1:27017")
# database 연결
database = mongoClient["study_APIs"]
# collection 작업
collection1 = database['insight_naver']
collection2 = database['insight_naver']

def main():
    uri = f'https://openapi.naver.com/v1/search/shop'
    params = {'query':'진주'}
    headers = {
        'X-Naver-Client-Id' : 'h99Roh4XOVpiiYZvgRVM'
        ,'X-Naver-Client-Secret' : 'Lbi3coWjV1'
    }
    
    response = requests.get(params = params, url = uri, headers = headers)

    if response.status_code == 200:
        contents = json.loads(response.text)
        pass
    return
if __name__=='__main__':
    main()
    pass