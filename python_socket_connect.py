import socket

ip = '192.168.163.132' #Metasploitable2
ports = [21, 22, 23, 80, 8080, 8180, 8888]

for port in ports:    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #SOCK_STREAM : TCP
    #SOCK_DGRAM : UDP
    result = sock.connect_ex((ip, port))
    print(port, ":", result)
    sock.close()

