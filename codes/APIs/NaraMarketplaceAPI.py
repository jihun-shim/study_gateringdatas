# 조달청 표준정보수집

import requests

url =f'http://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo?serviceKey=XleMEo5Ty3YJwsQoxcazl3mWivEv0RDL7Ks4RFIcNLcAylV9POlpSl3vskumAqAbLdM7nJzogqrqkxVq4VCmRw%3D%3D&pageNo=1&numOfRows=10&type=json&bidNtceBgnDt=201712010000&bidNtceEndDt=201712312359'

url = f'http://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo'
params = {
    # XleMEo5Ty3YJwsQoxcazl3mWivEv0RDL7Ks4RFIcNLcAylV9POlpSl3vskumAqAbLdM7nJzogqrqkxVq4VCmRw==
        'serviceKey':'XleMEo5Ty3YJwsQoxcazl3mWivEv0RDL7Ks4RFIcNLcAylV9POlpSl3vskumAqAbLdM7nJzogqrqkxVq4VCmRw=='
        ,'pageNo':'1'
        ,'numOfRows':'10'
        ,'type':'json'
        ,'bidNtceBgnDt':'201712010000'
        ,'bidNtceEndDt':'201712312359'
         }

response = requests.get(url,params=params)

from bs4 import BeautifulSoup
if response.status_code == 200:
    # '<OpenAPI_ServiceResponse>\n\t<cmmMsgHeader>\n\t\t<errMsg>SERVICE ERROR</errMsg>\n\t\t<returnAuthMsg>SERVICE_KEY_IS_NOT_REGISTERED_ERROR</returnAuthMsg>\n\t\t<returnReasonCode>30</returnReasonCode>\n\t</cmmMsgHeader>\n</OpenAPI_ServiceResponse>'
    
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