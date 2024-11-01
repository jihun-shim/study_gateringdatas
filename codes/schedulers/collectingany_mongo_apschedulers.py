from get_classes import getfunctions as gf
from get_insert import getinsert_mongo as gm
from get_download_image import get_image as gi
from apscheduler.schedulers.background import BackgroundScheduler
from pymongo import MongoClient

temp = 'temp message'
import time
def main(message):
    
    # 스케쥴러 등록
    scheduler = BackgroundScheduler()
    scheduler.add_job(gf.message_print, trigger='interval', seconds=1, coalesce=True, max_instances=1)
    scheduler.add_job(gf.job_print, trigger='interval', seconds=1, coalesce=True, max_instances=1)
    scheduler.add_job(gm.main, trigger='interval', seconds=1, coalesce=True, max_instances=1)
    scheduler.add_job(gi.main, trigger='interval', seconds=1, coalesce=True, max_instances=1)
    scheduler.start()
    # 정지 예방
    count = 0
    while True:
        time.sleep(1)
        print(f'{message} : count - {count}')
        count = count + 1
        pass
    return True

if __name__ == '__main__':
    main('task forever!')
    pass