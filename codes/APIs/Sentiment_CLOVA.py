import requests
import json

def main():
    uri = f'https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze'
    headers = {
        'X-NCP-APIGW-API-KEY-ID' : 'mlm0ok8meu'
        , 'X-NCP-APIGW-API-KEY' : '3U5jyV3A12dXmQmcCdYcouJvjjHjbMofc5EexYAW'
        , 'Content-Type':'application/json'
    }
    bodys = {
            "content": "아침밥과 함께하는 따뜻한 영상"
            }        
            
    response = requests.post(url = uri, headers = headers, data =json.dumps(bodys))
    contents = json.loads(response.text)
    return

if __name__=='__main__':
    main()
    pass