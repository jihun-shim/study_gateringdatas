import requests

# ?&appid={API key}
url = 'http://api.openweathermap.org/geo/1.0/direct'
params ={'q':'Monaco'
         , 'appid':'cbdbbb3a98df1289f73ac00a15f1cd46'}

response = requests.get(url, params=params)
if response.status_code == 200:
    # print(response.content)
    if response.text != '[]':
        import json
        content = json.loads(response.content)

        # mongoDB 저장
        from pymongo import MongoClient
        # mongodb에 접속 -> 자원에 대한 class
        mongoClient = MongoClient("mongodb://python_selenium_drive_mongo-db_mongodb_7-1:27017")
        # database 연결
        database = mongoClient["study_finance"]
        # collection 작업
        collection = database['coordinatesbylocationonname']

        result = collection.insert_many(content)
    else : 
        print(f'result empty : {response.text}')
else:
    print(f'error : {response.status_code}')