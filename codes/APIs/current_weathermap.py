import requests

# ?lat=44.34&lon=10.99&appid=cbdbbb3a98df1289f73ac00a15f1cd46


url = 'http://api.openweathermap.org/geo/1.0/direct'
params_list =[{'q':'Monaco', 'appid':'cbdbbb3a98df1289f73ac00a15f1cd46'},
{'q':'tokyo', 'appid':'cbdbbb3a98df1289f73ac00a15f1cd46'},
{'q':'guam', 'appid':'cbdbbb3a98df1289f73ac00a15f1cd46'}]

# {'lat': '35.6828387','lon': '139.7594549','appid':'cbdbbb3a98df1289f73ac00a15f1cd46'},
# {'lat': '13.450125700000001','lon': '144.75755102972062','appid':'cbdbbb3a98df1289f73ac00a15f1cd46'},
# {'lat': '43.7311424','lon': '7.4197576','appid':'cbdbbb3a98df1289f73ac00a15f1cd46'}

for i in params_list:
    
    # 주석다는습관
    response = requests.get(url, params=i)

    # status 가 200이 되지않으면 에러로 출력
    if response.status_code == 200:
        print(response.content)
        
        # 값이 리스트가 아닌 경우
        if response.text !='[]':
            import json
            content = json.loads(response.content)
            
            # mongoDB 저장
            from pymongo import MongoClient
            # mongodb에 접속 -> 자원에 대한 class
            mongoClient = MongoClient("mongodb://python_selenium_drive_mongo-db_mongodb_7-1:27017")
            # database 연결
            database = mongoClient["study_finance"] 
            #collection 작업
            collection = database['coordinatesbylocationonnme']
            
            result = collection.insert_many(content)
        else:
            # 값이 없을때
            print(f'result empty : {response.text}')
    else:
        print(f'error : {response.status_code}')
        