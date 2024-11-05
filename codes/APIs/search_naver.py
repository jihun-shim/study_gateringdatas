import requests
import json

def main():
    # postman에서 입력한 값 대입
    uri = f'https://openapi.naver.com/v1/search/blog'
    # params 와 headers 구분하기 params 입력 후 headers 값 입력
    params = {'query':'진주'}
    headers = {
        'X-Naver-Client-Id' : 'h99Roh4XOVpiiYZvgRVM'
        , 'X-Naver-Client-Secret' : 'Lbi3coWjV1'
    }
    
    #response 에 받을 requests.get 설정 하기
    response = requests.get(url=uri, params = params , headers = headers) # like postman
    
    # 만약 response.status_code 값이 200이면 아래와 같이출력
    if response.status_code == 200: # 200 == 200
        
        # contents 에 json 형태로 loads한 resoponse.text 담기
        contents = json.loads(response.text)    # python에서 다루기 편하게 format 수정
        pass
    return

if __name__=='__main__':
    main()
    pass