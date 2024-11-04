import requests

def main():
    # 자료 요청
    uri = f'http://openapi.seoul.go.kr:8088/72696a654168656135334a4a5a456d/json/bikeList/1/5/'
    response = requests.get(url=uri)
    
    # 응답결과 200 이면 출력
    if response.status_code == 200:
        print(f'{response.text}')
        import json
        
        # data_dict 변수에 제이슨 형태로 담기
        data_dict = json.loads(response.text)
        data_dict
        #{'rentBikeStatus': {'list_total_count': 5, 'RESULT': {...}, 'row': [...]}}
        
        # data_dict 타입확인
        type(data_dict)
        
        #<class 'dict'>
        # data = {
        #       'name': ["Choi", "Choi", "Choi", "Kim", "Park"], 
        #       'year': [2013, 2014, 2015, 2016, 2017], 
        #       'points': [1.5, 1.7, 3.6, 2.4, 2.9]
        #       }
        
        # 받을 변수 딕셔너리 형태로 만들고 data_bikes 변수에 담기
        data_bikes = {"stationName":[]
                , "parkingBikeTotCnt":[]
                , "stationLatitude":[]
                , "stationLongitude":[]} 

        # for문을 사용하여 설정한 데이터 값 출력하기
        for row in data_dict['rentBikeStatus']['row']:
            print(f'stationName : {row["stationName"]}, parkingBikeTotCnt : {row["parkingBikeTotCnt"]}')
            data_bikes ['stationName'].append(row["stationName"])
            data_bikes ['parkingBikeTotCnt'].append(int(row["parkingBikeTotCnt"]))
            data_bikes ['stationLatitude'].append(float(row["stationLatitude"]))
            data_bikes ['stationLongitude'].append(float(row["stationLongitude"]))
            pass
        
        import pandas as pd
        
        #판다스 데이터프레임에 넣은 data_bikes를 df 변수에 넣기
        df = pd.DataFrame(data_bikes)
        pass
    
        import pydeck as pdk
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
        map.to_html("./seoul_bike.html")    
    else : 
        pass    # 에러 메세지 출력
    return

if __name__=='__main__':
    main()
    pass