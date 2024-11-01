import requests

# ?&&&&&
url = 'https://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo'
params ={'serviceKey' : 'XleMEo5Ty3YJwsQoxcazl3mWivEv0RDL7Ks4RFIcNLcAylV9POlpSl3vskumAqAbLdM7nJzogqrqkxVq4VCmRw%3D%3D'
         , 'pageNo' : '1'
         , 'numOfRows' : '10'
         , 'type' : 'json'
         , 'bidNtceBgnDt' : '201712010000'
         , 'bidNtceEndDt' : '201712312359' }

response = requests.get(url, params=params)
print(response.content)
