import schedule
import time

def start1():
    print("3초 마다 Test입니다.")

def start2():
    print("1분 마다 Test입니다.")


schedule.every(3).seconds.do(start1) # 3초마다 start1 실행
schedule.every(1).minutes.do(start2) # 1분마다 start2 실행
schedule.every().minute.at(":23").do(start1) #매분마다 23초 실행
schedule.every().hour.at(":23").do(start2) #매시간마다 23분에 실행

while True:
    schedule.run_pending()
    time.sleep(1)
