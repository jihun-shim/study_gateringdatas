import requests

def main():
    try : 
        pass
        # html 파일 요청
        response = requests.get('https://www.mk.co/')
    except Exception as e:
        pass
        response = requests.get('https://www.mk.co.kr/')
    return response

if __name__=='__main__':
    main()
    pass