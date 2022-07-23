import socket
import sys
#에러 넘버값 관련 패키지
import errno


#IP입력
remoteServer = input("점검할 호스트 IP를 입력: ")
#호스트 이름을 소켓으로 저장
remoteServerIP  = socket.gethostbyname(remoteServer)
print("스캔할 포트 범위를 입력하세요")
startPort    = input("시작 포트")
endPort    = input("마지막 포트 번호: ")
print("스캔 중입니다. 호스트: ", remoteServerIP)

try:
    #문자열로 받은 포트를 정수형으로 적용
    for port in range(int(startPort),int(endPort)):
        
        #소켓 연결하고 특정시간만큼 반응이 없으면 지나감
        print ("Checking port {} ...".format(port))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((remoteServerIP, port))
        
        # 0이면 Open 그 외 숫자면 Close 상태
        if result == 0:
            print("포트 {}: Open".format(port))
        else:
            print("포트 {}: Closed".format(port))
            print("Reason:",errno.errorcode[result])
            sock.close()
            
except socket.error:
    print("서버에 연결할 수 없습니다.")
    sys.exit()
    
print('포트 스캔이 완료되었습니다.')
