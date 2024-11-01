from CoordinatesbylocationnameWithErrors import requests



def main():
    
    # ?lat={lat}&lon={lon}&appid={API key}
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params ={'q':'tokyo',
            }

    # 'Tokyo lat': 35.6828387, 'lon': 139.7594549,
    # 'Guam' 'lat': 13.450125700000001, 'lon': 144.75755102972062
    # 'Monaco' 'lat': 43.7311424, 'lon': 7.4197576



    response = requests.get(url, params=params)
    if response.status_code == 200:
        #print(response.content)
        if response.text !='[]':
            import json
            content = json.loads(response.content)
            
            # mongoDB 저장
            from pymongo import MongoClient
            # mongodb에 접속 -> 자원에 대한 class
            mongoClient = MongoClient("mongodb://python_selenium_drive_mongo-db_mongodb_7-1:27017")
            # database 연결
            database = mongoClient["study_finance"]
            # collection 작업
            collection = database['forecast30_openweathermap']
            
            result = collection.insert_many(content)
        
        else :
            print(f'result empty : {response.text}')
    else:
        print(f'error : {response.status_code}')    
    
if __name__=='__main__':
    main()
    pass    