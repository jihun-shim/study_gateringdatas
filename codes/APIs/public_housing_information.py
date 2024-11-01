# + 국토교통부_법정동코드
#  + https://www.data.go.kr/data/15058476/openapi.do
# - 한국도로교통공단_자전거 교통사고 다발지역 정보 수집
# - 지역 : 시도 이하 적용

import requests

#주소와 파라미터
url = 'http://apis.data.go.kr/B552061/frequentzoneBicycle/getRestFrequentzoneBicycle'
params ={
    # XleMEo5Ty3YJwsQoxcazl3mWivEv0RDL7Ks4RFIcNLcAylV9POlpSl3vskumAqAbLdM7nJzogqrqkxVq4VCmRw%3D%3D
        'ServiceKey' : 'XleMEo5Ty3YJwsQoxcazl3mWivEv0RDL7Ks4RFIcNLcAylV9POlpSl3vskumAqAbLdM7nJzogqrqkxVq4VCmRw==', 
        'searchYearCd' : '2023', 
        'siDo' : '11', 
        'guGun' : '680', 
        'type' : 'json',
        'numOfRows' : '10',
        'pageNo' : '1'
        }

#응답
response = requests.get(url, params=params)
print(response.content)

#만약 정상적이지 않다면 출력되게 하는 코드
from bs4 import BeautifulSoup
if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'xml')
    print(soup.prettify())
    return_auth_msg = soup.find('returnAuthMsg')
    if return_auth_msg != None :
        print(response.text)
    else :
        print(f'return_auth_msg : {return_auth_msg}')
    pass
    print(response.text)
pass