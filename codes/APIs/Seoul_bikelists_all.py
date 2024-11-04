import requests
import json
import pandas as pd
import pydeck as pdk
from pymongo import MongoClient

# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://python_selenium_drive_mongo-db_mongodb_7-1:27017")
# database 연결
database = mongoClient["Seoul_bikes_all"]
#collection 작업
collection = database["Seoul_bikes_all"]


#함수사용
def main():
    #자료요청
    uri_all=[f'http://openapi.seoul.go.kr:8088/72696a654168656135334a4a5a456d/json/bikeList/1/999/',
            f'http://openapi.seoul.go.kr:8088/72696a654168656135334a4a5a456d/json/bikeList/1000/1999/',
            f'http://openapi.seoul.go.kr:8088/72696a654168656135334a4a5a456d/json/bikeList/2000/2703/']
    
    result = []
    for url in uri_all:
        response = requests.get(url = url)
    
        # 응답결과 status = 200 이면 출력    
        if response.status_code == 200:
            print(f'{response.text}')
       
            # data.dict 변수에 json 형태로 담기
            data_dict = json.loads(response.text)
            
            # 받을 변수 딕셔너리형태로 만들고 data_bikes 변수에 넣기
            data_bikes ={"stationName":[]
                        , "parkingBikeTotCnt":[]
                        , "stationLatitude":[]
                        , "stationLongitude":[]}

            # for 문을 사용하여 설정한 데이터 값 출력하기
            # 이중 for문 사용? for data_dict in range(1,2703):
            for row in data_dict['rentBikeStatus']['row']:
                print(f'stationName : {row["stationName"]}, parkingBikeToCnt : {row["parkingBikeTotCnt"]}')
                data_bikes ['stationName'].append(row["stationName"])
                data_bikes ['parkingBikeTotCnt'].append(int(row["parkingBikeTotCnt"]))
                data_bikes ['stationLatitude'].append(float(row["stationLatitude"]))
                data_bikes ['stationLongitude'].append(float(row["stationLongitude"]))
                pass    
            result.append(data_bikes)
        # 판다스 데이터프레임에 넣은 data_bikes를 df 변수에 넣기
        df = pd.DataFrame(data_bikes)
        pass    

        # Scatter plot 그리기
        layer = pdk.Layer(
                "ScatterplotLayer",
                df,
                get_position = ["stationLongitude", "stationLatitude"],
                get_fill_color = ["255-shared", "255-shared", "255"],
                get_radius = "60 * parkingBikeTotCnt / 100",
                pickable = True,
        )
        # 서울의 중심점 좌표 구해 지도 만들기
        lat_center = df["stationLatitude"].mean()
        lon_center = df["stationLongitude"].mean()
        initial_view = pdk.ViewState(latitude=lat_center, longitude=lon_center, zoom=10)
        map = pdk.Deck(layers=[layer], initial_view_state=initial_view, tooltip={"text":"대여소 : {stationName}\n현재 주차 대수 : {parkingBikeTotCnt}"})
        map.to_html("./seoul_bike_all.html")    
    else : 
        pass    # 에러 메세지 출력
        return
    return
    
if __name__=='__main__':
    main()
    pass